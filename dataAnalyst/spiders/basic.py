# -*- coding: utf-8 -*-
import datetime
import urlparse
import socket
import scrapy

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader
from scrapy.http import Request

from dataAnalyst.items import DataanalystItem


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["51job.com"]

    # Start on the first index page
    start_urls = (
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
    )
    


    def parse(self, response):
        item = DataanalystItem()
        # Get the next index URLs and yield Requests
        next_selector = response.xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[8]/a//@href')
        for url in next_selector.extract():
            yield Request(urlparse.urljoin(response.url, url))
        # Get item URLs and yield Requests
        item_selector = response.xpath('//*[@class="t1 "]/span/a//@href')
        for url in item_selector.extract():
            yield Request(urlparse.urljoin(response.url, url),callback=self.parse_item)

    def parse_item(self, response):
    
        l = ItemLoader(item=DataanalystItem(), response=response)

        # Load fields using XPath expressions
        #keys in old csv
        #   companyShortName
        #   positionAdvantage                 
        #   positionLables       

        l.add_xpath('city', '/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[1]',MapCompose(unicode.strip))
        l.add_xpath('companyFullName', '/html/body/div[3]/div[2]/div[2]/div/div[1]/p[1]/a[1]//@title',MapCompose(unicode.strip))
        l.add_xpath('companyLabelList', '//*[@class="sp4"]/text()',MapCompose(unicode.strip))
        l.add_xpath('companySize', '/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[2]/text()',MapCompose(unicode.strip))
        l.add_xpath('businessZones', '/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()',MapCompose(unicode.strip))
        l.add_xpath('firstType', '/html/body/div[3]/div[2]/div[3]/div[1]/div/div[1]/p/span[2]/text()',MapCompose(unicode.strip))
        l.add_value('secondType', '')
        l.add_xpath('secondType', '/html/body/div[3]/div[2]/div[3]/div[1]/div/div[1]/p/span[3]/text()',MapCompose(unicode.strip))
        l.add_xpath('education', '/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[3]',MapCompose(unicode.strip))
        
        l.add_xpath('industryField', '/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[3]/text()',MapCompose(unicode.strip))
        l.add_xpath('positionName', '/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()',MapCompose(unicode.strip))
        
        l.add_xpath('salary', '/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()',MapCompose(unicode.strip))
        l.add_xpath('workYear', '/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()[2]',MapCompose(unicode.strip))
        l.add_xpath('companyIdURL','//*[@class="com_name "]/@href',MapCompose(unicode.strip))
        l.add_xpath('positionId','//*[@id="hidJobID"]//@value',MapCompose(unicode.strip))
        l.add_xpath('positionMessage','//*[@class="bmsg job_msg inbox"]/p/text()',MapCompose(unicode.strip))

        
        #l.add_xpath('title', '//*[@itemprop="name"][1]/text()',
        #            MapCompose(unicode.strip, unicode.title))
        #l.add_xpath('price', './/*[@itemprop="price"][1]/text()',
        #            MapCompose(lambda i: i.replace(',', ''), float),
        #            re='[,.0-9]+')
        #l.add_xpath('description', '//*[@itemprop="description"][1]/text()',
        #            MapCompose(unicode.strip), Join())
        #l.add_xpath('address',
        #            '//*[@itemtype="http://schema.org/Place"][1]/text()',
        #            MapCompose(unicode.strip))
        #l.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src',
        #            MapCompose(lambda i: urlparse.urljoin(response.url, i)))

        # Housekeeping fields
        l.add_value('url', response.url)
        #l.add_value('project', self.settings.get('BOT_NAME'))
        #l.add_value('spider', self.name)
        #l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())
        return l.load_item()