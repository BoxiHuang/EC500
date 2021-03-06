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
		#pprint.pprint(data)
	#now we are loading data json file into our database
	airport.insert(data)

	

def Search(category, value):
	client = MongoClient()
	#accessing Databases
	db = client.Airport_data

	airport = db.Airport_data

	wanted = airport.find_one({category : value})
	print("Here are the information of your requested airport information: \n")
	for item in wanted:
		pprint.pprint(wanted)


def Search_mulitple(category, value):
	client = MongoClient()
	#accessing Databases
	db = client.Airport_data

	airport = db.Airport_data

	wanted = airport.find({category : value})
	print("Here are the information of your requested airports information: \n")
	for item in wanted:
		pprint.pprint(item)


if __name__ == "__main__":
	generate_database()
	method = input("Do you want to search for one airport or multiple airports? \n If yes, please input 1 for just one, else 0 for multiple airports: ")
	if(method == 0):
		print( "Here are the several categories for the airport: 'code','lat','lon','name','city','state','country','woeid','tz','phone','type','email','url','runway_length','elev','icao','direct_flights','carriers'! ")
		category = input("What category do you want to know about the airport? ")
		value = input("Please specify the value of the input category: ")
		Search(category, value)
	else:
		category = input("What category do you want to know about the airport? Please specify: ")
		value = input("Please specify the value of the input category: ")
		Search_mulitple(category, value)










