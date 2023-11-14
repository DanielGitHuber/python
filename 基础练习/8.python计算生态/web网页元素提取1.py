def getHtml():
    f = open('html1.html', 'r', encoding='utf-8')
    ls = f.readlines()
    f.close()
    return ls


def extractImageUrls(htmlLines):
    urls = []
    for line in htmlLines:
        if 'http' in line:
            url = 'http' + line.split('http')[-1].split('"')[0]
            urls.append(url)
    return urls


def showResults(urls):
    count = 0
    for url in urls:
        print('第{:2}个URL：{}'.format(count, url))
        count += 1


def saveResults(urls):
    f = open('html1_urls.txt', 'w')
    for url in urls:
        f.write(url + '\n')
    f.close()


def main():
    htmlLines = getHtml()
    urls = extractImageUrls(htmlLines)
    showResults(urls)
    saveResults(urls)


main()
