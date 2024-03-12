import scrapy
import root_data

# Global
RootDataList = root_data.RootData()

# Spider class for Scrapy
class RootDataSpider(scrapy.Spider):
    # Prpoerties
    name = 'root_data_spider'
    start_urls = ['https://www.rootdata.com/Projects']

    # Default parse method for Scrapy
    def parse(self, response):
        try:            
            # Get all the project names            
            for href in response.css('div > a.list_name.animation_underline').extract():            
                RootDataList.projectNames.append(href)

            # Get all the tags
            for href in response.css('div.tag_list.keep_all').extract():            
                RootDataList.tags.append(href)

            # Get all the descriptions
            for href in response.css('span.intro.keep_all').extract():            
                RootDataList.descriptions.append(href)
                                
        except Exception as e:
            print("Exception: ", e )

