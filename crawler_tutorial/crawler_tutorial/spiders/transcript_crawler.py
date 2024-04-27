import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptCrawlerSpider(CrawlSpider):
    name = "transcript_crawler"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies_letter-X"]
    rules=(
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths=('(//a[@rel="next"])[1]'))),
)

    def parse_item(self, response):
        article = response.xpath('//article[@class="main-article"]')
        yield{
            "Title":article.xpath('./h1/text()').get(),
            "Plot": article.xpath('./p/text()').get(),
            # "Transcript":article.xpath('./div/text()').getall(),
            "Url":response.url,
        }