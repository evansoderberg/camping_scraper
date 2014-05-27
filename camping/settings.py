# Scrapy settings for camping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'camping'

SPIDER_MODULES = ['camping.spiders']
NEWSPIDER_MODULE = 'camping.spiders'
DEFAULT_ITEM_CLASS = 'camping.items.CampSite'
ITEM_PIPELINES = {'camping.pipelines.CampingPipeline': 1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'camping (+http://www.yourdomain.com)'
