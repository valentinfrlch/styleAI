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
    # get the images
    # only get images with a height of at least 200
    # if img.get('height') >= 200
    images = [img for img in soup.find_all('img')]
    # save the images
    for img in images[:number_of_images]:
        if img.startswith('http'):
            with open("dataset/" + search_term + images.index(img) + '.jpg', 'wb') as f:
                f.write(requests.get(img).content)


get_images("Biohackers", 10)
