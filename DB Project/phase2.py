import tweepy
from tweepy import OAuthHandler
import json
import wget

import os
from base64 import b64encode
from os import makedirs
from os.path import join, basename
from sys import argv
import requests

import io

import PIL
from PIL import Image, ImageDraw, ImageFont

#Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#import MongoDB library
import pymongo
from pymongo import MongoClient
import pprint



def main():
    twitter_username = input("Enter the twitter account name of the twitter account you want to download from: ")
     # Please change the * below to your twitter development access keys

    consumer_key = 'NFDMpk1Fg8ceijtkGERJc2Z2a'
    consumer_secret = '8tvTg2rnY53XzSdrpKFcZruVOSJSHWPdutwMRg6U8XddoqPx3y'
    access_token = '956294196301791233-tzh1DeLpyEh3i7sVinidNTzUK7A6pRy'
    access_secret = 'DCavGa4IkSQDviwhFimXzqYu2gELIQU6F5DtqErberFlT'

    @classmethod
    def parse(cls, api, raw):
        status = cls.first_parse(api, raw)
        setattr(status, 'json', json.dumps(raw))
        return status
     
    # Status() is the data model for a tweet
    tweepy.models.Status.first_parse = tweepy.models.Status.parse
    tweepy.models.Status.parse = parse
    # User() is the data model for a user profil
    tweepy.models.User.first_parse = tweepy.models.User.parse
    tweepy.models.User.parse = parse
    # You need to do it for all the models you need
     
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
     
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=twitter_username,
                               count=200, include_rts=False,
                               exclude_replies=True)
    last_id = tweets[-1].id
     
    while (True):
        more_tweets = api.user_timeline(screen_name=twitter_username,
                                    count=200,
                                    include_rts=False,
                                    exclude_replies=True,
                                    max_id=last_id-1)
      # There are no more tweets
        if (len(more_tweets) == 0):
            break
        else:
            last_id = more_tweets[-1].id-1
            tweets = tweets + more_tweets

    media_files = set()
    for status in tweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
     
    for media_file in media_files:
        wget.download(media_file)
#-------------------------------------------- Implementation of the google API and generate Labels-------------------------------



    counter = -1
    for item in media_files:
        if (counter < 200):
            counter = counter +1
            address = '/Users/borishuang/Desktop/EC500/' + str(counter) + '.jpg'
            #Please put in the desired directory for storing pictures
            wget.download(item,address)

    counter_two = 0
    client = vision.ImageAnnotatorClient()
    

    description_label =[]
    percentage_label=[]
    for x in range(0, counter +1):
        counter_two += x 
        name = str(counter_two) + '.jpg'

        path = os.getcwd()
        with io.open(path + '/' + name, 'rb') as image_file:
            content = image_file.read();

        image = types.Image(content = content)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        #Rename and superposition labels on the pictures
        new = 'new' +str(counter_two)+'.jpg'
        image = Image.open(name)
        draw = ImageDraw.Draw(image)
        y_coordinate = 70


        for item in labels: 
            word = item.description
            score = item.score
            y_coordinate += 10
            draw.text((200, y_coordinate), text = word, fill=(250,250,250))
            #print(word)
            description_label.append(word)
            percentage_label.append(score)


        image.save(new)
        newcommand = "rm " +name;
        print(newcommand)
        os.system(newcommand)

    result= zip(description_label,percentage_label)
    resultset = set(result)


#    Using ffmpeg

    os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")

    return resultset, twitter_username

# def generate_db():
#     establishiung a connection
#     client = MongoClient()
#     #accessing Databases
#     db = client.twitter_data
#     twitter = db.twitter_data
#     #populate the data with user's labels
#     twitter.insert(labels)
#     #print out all the labels stored as json file
#     pprint.pprint(twitter)

def Search(category, value):
    client = MongoClient()
    #accessing Databases
    db = client.og
    twitter = db.og
    wanted = twitter.find({category : value})
    print("Here is the percentage of requested label from the pictures: \n")
    pprint.pprint(wanted) 
    




if __name__ == "__main__":
    b,k = main()
    client = MongoClient()
    #accessing Databases
    db = client.og
    twitter = db.og
    #populate the data with user's labels
    c = dict(b)
    print(c)
    twitter.insert(c)

    category = input("What label do you want to know about the pictures from designated twitter account? ")
    value = input("Please specify the value of the input category: ")
    Search(category, value)
    
    



