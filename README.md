# Scrapy-Python
Logging via Forms into any website and scraping it with callbacks

**How to start building spiders with Scrapy** :

1 Right Click on Desktop - **Open with Code**   
2 `CTRL +'` to **open VS Code Terminal (cmd) **.  
3 `py -m venv venv` - create a desktop virtual environment for python  
4 `.\venv\Scripts\activate` - to be in venv mode, you can now install packages locally to this project  
5 `pip install scrapy` - Needs Microsoft 14++ installed, see my email sent to myself  

See **login_spider**.py for how to log in to a website before crawling  
See **time**.py for how to format datetime to make time_ago time  
See **saving_spider**.py for how to save locally information to a file.  
**PyCharm** ( needs Git installed for VSC) is really cool IDE for Python.

**You know how to**:
- Crawl a webpage and extract data
- Authenticate to a webpage then crawl and extract
- Save data in csv and json format
- Open browser with scraped data automatically
- Extract any piece of information you want exactly with css selectors and Xpath

**Other useful commands**:
- `CTRL + Z + Enter` to terminate Scrapy shell
- `//from scrapy.utils.response import open_in_browser  
  //open_in_browser(response)` - auto open new Chrome window with scraped data
- `scrapy shell 'https://your_link'` - cool to test things
- Save scraped data as html document locally:  
`with open('page.html', 'wb') as html_file:  
              html_file.write(response.body)`
