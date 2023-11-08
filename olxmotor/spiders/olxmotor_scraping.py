import scrapy

class OlxmotorScrapingSpider(scrapy.Spider):
    name = "olxmotor_scraping"
    allowed_domains = ["www.olx.co.id"]

    def start_requests(self):
        starts_url = "https://www.olx.co.id/motor-bekas_c200?page={}"
        for page_number in range(31): #looping page 1 to 30
            url = starts_url.format(page_number)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        price = response.css('._2Ks63::text').extract()
        year = response.css('.YBbhy::text').extract()
        brand = response.css('._2poNJ::text').extract()

        for item in zip(price, year, brand):
            items_info = {
                'price': item[0],
                'year': item[1],
                'brand': item[2]
            }

            yield items_info
