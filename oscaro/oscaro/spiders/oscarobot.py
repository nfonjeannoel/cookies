import scrapy
from lxml.html import open_in_browser
from scrapy.shell import inspect_response
class OscarobotSpider(scrapy.Spider):
    name = 'oscarobot'
    # start_urls = ['https://www.oscaro.es/']

    def start_requests(self):
        h = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'no-cache', 'pragma': 'no-cache', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

        yield scrapy.Request(url="https://www.oscaro.es", headers=h)

    def parse(self, response):
        inspect_response(response, self)
        open_in_browser(response)
        print(response)
