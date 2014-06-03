from scrapy.spider import Spider
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request

from camping.items import CampSite

class AusCampSpider(CrawlSpider):
    name = 'aus_camp'
    allowed_domains = ['australiancampsites.com.au']
    start_urls = [
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=20&Itemid=80",
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=22&Itemid=82",
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=15&Itemid=81",
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=15&Itemid=81&limitstart=50",
    ]

    rules = (Rule (SgmlLinkExtractor(restrict_xpaths=('//*/a[@class="blogsection"]', )), callback="parse_items", follow=True),)

    def parse_items(self, response):
        sel = Selector(response)

        name = sel.xpath('//*/span[@style="font-size: xx-large;"]/text()').extract()[0]
        spans = sel.xpath('//*/span')

        details = None
        lat = None
        lon = None
        for index, item in enumerate(spans):
            try:
                if item.xpath('text()').extract()[0].find("GPS") > -1:
                    details = item.xpath('text()').extract()[0]
                    g = details.find('GPS')
                    c = details.find(':', g)
                    coords = details[c+2:-1]
                    lat = float(coords.split(',')[0])
                    lon = float(coords.split(',')[1])
            except IndexError:
                pass

        item = CampSite()
        item['name'] = name
        item['url'] = response.url
        item['lat'] = lat
        item['lon'] = lon
        
        return item
