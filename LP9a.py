# 9)A) Write a python program to download the all XKCD comics

import requests
import os

os.makedirs('xkcd', exist_ok=True)
url = 'https://xkcd.com/info.0.json'
response = requests.get(url)
response.raise_for_status()
latest_comic = response.json()['num']

for comic_num in range(latest_comic, 0, -1):
    url = f'https://xkcd.com/{comic_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comic_data = response.json()

    image_url = comic_data['img']
    response = requests.get(image_url)
    response.raise_for_status()

    file_name = os.path.basename(image_url)
    
    with open(f'xkcd/{file_name}', 'wb') as image_file:
        for chunk in response.iter_content(100000):
            image_file.write(chunk)
    print(f'Downloaded {file_name}')

