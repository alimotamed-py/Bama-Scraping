import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

cars = []
with open('carurl.txt') as car_url:
    cars_url = car_url.read().split(',')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}

for url in cars_url:
    print(f'\n🔎 در حال پردازش: {url}')

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html5lib')
    car_dict = dict()

    # ____________________ TOP SECTION ____________________

    title = soup.find(class_='bama-ad-detail-title__title')
    model = soup.find_all(class_='bama-ad-detail-title__subtitle')
    year = model[0].text.strip()
    real_model = model[1].text.strip()
    time = soup.find(class_='bama-ad-detail-title__ad-time')
    price = soup.find(class_='bama-ad-detail-price__price')
    if price.text.strip() == 'توافقی':
        price = price.text.strip()
    else:
        price = float(price.text.replace(',', ''))

    location = soup.find(class_='address-text')
    description = soup.find(class_='description')
    if description:
        description = description.text
    else:
        description = ''

    # _____________________________________________________

    # ____________________ DETAIL _________________________

    keys = []
    car_detail_item_keys = soup.select('.bama-vehicle-detail-with-icon__detail-holder span')
    detail_keys = [item.text for item in car_detail_item_keys if car_detail_item_keys]
    car_detail_item_values = soup.select('.bama-vehicle-detail-with-icon__detail-holder p')
    detail_values = [item.text for item in car_detail_item_values if car_detail_item_values]
    car_detail_dict = {detail_keys[i]: detail_values[i] for i in range(len(detail_keys)) if detail_keys}

    # _____________________________________________________

    # ____________________ TECKNICAL DETAIL _______________

    technical_detail_keys = soup.find_all(class_='bama-vehicle-detail-with-link__row-title')
    technical_keys = [item.text.strip() for item in technical_detail_keys if technical_detail_keys]
    technical_detail_values = soup.find_all(class_='bama-vehicle-detail-with-link__row-text')
    technical_values = [item.text.strip() for item in technical_detail_values if technical_detail_values]
    technical_dict = {technical_keys[i]: technical_values[i] for i in range(len(technical_keys)) if technical_keys}

    # ______________________________________________________

    car_dict.update({

        'نام': title.text,
        'سال ساخت': year,
        'مدل': real_model,
        'تایم': time.text,
        'قیمت': price,
        'آدرس': location.text,
        'توضیحات': description,

    })
    car_dict.update(car_detail_dict)
    car_dict.update(technical_dict)
    cars.append(car_dict)

    print(f'✅ اطلاعات ثبت شد: {car_dict["نام"]} - {car_dict["قیمت"]}')

# ____________________ JSON FILE ____________________
with open('car.json', 'w', encoding='utf-8') as car:
    json.dump(cars, car, ensure_ascii=False, indent=2)

# ____________________ EXCEL FILE ____________________
df = pd.DataFrame(cars)  #
df.to_excel('cars.xlsx', index=False, engine='openpyxl')

print('\n📁 ذخیره‌سازی فایل‌ها کامل شد!')
