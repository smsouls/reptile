import urllib
import urllib.request
from lxml import etree
import os

def handle_request(url, page):
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))

    headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0)Gecko/20100101 Firefox/60.0'}
    request = urllib.request.Request(url=url, headers=headers)
    return request

def download_image(image_src):
    dirpath = 'pic'
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    filename = image_src.attrib['alt'] + '.jpg'
    filepath = os.path.join(dirpath, filename)
    headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0)Gecko/20100101 Firefox/60.0'}
    image_url = image_src.attrib['src2'].replace('Files', 'files')
    image_url = image_url.replace('_s', '')
    image_url = 'http:' + image_url
    request = urllib.request.Request(url=image_url, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def parse_content(content):
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img[@src2]')
    for image_src in image_list:
        download_image(image_src)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'http://sc.chinaz.com/tupian/fengjingtupian{}.html'
    start_page = 1
    end_page = 2
    for page in range(start_page, end_page):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)


