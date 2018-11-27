from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def gather_images(url):
    query = raw_input("Enter Directroy Name: ")
    image_type=query
    query= query.split()

    query='+'.join(query)
    print(url)
    #add the directory for your image here
    DIR="Pictures"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)


    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print("there are total" , len(ActualImages),"images")

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    DIR = os.path.join(DIR, query.split()[0])

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    ###print images
    for i , (img , Type) in enumerate( ActualImages):
        try:
            req = urllib2.Request(img, headers={'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()

            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            print(cntr)
            if len(Type)==0:
                f = open(os.path.join(DIR , image_type + "2_" + str(cntr)+".jpg"), 'wb')
            else :
                f = open(os.path.join(DIR , image_type + "2_" +  str(cntr)+"."+Type), 'wb')


            f.write(raw_img)
            f.close()
        except Exception as e:
            print("could not load : "+img)
            print(e)

gather_images("https://www.google.com.eg/search?tbm=isch&q=sleep+faces&chips=q:sleep+faces,online_chips:sleep+deprivation&usg=AI4_-kRot2Q9tJyt4_Ra4zahXuxigHIPAQ&sa=X&ved=0ahUKEwjykNazme_eAhUGBSwKHXutAdwQ4lYIJygB&biw=1920&bih=901&dpr=1")
