"""GoogleSpider."""
import scrapy


class GoogleSpider(scrapy.Spider):
    """Scraper for google serach."""

    name = "googel_spider"

    def __init__(self, first, last):
        """Initialize the spider."""
        super(GoogleSpider, self).__init__(first, last)
        self.start_urls = ['http://www.google.com/search?q={first}+{last}&start=1'.format(first, last)]

    def parse(self, response):
        """Crawl through search and return first page information."""
        SET_SELECTOR = '.g'
        for post in response.css(SET_SELECTOR):

            TITLE_SELECTOR = 'h3 a ::text'
            SITE_SELECTOR = 'h3 a ::attr(href)'
            yield{
                'title': post.css(TITLE_SELECTOR).extract(),
                'site': post.css(SITE_SELECTOR).extract_first()
            }
