import logging
from urllib import response

import requests
from lxml import etree

count=0
url_in="https://bangumi.tv/"
for page in range(1,353):
    url = f"https://bangumi.tv/anime/browser?sort=rank&page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    res=requests.get(url,headers=headers)
    res.encoding = res.apparent_encoding
    page=res.text
    html=etree.HTML(page)
    anime_list=html.xpath('//div[@class="section"]/ul/li')
    for anime in anime_list:
        count=count+1
        title=anime.xpath('./div[@class="inner"]/h3/a/text()')[0]
        mark=anime.xpath('./div[@class="inner"]/p[@class="rateInfo"]/small/text()')[0]
        rank=anime.xpath('div[@class="inner"]/span/small/text()')[0]
        url = anime.xpath('./div[@class="inner"]/h3/a/@href')[0]
        print(f"Rank {count}:{title},评分:{mark},链接:{url_in}{url}")