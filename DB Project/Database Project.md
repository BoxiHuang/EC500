
### Phase 1 is within the file: Mongo.py
### Phase 2 is within the files: Phase2_v2.py (phase2 is my first try of Phase2)
### Phase 3 is within the file: TBD


# Phase 1:
#### Assignment Objective:
Phase 1: Learn mongdb --> Go through Mongo DB tutorial Install all Pyhton related SW and drivers 
Write a python program to import the airport location data 
Demonstrate the following functions Read data Update data Search and find data


#### Code Briefing:
Mongo.py contains a function of populating a mongo database and stores all information of airport data within Airport_data collection.
Moreover, the code contains two search functions which allow users to select either search one or multiple data points. User needs to provide "category" and "value" in order to search.

#### HOW TO USE:

Please make sure the following library are within the code:
import pymongo
from pymongo import MongoClient
import urllib.request 
import json

Complie and run this code.
The module will automatically generate a database to store all airport data from "https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json"
and prompts the user to enter a category as well as a value. Users have the option to select whether they would love to search one or multiple data points from the database.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Phase 2: 
#### Assignment Objective:
Go back to Project 1: Twitter+FFMPEG+Google Vision 
Design database to implement persistent user stories 
Detail information of every transaction the user may run using your system 
Retrieve information about twitter handles in your system, 
Description of the media they have 
Description of videos generated 
Collective statistics about overall usage of the system. (For example Number of images per feed) 
Most popular descriptors Relationship between Google Trending terms and Twitter feeds

#### HOW TO USE:
Complie and run this code.
Please enter your consumer access, consumer key, access token, access secret as guided in command line window.
The module will then prompt the user to enter the twitter account name as well as the number of images. 
As soon as these two pieces of information are pushed into the module, the code will start download pictures from designated twitter account 
and run GOOGLE vision API to analyze each downloaded picture. And later ffmpeg is called and generated a video with all the pictures that are annotated. 
In the assignment, a function which populates a database with all the annotations is called. 

# The data structure within the database:

### Twitter account:
twitter account name

### Picture Data:
Picture Number : #
Label: all the labels from that one picture

Users are able to generate the conduct search by providing twitter account and picture number. The linked labels are then pushed to the command line window for user to observe.

 
