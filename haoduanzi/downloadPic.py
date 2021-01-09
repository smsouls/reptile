import urllib

def handle_request(url, page):
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))

    headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0)Gecko/20100101 Firefox/60.0'}
    request = urllib.request.Request(url=url, headers=headers)
    return request


if __name__ == '__main__':
    url = 'http://sc.chinaz.com/tupian/fengjingtupian{}.html'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page, end_page + 1):
        print('开始爬取第%s页' % page)
        request = handle_request(url, page)