# get full resolution images from google
# and save them to a folder

from bs4 import BeautifulSoup
import requests
import os


def get_images(query, num_images):
    url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"
    print(url)
    # get the html from the url
    response = requests.get(url)
    # parse the html
    soup = BeautifulSoup(response.text, "html.parser")
    # get the image links
    links = []
    for img in soup.find_all("img"):
        if img.get("src"):
            links.append(img.get("src"))
    # download the images
    x = 0
    for link in links:
        x += 1
        requests.get(link)
        with open("images/" + query + str(x) + ".jpg", "wb") as f:
            f.write(response.content)
            f.close()
        print("could not download image")


get_images("cat", 10)
