import time
import os
import datetime




while True:
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('crawl time is :',nowTime,'.......................')
    os.system("scrapy crawl launchPosition")
    time.sleep(86400)  #每隔一天运行一次 24*60*60=86400s