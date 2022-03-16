import scrapy

class Webcrawler(scrapy.Spider):
    name = "rescale"
    start_urls = ["http://www.rescale.com"]  

    def parse(self, response):
        """ This function parses a sample response
        @url http://www.rescale.com
        @returns items 211
        @returns requests 0 0
        @scrapes link
        """
        for href in response.xpath('//a'):
            # convert to string object
            href_to_save = href.xpath('string(./@href)').get()

            if href_to_save:
                # for sub paths that begin with / and re-route to rescale.com
                if href_to_save[0] == '/':
                    href_to_save = 'http://www.rescale.com' + href_to_save
                yield {'link': href_to_save}
