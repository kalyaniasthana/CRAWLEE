import tweepy #open source library to access Twitter's API

#declare the variable consumer_key,consumer_secret,access_token,access_token_secret for your registered Twitter app here.
#consumer_key="......."
#consumer_secret="........"
#access_token="........"
#access_token_secret="........"

#creating a tweepy api object with the four kets defined above
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
id=input("Enter id to be searched: ")

try: #for a valid user id
	user=api.get_user(id) #returns information about the specified user as an object(stored in variable 'user') of the class API 
	print("Screen name: ",user.screen_name)
	print("User name: ",user.name)
	print("Description: ",user.description)
	print("User location: ",user.location)
	print("Time zone: ",user.time_zone)
	print("Number of followers: ",user.followers_count)
	print("Number of friends: ",user.friends_count)
	print("Number of statuses: ",user.statuses_count)
	print("User URL: ",user.url)
except Exception as e: # if the user Id is not valid 
	print(e)
