import scrapy
from scrapy.http import FormRequest
from facebook_spider.items import FacebookFriend
from scrapy.loader import ItemLoader

class FacebookSpider(scrapy.Spider):
    name = 'friend_crawler'
    allowed_domains = ['m.facebook.com']
    start_urls = ['http://m.facebook.com/']
    root_url = 'https://m.facebook.com'

    def __init__(self, *args, **kwargs):
        super(FacebookSpider, self).__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.user_id =  kwargs.get('uid')
        self.proxy = kwargs.get('proxy', None)
        self.page = 0

    def parse(self, response):
        return [FormRequest('https://m.facebook.com/login.php',
            formdata={
                'email': self.email,
                'pass': self.password
            }, callback=self.parse_post_login)
        ]

    def parse_post_login(self, response):
        return scrapy.Request(self.root_url + '/' + self.user_id + '/friends',
                              callback=self.get_friends)

    def get_friends(self, response):
        if self.page == 0:
            path = '//body/div/div/div[2]/div/div/div[2]/div'
        else:
            path = '//body/div/div/div[2]/div/div/div/div'

        for friend in response.xpath(path):
            l = ItemLoader(FacebookFriend(), selector=friend)
            l.add_xpath('name', './/table/tbody/tr/td[2]/a/text()')
            l.add_xpath('url_profile', './/table/tbody/tr/td[2]/a/@href')
            yield l.load_item()

        if self.page == 0:
            path_to_next = '//body/div/div/div[2]/div/div/div[3]/a/@href'
            self.page = 1
        else:
            path_to_next = '//body/div/div/div[2]/div/div/div[2]/a/@href'

        next_page = response.xpath(path_to_next).extract_first()
        if next_page != None:
            yield scrapy.Request(self.root_url + next_page,
                                  callback=self.get_friends)
