import pymongo
from pymongo import MongoClient
import urllib.request 
import json
import os
import pprint


def generate_database():
	#establishiung a connection
	client = MongoClient()
	#accessing Databases
	db = client.Airport_data
	airport = db.Airport_data
	
	#we are now opening the json file
	with urllib.request.urlopen("https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json") as url:
		data = json.loads(url.read())
	#now we are loading data json file into our database
	airport.insert(data)



def Search(category, value):
	client = MongoClient()
	#accessing Databases
	db = client.Airport_data
	airport = db.Airport_data

	wanted = airport.find_one({category : value})
	print("Here are the information of your request airport information: \n")
	pprint.pprint(wanted)




if __name__ == "__main__":
	generate_database()
	print( "Here are the several categories for the airport: 'code','lat','lon','name','city','state','country','woeid','tz','phone','type','email','url','runway_length','elev','icao','direct_flights','carriers'! ")
	category = input("What category do you want to know about these airport? ")
	value = input("Please specify the value of the input category!")
	Search(category, value)
	








