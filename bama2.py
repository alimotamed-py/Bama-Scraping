import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

cars = []

with open('carurl.txt', encoding='utf-8') as car_url:
    cars_url = car_url.read().split(',')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

for url in cars_url:
    print(f'\n🔎 در حال پردازش: {url}')
    try:
        response = requests.get(url.strip(), headers=headers)
        soup = BeautifulSoup(response.text, 'html5lib')
        car_dict = {}

        # ---------------------- TOP SECTION ----------------------
        title = soup.find(class_='bama-ad-detail-title__title')
        title = title.text.strip() if title else ''

        model = soup.find_all(class_='bama-ad-detail-title__subtitle')
        model_year = model[0].text.strip() if len(model) > 0 else ''
        real_model = model[1].text.strip() if len(model) > 1 else ''

        time = soup.find(class_='bama-ad-detail-title__ad-time')
        time = time.text.strip() if time else ''

        price_tag = soup.find(class_='bama-ad-detail-price__price')
        if price_tag:
            price_text = price_tag.text.strip()
            if price_text == 'توافقی':
                price_text = 'توافقی'
            else:
                price_text = float(price_text.replace(',', ''))
        else:
            price_text = ''

        location = soup.find(class_='address-text')
        location = location.text.strip() if location else ''

        description = soup.find(class_='description')
        description = description.text.strip() if description else ''

        image = soup.find('img', class_='ad-image')
        image_url = image['src'] if image and image.get('src') else ''

        # ---------------------- DETAIL SECTION ----------------------

        detail_keys = [item.text.strip() for item in soup.select('.bama-vehicle-detail-with-icon__detail-holder span')]
        detail_values = [item.text.strip() for item in soup.select('.bama-vehicle-detail-with-icon__detail-holder p')]
        car_detail_dict = {detail_keys[i]: detail_values[i] for i in range(min(len(detail_keys), len(detail_values)))}

        # ---------------------- TECHNICAL DETAIL ----------------------

        technical_keys = [item.text.strip() for item in
                          soup.find_all(class_='bama-vehicle-detail-with-link__row-title')]
        technical_values = [item.text.strip() for item in
                            soup.find_all(class_='bama-vehicle-detail-with-link__row-text')]
        technical_dict = {technical_keys[i]: technical_values[i] for i in
                          range(min(len(technical_keys), len(technical_values)))}

        # ---------------------- ITEM DICT -----------------------------
        car_dict.update({
            'نام': title,
            'سال ساخت': model_year,
            'مدل': real_model,
            'تایم': time,
            'قیمت': price_text,
            'آدرس': location,
            'توضیحات': description,
            'تصویر': image_url,
        })
        car_dict.update(car_detail_dict)
        car_dict.update(technical_dict)
        cars.append(car_dict)

        print(f'✅ اطلاعات ثبت شد: {car_dict["نام"]} - {car_dict["قیمت"]}')

    except Exception as e:
        print(f'❌ خطا در پردازش {url}: {e}')
        continue

# ---------------------- SAVE JSON FILE ----------------------
with open('car.json', 'w', encoding='utf-8') as car:
    json.dump(cars, car, ensure_ascii=False, indent=2)

# ---------------------- SAVE EXCEL FILE ----------------------
df = pd.DataFrame(cars)
df.to_excel('cars.xlsx', index=False, engine='openpyxl')

print('\n📁 ذخیره‌سازی فایل‌ها کامل شد!')
