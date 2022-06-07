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
    
    # get the images for the first 10 links
    for link in links[:number_of_images]:
        try:
            # get the image url
            img_url = link.get('href')[7:].split('&sa=')[0]
            print(link)
            # get the image name
            img_name = img_url.split('/')[-1]
            # get the image
            img_data = requests.get(img_url).content
            # save the image
            with open(os.path.join('images', img_name), 'wb') as handler:
                handler.write(img_data)
        except:
            error('Error: image not found')


get_images("Biohackers", 10)
