from scrapy.spider import Spider
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request

from camping.items import CampSite

class ParkWebVicSpider(CrawlSpider):
    name = 'parkweb_vic'
    allowed_domains = ['parkweb.vic.gov.au']
    start_urls = [
        "http://parkweb.vic.gov.au/explore/parks/great-otway-national-park/things-to-do/camping"
    ]

    rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//*/tr/td/p/a', )), callback="parse_items", follow=True),)

    def parse_items(self, response):
        sel = Selector(response)

        name = sel.xpath('//*/h1[@class="page-title"]/text()').extract()[0]
        description = sel.xpath('//*/div[@class="overview section"]/p/text()').extract()

        lat = None
        lon = None


        item = CampSite()
        item['name'] = name
        item['url'] = response.url
        item['lat'] = lat
        item['lon'] = lon
        item['description'] = description
        
        return item
