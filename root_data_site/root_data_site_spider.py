import scrapy
import root_data_item

class RootDataSpider(scrapy.Spider):
    name = 'root_data_spider'
    start_urls = ['https://www.rootdata.com/Projects']

    def parse(self, response):
        try:            
            for href in response.css('div > a.list_name.animation_underline').extract():            
                data = response.css('list_name animation_underline::text').get()
                print("href:", href )    
                print("data:", data )    
                #yield response.follow(href, self.parse_root_data_item_detail)
        except Exception as e:
            print("Exception: ", e )

    def parse_root_data_item_detail(self, response):
        try:
            data = response.css('css-selector-for-title::text').get()
            
            #item['title'] = response.css('css-selector-for-title::text').get()
            #item['company'] = response.css('css-selector-for-company::text').get()
            
            #item['description'] = response.css('css-selector-for-description::text').getall()  # Use getall() if the description is split across multiple tags
            #item['link'] = response.url  # The link to the detail page (already available)

            # Use the summarizer to summarize the description
            #summarizer = Summarizer()
            #item['description'] = summarizer.summarize(' '.join(item['description']))

            yield data
        except Exception as e:
            print("Exception: ", e )

            
