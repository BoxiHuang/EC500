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

	'''
	data1 = {
	"code": "AAA",
	"lat": "-17.3595",
	"lon": "-145.494",
	"name": "Anaa Airport",
	"city": "Anaa",
	"state": "Tuamotu-Gambier",
	"country": "French Polynesia",
	"woeid": "12512819",
	"tz": "Pacific\/Midway",
	"phone": "",
	"type": "Airports",
	"email": "",
	"url": "",
	"runway_length": "4921",
	"elev": "7",
	"icao": "NTGA",
	"direct_flights": "2",
	"carriers": "1"
	}
	data2 ={
	"code": "AAE",
	"lat": "36.8236",
	"lon": "7.8103",
	"name": "El Mellah Airport",
	"city": "El Tarf",
	"state": "Annaba",
	"country": "Algeria",
	"woeid": "12510325",
	"tz": "Africa\/Algiers",
	"phone": "",
	"type": "Airports",
	"email": "",
	"url": "",
	"runway_length": "9843",
	"elev": "16",
	"icao": "DABB",
	"direct_flights": "6",
	"carriers": "2"
	}
	data3 ={
	"code": "AAE",
	"lat": "36.8236",
	"lon": "7.8103",
	"name": "El Mellah Airport",
	"city": "El Tarf",
	"state": "Annaba",
	"country": "Algeria",
	"woeid": "12510325",
	"tz": "Africa\/Algiers",
	"phone": "",
	"type": "Airports",
	"email": "",
	"url": "",
	"runway_length": "9843",
	"elev": "16",
	"icao": "DABB",
	"direct_flights": "6",
	"carriers": "2"

	}


	result = airport.insert_many([data1,data2,data3])
	print('Multiple airport: {0}'.format(result.inserted_ids))
	'''
	

def Search(category, value):
	client = MongoClient()
	#accessing Databases
	db = client.Airport_data

	airport = db.Airport_data

	wanted = airport.find_one({category : value})
	print("Here are the information of your request airport information: \n")
	pprint.pprint(wanted)

#def update();



if __name__ == "__main__":
	generate_database()
	print( "Here are the several categories for the airport: 'code','lat','lon','name','city','state','country','woeid','tz','phone','type','email','url','runway_length','elev','icao','direct_flights','carriers'! ")
	category = input("What category do you want to know about the airport? ")
	value = input("Please specify the value of the input category!")
	Search(category, value)
	#update()








