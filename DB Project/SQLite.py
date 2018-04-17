# Python code to demonstrate SQL to fetch data.
# importing the module
import sqlite3
import project

def generate_sqlDB(a, b):
	# connect withe the myTable database
	connection = sqlite3.connect("boxi.db")
	 
	# cursor object
	crsr = connection.cursor()
	 
	# execute the command to fetch all the data from the table emp
	crsr.execute('CREATE TABLE tweepy(twitter_account TEXT, Labels TEXT)') 

	#crsr.execute("INSERT INTO tweepy(twitter_account, Labels) VALUES (?, ?)", (twitter_account, Labels))
	# crsr.execute("INSERT INTO tweepy VALUES(1,'chicken')")
	# crsr.execute("INSERT INTO tweepy VALUES(2,'cake')")
	# crsr.execute("INSERT INTO tweepy VALUES(3,'dingdong')")	
	 
	Labels = {}
	for i in twitter_account:
		Labels[i] = []
		data = project.module(i, int(num_tweet))
		if type(data) == dict:
			for item in data['0']:
				Labels[name].append(item)

	for key, value in Labels.items():
	keys = key
	values= value
	for item in values:
		crsr.execute("INSERT INTO tweepy (keys, item) VALUES (?, ?)", (keys, item))

	connection.commit()

	for row in crsr.execute('SELECT * FROM tweepy ORDER BY Labels'):
		print(row)

	# close the connection
	crsr.close()
	connection.close()

if __name__ == '__main__':
	twitter_account = input('Please insert your twitter account name here: \n')
	num_tweet = input('Please tell me the number of the tweet you wants: \n')
	twitter_account = twitter_account.split('')
	generate_sqlDB(twitter_account, num_tweet)





