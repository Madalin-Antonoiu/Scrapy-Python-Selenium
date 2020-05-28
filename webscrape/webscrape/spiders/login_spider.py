import datetime
import scrapy
import timeago
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class TicketItem(scrapy.Item):
    id = scrapy.Field()
    time_ago = scrapy.Field()
    subject = scrapy.Field()

class LoginSpider(scrapy.Spider):
    name = "login_spider"
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'scrape_test.csv'
    }
    start_urls = [
        #'https://servicedesk.csiltd.co.uk/RequestsView.cc' # Base Url where i can access ticket data
        'https://servicedesk.csiltd.co.uk/RequestsView.cc?requestViewChanged=true&viewName=36502_MyView&globalViewName=All_Requests' # Service Desk Unassigned
    ]

    def parse(self, response):
        user = 'antonoium'
        password = 'madutzu93classiC'
        token = response.css('form input::attr(value)').extract_first()      # print(token) #RememberMeLoginModule hidden value
        return FormRequest.from_response(response, formdata={
            'AUTHRULE_NAME': token,
            'j_username': user,
            'j_password': password,
            'dname': '0',
            'DOMAIN_NAME': '-',
            'LDAPEnable': 'false',
            'hidden': 'Select a Domain',
            'hidden': 'For Domain',
            'AdEnable': 'false',
            'DomainCount': '3',
            'LocalAuth': 'No',
            'LocalAuthWithDomain': 'Not in Domain',
            'dynamicUserAddition_status': 'true',
            'localAuthEnable': 'true',
            'logonDomainName': '-1',
            'checkbox': 'checkbox'
        }, callback=self.start_scraping)

    @staticmethod
    def start_scraping(response):

        ### REMOVE TBODY FROM ANY XPATH ! WARNING, else [] empty response
        for ticket in response.xpath('/html/body/div/table/tr[position() > 2]'): # don't put get or extract here, > 2 because first two are header rows

            item = TicketItem()

            for date in ticket.xpath('normalize-space(./td[11]/div/text())').extract(): # date string grabbed from every xpath
                datetime_object = datetime.datetime.strptime(date, '%d/%m/%Y %I:%M %p') # formatted into proper datetime date object (comes like '27/05/2020 12:17 PM' on the website)
                time_ago = timeago.format(datetime_object, datetime.datetime.now()) # given date vs time taken now to povide time ago
                item['time_ago'] = time_ago + ' (' + date + ')' # and finally, i have the time ago ( date ) for double check!

            item['id'] = ticket.xpath('normalize-space(./td[6]/div/text())').extract()
            item['subject'] = ticket.xpath('td[7]/div/a/text()').extract()

            yield item

        open_in_browser(response)
