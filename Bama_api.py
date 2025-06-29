import requests
from urllib.parse import urljoin

urls = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
for i in range(1, 4):
    params = {'pageIndex': i}
    url = 'https://bama.ir/cad/api/search'

    response = requests.get(url, headers=headers, params=params)

    data = response.json()['data']['ads']
    for item in data:
        if item.get('detail'):
            url = urljoin('https://bama.ir', item['detail']['url'])
            urls.append(url)

with open('carurl.txt', 'w') as carurl:
    carurl.write(','.join(urls))

print('\n📁 فایل کامل شد!')
