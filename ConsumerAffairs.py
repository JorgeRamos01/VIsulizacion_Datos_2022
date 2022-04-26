import scrapy
from datetime import datetime

class consumerAffairsSpider(scrapy.Spider):
	name= "CAffairs"
	start_urls = ["https://www.consumeraffairs.com/insurance/bluecross_fl.html", 
	"https://www.consumeraffairs.com/insurance/anthem.html",
	"https://www.consumeraffairs.com/insurance/united_health_care.html"]
	handle_httpstatus_list = [403]

	def parse(self, response):
		now=datetime.now()
		producto=response.css('.prf-hdr__cpy-nm::text').get()
		for reviews in response.css('div[itemprop="reviews"]'):
			try:
				yield{
					'webpage': "www.consumeraffairs.com",
					'product': producto,
					'date_review': reviews.css('div:nth-child(3) > span:nth-child(1)::text').get().split(": ")[1],
					'user': reviews.css('div:nth-child(2) > div:nth-child(2) > strong:nth-child(1)::text').get().split(" of")[0],
					'review':reviews.css('div[itemprop="reviews"] > div:nth-child(3) > p::text').get()+" "+reviews.css('div[itemprop="reviews"] > div:nth-child(3) > div> p::text').get(),
					'grade': response.css('div[itemprop="reviews"] > div:nth-child(1) > div:nth-child(1) > meta[itemprop="ratingValue"]').attrib['content'],
					'extrac_date':now

				}
			except:
				try:
					yield{
						'webpage': "www.consumeraffairs.com",
						'product': producto,
						'date_review': reviews.css('div:nth-child(3) > span:nth-child(1)::text').get().split(": ")[1],
						'user': reviews.css('div:nth-child(2) > div:nth-child(2) > strong:nth-child(1)::text').get().split(" of")[0],
						'review':reviews.css('div[itemprop="reviews"] > div:nth-child(3) > p::text').get(),
						'grade': response.css('div[itemprop="reviews"] > div:nth-child(1) > div:nth-child(1) > meta[itemprop="ratingValue"]').attrib['content'],
						'extrac_date':now
					}
				except:
					yield{
						'webpage': "www.consumeraffairs.com",
						'product': producto,
						'date_review': reviews.css('span.ca-txt-cpt:nth-child(2)::text').get().split(": ")[1],
						'user': reviews.css('div:nth-child(2) > div:nth-child(2) > strong:nth-child(1)::text').get().split(" of")[0],
						'review':reviews.css('div[itemprop="reviews"] > div:nth-child(3) > p::text').get(),
						'grade': response.css('div[itemprop="reviews"] > div:nth-child(1) > div:nth-child(1) > meta[itemprop="ratingValue"]').attrib['content'],
						'extrac_date':now
					}

		next_page = response.css('a.ca-btn:nth-child(7)').attrib['href']

		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)
		else:
			raise CloseSpider('Done')




