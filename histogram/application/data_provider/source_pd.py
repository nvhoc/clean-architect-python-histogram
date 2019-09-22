import os
import config
from application.lib import singleton

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = "{}".format(config.of().get('source_provider.browser'))
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome(chrome_path, options=chrome_options)

@singleton
class SourceProvider(object):
    def __init__(self, data_source, data_format):
        self.data_source = data_source
        self.data_format = data_format

    def get_plain_data(self, params):
        url = params.get('url')
        browser.get(url) 
        return browser.page_source