import scrapy

# Root data item
class RootDataItem(scrapy.Item):
    # Define the fields for root data
    name = scrapy.Field()       
    tags = scrapy.Field()       
    ecosystem = scrapy.Field()
    intro = scrapy.Field()
