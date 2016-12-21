#!/usr/bin/python
# coding=utf-8

#from baike_spider import url_manager,html_downloader,html_parser,html_outputer
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    """docstring for SpiderMain"""
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        #如果管理器中有url, 下载，解析，把解析出的url放入 管理器，有用内容放入 收集器
        while  self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)