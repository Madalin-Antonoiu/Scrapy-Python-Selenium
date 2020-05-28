import scrapy
import timeago, datetime

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
         #adding 3 minutes ago to





        ### REMOVE TBODY FROM ANY XPATH ! WARNING


       # print(response.xpath('/html/body/div/table/tr[3]/td[7]/div/a/text()').get()) # Works
                                        #### Table Rows ####
        for ticket in response.xpath('/html/body/div/table/tr[position() > 2]'): # don't put get or extract here, > 2 because first two are header rows

            item = TicketItem()


            # This for is needed because every xpath.extract gives a list with all of them, and need parsed individually

            for date in ticket.xpath('normalize-space(./td[11]/div/text())').extract(): # date string grabbed from every xpath
                datetime_object = datetime.datetime.strptime(date, '%d/%m/%Y %I:%M %p') # formatted into proper datetime date object (comes like '27/05/2020 12:17 PM' on the website)
                time_ago = timeago.format(datetime_object, datetime.datetime.now()) # given date vs time taken now to povide time ago
                item['time_ago'] = time_ago + ' (' + date + ')' # and finally, i have the time ago ( date ) for double check!

            item['id'] = ticket.xpath('normalize-space(./td[6]/div/text())').extract()
            item['subject'] = ticket.xpath('td[7]/div/a/text()').extract()

            yield item

        open_in_browser(response)

        # print(response) #.text
        # first_ticket = response.selector.xpath('//*[@id="RequestsView_r_0_6"]/div/a/text()').get()
        # print(first_ticket)

        # table_rows = response.xpath('//*[@id="RequestsView_TABLE"]/tbody/tr').extract()
        # print(table_rows)

        # mydiv = response.xpath("//div").extract()
        # print(mydiv)



















        # CTRL + Z + Enter to terminate Scrapy shell

        # response.css('title')
        #   response.css('#RequestsView_r_0_6 > div > a')
        #
        #
        #
        #
        #
        #

        # Open in Browser
        # open_in_browser(response)

        # Write scrape result to HTML file
        #with open('page.html', 'wb') as html_file:
        #   html_file.write(response.body)


#To run this program in the shell

# scrapy shell https://servicedesk.csiltd.co.uk/RequestsView.cc?requestViewChanged=true&viewName=36502_MyView&globalViewName=All_Requests
# then write this in the shell

 # def parse(self, response):
 #        user = 'antonoium'
 #        password = 'madutzu93classiC'
 #        token = response.css('form input::attr(value)').extract_first()      # print(token) #RememberMeLoginModule hidden value
 #        return FormRequest.from_response(response, formdata={
 #            'AUTHRULE_NAME': token,
 #            'j_username': user,
 #            'j_password': password,
 #            'dname': '0',
 #            'DOMAIN_NAME': '-',
 #            'LDAPEnable': 'false',
 #            'hidden': 'Select a Domain',
 #            'hidden': 'For Domain',
 #            'AdEnable': 'false',
 #            'DomainCount': '3',
 #            'LocalAuth': 'No',
 #            'LocalAuthWithDomain': 'Not in Domain',
 #            'dynamicUserAddition_status': 'true',
 #            'localAuthEnable': 'true',
 #            'logonDomainName': '-1',
 #            'checkbox': 'checkbox'
 #        }, callback=self.start_scraping)
 #
 #    def start_scraping(self, response):

 # then all you do is type response and you have all the code lol, and you are authenticated