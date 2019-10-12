import requests 
from application.lib import singleton
from bs4 import BeautifulSoup 
import re

STYLE_TAG_REG = r"<style>([^<]|\n)*<\/style>"
SCRIPT_TAG_REG = r"<script[^>]*>([^<]|\n)*<\/script>"
SPECIAL_CHARACTER_REG = r"(\n|\r|\t)"
INGORE_WORD = ['', '|', '-']

@singleton
class ParserProvider(object):
    
    def clean_html_tag(self, text):
        text = re.sub(STYLE_TAG_REG, "", text)
        text = re.sub(SCRIPT_TAG_REG, "", text)
        return text
    
    def clean_unused_characters(self, text):
        text = re.sub(SPECIAL_CHARACTER_REG, " ", text)
        return [*filter(lambda i: i not in INGORE_WORD, text.split(' '))]

    def execute(self, text): 
        text = self.clean_html_tag(text)
        soup_text = BeautifulSoup(text,'html.parser').get_text()   
        return self.clean_unused_characters(soup_text)