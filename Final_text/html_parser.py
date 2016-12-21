#!/usr/bin/python
# coding=utf-8

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
    """docstring for HtmlParser"""
    def __init__(self):
        pass

    def parser(self, page_url, html_cont):
        #print page_url
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        # /view/数字.htm
        # such as /view/123.htm
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            #print new_url
            #安装page_url 的格式，把new_url补全
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            #print new_full_url
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}   #字典

        # url
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title">
        #<h1>Python</h1>
        title_node = soup.find('dd',  class_= "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_= "lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data