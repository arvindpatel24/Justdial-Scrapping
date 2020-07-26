import scrapy
from ..items import JustdialItem

class JdSpider(scrapy.Spider):
    name = 'jd'

    domains = ['justdial.com']
    base_url = 'https://www.justdial.com/Delhi/House-On-Rent/nct-10192844/page-%s'
    start_urls = [base_url % 1]

    mapNum={'icon-dc':'+',
                'icon-fe':'(',
                'icon-hg':')',
                'icon-ba':'-',
                'icon-ji':9,
                'icon-lk':8,
                'icon-nm':7,
                'icon-po':6,
                'icon-rq':5,
                'icon-ts':4,
                'icon-vu':3,
                'icon-wx':2,
                'icon-yz':1,
                'icon-acb':0,
                }

    pageNo = 1

    def parse(self, response):
        # items = JustdialItem()

        # name = response.css('.lng_cont_name::text').extract()
        # rating = response.css('.green-box::text').extract()
        # address = response.css('.cont_fl_addr::text').extract()
        # all_number = response.css('.mobilesv').extract()

        # mobile = []
        # eachNum = ''
        # i=0
        # for span in all_number:
        # 	i=i+1
        # 	li = span.split('"')
        # 	index = li[1].replace('mobilesv ','')
        # 	eachNum = eachNum + str(self.mapNum[index])
        # 	if(i%16 == 0):
        # 		mobile.append(eachNum)
        # 		eachNum = ''

        # items['name'] = name
        # items['rating'] = rating
        # items['address'] = address 
        # items['mobile'] = mobile 

        # yield items

        items = JustdialItem()

        name = response.css('.lng_cont_name::text').extract()
        rating = response.css('.green-box::text').extract()
        address = response.css('.cont_fl_addr::text').extract()
        all_number = response.css('.mobilesv').extract()

        phone = []
        eachNum = ''
        i=0
        for span in all_number:
        	i=i+1
        	li = span.split('"')
        	index = li[1].replace('mobilesv ','')
        	if(i%16 > 6 or i%16 == 0):
        		eachNum = eachNum + str(self.mapNum[index])
        	if(i%16 == 0):
        		phone.append(eachNum)
        		eachNum = ''

        for i in range(len(name)):
        	yield {
        		'name' : name[i],
        		'rating' : rating[i],
        		'phone' : phone[i],
        		'address' : address[i],
        	}

        print(self.pageNo)
        self.pageNo = self.pageNo + 1
        if(self.pageNo < 11):
        	yield scrapy.Request(self.base_url % self.pageNo)



