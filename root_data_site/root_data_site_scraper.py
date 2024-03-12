from scrapy.crawler import CrawlerProcess
from root_data_site_spider import RootDataSpider
from root_data_site_spider import RootDataList

# Main program
try:
    # Define crawler process
    process = CrawlerProcess({
        'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
        'FILES_STORE': '/path/to/your/folder'
    })

    # Crawl through the site
    process.crawl(RootDataSpider)
    process.start()

    # Print the scraped properties
    # These can be stored in a file or a database for further querying
    print("Scraping complete.")
    print("Project Names scraped: \n----------------------\n", '\n '.join(str(href) for href in RootDataList.projectNames))
    print("Project Tags scraped: \n---------------------\n", '\n '.join(str(href) for href in RootDataList.tags))
    print("Project Descriptions scraped: \n-----------------------------\n", '\n '.join(str(href) for href in RootDataList.descriptions))

except Exception as e:
    print(f'Error in main: {e}')
