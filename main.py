# get images from a google search
# and save them in a folder

from distutils.log import error
import os
import sys
import requests
from bs4 import BeautifulSoup


def get_images(search_term, number_of_images):
    # get the url
    url = 'https://www.google.com/search?q=' + search_term + '&source=lnms&tbm=isch'
    # get the html
    html = requests.get(url).text
    # parse the html
    soup = BeautifulSoup(html, 'html.parser')
    # get all links
    links = soup.find_all('a')
    
    # if ends in jpg, png, jpeg
    def is_image(link):
        return link.get('href') and link.get('href').endswith(('.jpg', '.png', '.jpeg'))
    images = [link.get('href') for link in links if is_image(link)]
    print(images)



get_images("Biohackers", 10)
