# -*- coding: utf-8 -*-
import scrapy
import sys
import os
import datetime
from Launches.settings import FILES_STORE
from Launches.items import LaunchesItem
base_url = 'https://www.celestrak.com/NORAD/elements/'
class LaunchpositionSpider(scrapy.Spider):
    name = "launchPosition"
    allowed_domains = [""]
    url = base_url
    #url = "https://www.baidu.com"
    start_urls = [url]

    def parse(self, response):
        print('***********************  hello')
        #print('------------',sys.path[0])
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d')

        time_path = os.path.join(FILES_STORE,nowTime+'/'+'file_exp')
        if not os.path.exists(time_path):
            os.makedirs(time_path)
        describe = os.path.join(time_path,'read.txt')
        with open(describe,'w',encoding='utf-8') as tf:
            print('writing...')
            print(response)
            #print(response.xpath('/html/body/table[1]/tbody/tr/td'))
            #for table in response.selector.css('html>body>center>table>tr > td > table'):
            for table in response.selector.css('html>body>table>tr>td>table'):
                # table.css('table > tr > th > table > tr > td > a')
                #print(table)
                titles = table.css('tr > th::text').extract()
                if (len(titles) > 0):
                    title = titles[0]
                else:
                    continue
                print(title)
                for each in table.css('tr > td > a'):
                    each_url = each.css('a::attr(href)').extract()[0]
                    each_name = each.css('a::text').extract()[0]
                    tf.write(title + '--->' + each_name + '--->' + each_url + '\n')
            #for each in response.selector.css('html>body>center>table>tr>td>table>tr>td>a::text').extract():

        #for table in response.selector.css('html>body>center>table>tr > td > table'):
        for table in response.selector.css('html>body>table>tr>td>table'):
            #table.css('table > tr > th > table > tr > td > a')
            titles = table.css('tr > th::text').extract()
            if (len(titles)>0):
                title = titles[0]
            else:
                continue
            print(title)
            for each in table.css('tr > td > a'):
                each_url = each.css('a::attr(href)').extract()[0]
                each_name = each.css('a::text').extract()[0]
                # tf.write(title+'--->'+each_name+'--->'+each_url+'\n')
                print(title,'----',each_name)
                item = LaunchesItem()
                all_url = base_url + str(each_url)
                item['file_url'] = [all_url]
                item['file_path'] = [title]
                yield item
                # yield scrapy.Request(url=base_url + str(each),
                #                      callback=self.download_file)
                #tf.write('------'+each+'\n')

    # def download_file(self,response):
    #     print('zzzzzzzzzzzzzzzzzzz')
    #     print('======================',response.url())
        # item = LaunchesItem()
        # item['file_urls'] = response.url()
