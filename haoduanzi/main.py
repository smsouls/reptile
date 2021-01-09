import urllib
import urllib.request
from lxml import etree
import re


#!/usr/bin/python
# -*- coding: UTF-8 -*-

def handle_request(url, page):
    url = url.format(str(page))
    print(url)
    headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0)Gecko/20100101 Firefox/60.0'}

    request = urllib.request.Request(url=url, headers=headers)
    return request


def parse_content(content):
    tree = etree.HTML(content)
    li_list = tree.xpath('//ul[@class="list-box"]/li')
    for text_list in li_list:
        item = []
        try:
            title = text_list.xpath('./div/img/@alt')[0]
            content = text_list.xpath('./div/a/p/text()')
            if len(content) == 0:
                content = text_list.xpath('./div/a/text()')
            content = ''.join(content)
            content = re.sub(r'[(\n)(\u3000)]', '', str(content))
            item.append(title)
            item.append(content)
            item = '\n'.join(item) + '\n'

            with open('haoduanzi', 'a', encoding='utf8', newline='\n') as fp:
                fp.write(item)
                fp.write('\n')

        except:
            pass

if __name__ == '__main__':
    url = 'http://www.haoduanzi.com/category/?11-{}.html'

    start_page = 1
    end_page = 10

    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
