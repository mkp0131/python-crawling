import requests
import re
from bs4 import BeautifulSoup
import os

year_list = [2019, 2018, 2017, 2016]

for y in year_list:
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(
        y)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0'
    }

    res = requests.get(url, headers=headers)
    res.raise_for_status

    dir_name = './img/{0}'.format(y)
    if not os.path.isdir(dir_name):
        os.makedirs(os.path.join(dir_name))

    soup = BeautifulSoup(res.text, 'html.parser')
    d = soup.find(attrs={"class": "movie_list"}).find_all("li")

    for idx, item in enumerate(d):
        img_src = item.find(attrs={"class": "thumb_img"})['src']
        if img_src.startswith('//'):
            img_src = 'https:' + img_src

        print(img_src)
        img_res = requests.get(img_src, headers=headers)
        res.raise_for_status

        with open(dir_name + '/movie{0}.jpg'.format(idx + 1), 'wb') as f:
            f.write(img_res.content)

        if idx == 4:
            break
