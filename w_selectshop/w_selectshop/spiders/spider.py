import scrapy
import re
import numpy as np
from scrapy.http import TextResponse
from w_selectshop.items import WSelectshopItem

class SelectshopSpider(scrapy.Spider):
    name = "SelectshopSpider"
    allow_domain = ["https://www.wconcept.co.kr/"]
    start_urls = ["https://www.wconcept.co.kr/Brand"]

    def parse(self, response):
        count_set = []
        for num in range(1, 28):
            count1 = response.xpath('//*[@id="pajx_container"]/div[3]/div[{}]'.format(num)).extract()
            count_set.append(count1)

        count_total =[]
        for link in count_set:
            count2 = link[0].count('brand_card brand-card-popup')+1
            count_total.append(count2)      

        for alphabet, count in tuple(zip(list(range(1,28)), count_total)):
            for brand in range(1, count):
                child_code = response.xpath('//*[@id="pajx_container"]/div[3]/div[{}]/ul/li[{}]/a/@onclick'.format(alphabet, brand)).extract()[0]
                child_code = re.findall('\d+', child_code)[0]
                url = "https://www.wconcept.co.kr/Brand/{}?sort=1&mcd=M33439436&ccd=1_001000000".format(child_code)
                yield scrapy.Request(url, callback=self.page_parse)

    def page_parse(self, response):
        for num in range(1, 6):
            link = "https://www.wconcept.co.kr" + response.xpath('//*[@id="brandshop"]/div[3]/ul/li[{}]/a/@href'.format(num)).extract()[0]
            yield scrapy.Request(link, callback=self.item_parse)

    def item_parse(self, response):
        item = WSelectshopItem()
        try:    
            try:
                item['target'] = response.xpath('//*[@id="prdLocaiton"]/li[2]/button/text()').extract()[0]
            except:
                item['target'] = np.nan
            try:
                item['product'] = response.xpath('//*[@id="btn4depth"]/text()').extract()[0]
            except:
                item['product'] = np.nan
            try:
                item['brand'] = response.xpath('//*[@id="frmproduct"]/div[1]/h2/a/text()').extract()[0]
            except:
                item['brand'] = np.nan
            try:
                item['explain'] = response.xpath('//*[@id="frmproduct"]/div[1]/h3/text()').extract()[0]
            except:
                item['explain'] = np.nan
            try:
                item['origin_price'] = response.xpath('//*[@id="frmproduct"]/div[2]/dl/dd[1]/em/text()').extract()[0]
            except:
                item['origin_price'] = np.nan
            try: 
                item['now_price'] = response.xpath('//*[@id="frmproduct"]/div[2]/dl/dd[2]/em/text()').extract()[0]
            except:
                item['now_price'] = np.nan
            try: 
                item['star_score'] = response.xpath('//*[@id="reviewAvg2"]/text()').extract()[0]
            except:
                item['star_score'] = np.nan
            try:
                item['code'] = response.xpath('//*[@id="container"]/div/div/div[1]/div[2]/dl/dd/ul/li[1]/text()').extract()[1].replace("\r\n", "").replace("  ", "")
            except:
                item['code'] = np.nan
            try:
                item['material'] = response.xpath('//*[@id="container"]/div/div/div[1]/div[2]/dl/dd/ul/li[2]/text()').extract()[1].replace("\r\n", "").replace("  ", "")
            except:
                item['material'] = np.nan
            try:
                item['firm_madein'] = response.xpath('//*[@id="container"]/div/div/div[1]/div[2]/dl/dd/ul/li[3]/text()').extract()[1].replace("\r\n", "").replace("  ", "")
            except:
                item['firm_madein'] = np.nan
            try:
                item['material2'] = response.xpath('//*[@id="container"]/div/div/div[3]/table/tbody/tr[1]/td/text()').extract()[0]
            except:
                item['material2'] = np.nan
            try:
                item['firm_import'] = response.xpath('//*[@id="container"]/div/div/div[3]/table/tbody/tr[4]/td/text()').extract()[0]
            except:
                item['firm_import'] = np.nan
            try:
                item['made_in'] = response.xpath('//*[@id="container"]/div/div/div[3]/table/tbody/tr[5]/td/text()').extract()[0]
            except:
                item['made_in'] = np.nan
            try:
                item['birth'] = response.xpath('//*[@id="container"]/div/div/div[3]/table/tbody/tr[7]/td/text()').extract()[0]
            except:
                item['birth'] = np.nan
            try:
                item['image_link'] = response.xpath('//*[@id="tx_entry_63923_"]/@src').extract()[0]
            except:
                item['image_link'] = np.nan
            yield item
        except:
            pass