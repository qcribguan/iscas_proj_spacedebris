# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
import datetime
from scrapy.pipelines.files import FilesPipeline
from Launches.settings import FILES_STORE
from scrapy.exceptions import DropItem
class LaunchesPipeline(FilesPipeline):

    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self, item, info):
        for url in item["file_url"]:
            yield scrapy.Request(url)

    def file_path(self, request,response=None, info=None):
        """
        重命名模块
        """
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
        file_name = request.url.split('/')[-1]
        title = self.get_title(file_name)
        path = os.path.join(nowTime+'/'+title+'/',request.url.split('/')[-1])
        return path
    def get_title(self,curr_name):
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
        time_path = os.path.join(FILES_STORE, nowTime + '/' + 'file_exp')
        if not os.path.exists(time_path):
            os.makedirs(time_path)
        describe = os.path.join(time_path, 'read.txt')
        with open(describe, 'r', encoding='utf-8') as tf:
            lines = tf.readlines();
            for line in lines:
                list_name = line.strip().split('--->')
                if(curr_name == list_name[2]):
                    print(curr_name,list_name[0])
                    return list_name[0]

# strs = 'asdasd.asd.asd'
# print(strs.split('.')[0])