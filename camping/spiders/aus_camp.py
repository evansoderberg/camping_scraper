from scrapy.spider import Spider
from scrapy.selector import Selector

from camping.items import CampSite

class AusCampSpider(Spider):
    name = 'aus_camp'
    allowed_domains = ['australiancampsites.com.au']
    start_urls = [
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=20&Itemid=80",
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=22&Itemid=82",
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=15&Itemid=81",
        "http://australiancampsites.com.au/index.php?option=com_content&view=section&layout=blog&id=15&Itemid=81&limitstart=50",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*/a[@class="blogsection"]')
        items = []

        for site in sites:
            item = CampSite()
            item['name'] = site.xpath('text()').extract()[0]
            item['url'] = site.xpath('@href').extract()[0]
            items.append(item)
        
        return items
