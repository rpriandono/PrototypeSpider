from scrapy.item import Item, Field


class LivingSocialDeal(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    # Like a variable delcaration in GPL, but there is only one option type.
    # The item class behaves like dictionary in python.

    title = Field()
    link = Field()
    location = Field()
    original_price = Field()
    price = Field()
    end_date = Field()
