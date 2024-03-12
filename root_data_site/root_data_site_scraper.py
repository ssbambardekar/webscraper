from scrapy.crawler import CrawlerProcess
from root_data_site_spider import RootDataSpider

try:
    process = CrawlerProcess({
        'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
        'FILES_STORE': '/path/to/your/folder'
    })

    process.crawl(RootDataSpider)
    process.start()
except Exception as e:
    print(f'Error in main: {e}')
