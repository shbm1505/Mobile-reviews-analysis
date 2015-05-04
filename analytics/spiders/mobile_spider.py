import scrapy

class MobileSpider(scrapy.Spider):
    name = "mobile"
    allowed_domains = ["gsmarena.com"]
    start_urls = [
        "http://www.gsmarena.com/makers.php3",
       # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/" 
    ]

    def parse(self, response):
        for sel in response.xpath('//td/a'):
         #   title = sel.xpath('a/text()').extract()
          #  link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print desc
        