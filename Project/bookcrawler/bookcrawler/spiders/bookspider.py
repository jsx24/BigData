# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from urllib import  parse


class BookspiderSpider(RedisSpider, scrapy.Spider):
    name = 'book_spider'
    redis_key = "book_spider:start_urls"
    # start_urls = ['https://www.barnesandnoble.com/h/books/browse']

    def parse(self, response):
        superbject_scrope = response.xpath('//section[@class="links-container browse clearer"]/ul/li/ul/li')
        for item in superbject_scrope:
            subject_url = item.xpath('./a/@href').extract_first()
            subject_url = parse.urljoin(response.url, subject_url)
            subject = item.xpath('./a/text()').extract_first()

            yield scrapy.Request(url=subject_url,
                                 callback=self.parse_subject,
                                 meta={'subject':subject},
                                 dont_filter=True,
                                 )

    def parse_subject(self, response):
        """解析分类"""
        scopes = response.xpath('//ul[@class="lists lists--unstyled"]/li')
        for item in scopes:
            secondary_subject = item.xpath('./a/text()').extract_first()
            secondary_subject_url = item.xpath('./a/@href').extract_first()
            secondary_subject_url = parse.urljoin(response.url, secondary_subject_url)
            response.meta.update(secondary_subject=secondary_subject)
            yield scrapy.Request(url=secondary_subject_url,
                                 callback=self.parse_page_info,
                                 meta=response.meta,
                                 dont_filter=True)

    def parse_page_info(self, response):
        """解析详情页"""
        current_page_num = response.xpath('//li[@class="pagination__active"]/span/text()').extract_first()
        response.meta.update(current_page_num=current_page_num)
        book_urls = response.xpath('//a[@class="pImageLink "]/@href').extract()
        book_urls = [parse.urljoin(response.url, href) for href in book_urls]
        for book_url in book_urls:
            yield scrapy.Request(url=book_url,
                                 callback=self.parse_detail,
                                 meta=response.meta,
                                 dont_filter=False,)

        next_page_link = response.xpath('//a[@class="next-button"]/@href').extract_first()
        if next_page_link:
            yield scrapy.Request(url=parse.urljoin(response.url, next_page_link),
                                 callback=self.parse_page_info,
                                 meta=response.meta,
                                 dont_filter=True,)


    def parse_detail(self, response):
        """解析book 详情"""
        result = {}
        title = response.xpath('//h1[@class="pdp-header-title "]/text()').extract_first()
        author = response.xpath('//span[@id="key-contributors"]/a/text()').extract_first()
        avg_rating = response.xpath('//div[@class="bv_avgRating_component_container notranslate"]/text()').extract_first()
        reviews_num = response.xpath('//div[@class="bv_numReviews_text"]/text()').extract_first()
        if reviews_num:
            reviews_num = reviews_num.strip('(').strip(')')
        price = response.xpath('//span[@id="pdp-cur-price"]/text()').extract_first()
        old_price = response.xpath('//s[@class="old-price"]/text()').extract_first()
        if old_price:
            old_price=old_price.strip('$')
        isbn = response.xpath('//th[contains(.,"ISBN")]/parent::*/td/text()').extract_first()
        publisher = response.xpath('//th[contains(.,"Publisher")]/parent::*/td/a/span/text()').extract_first()
        pages= response.xpath('//th[contains(.,"Pages")]/parent::*/td/text()').extract_first()
        sales_rank = response.xpath('//th[contains(.,"Sales rank")]/parent::*/td/text()').extract_first()
        pub_date = response.xpath('//th[contains(.,"Publication date")]/parent::*/td/text()').extract_first()
        product_dimensions = response.xpath('//th[contains(.,"Product dimensions")]/parent::*/td/text()').extract_first()

        result.update(subject=response.meta['subject'],
                      secondary_subject = response.meta['secondary_subject'],
                      current_page_num = response.meta['current_page_num'],
                      title = title,
                      author=author,
                      avg_rating=avg_rating,
                      reviews_num=reviews_num,
                      price=price,
                      old_price=old_price,
                      isbn=isbn,
                      publisher=publisher,
                      pages=pages,
                      sales_rank=sales_rank,
                      pub_date=pub_date,
                      product_dimensions=product_dimensions,
                      url=response.url,

                      )
        yield result




