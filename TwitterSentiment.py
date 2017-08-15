import tweepy
import csv

####input your credentials here
consumer_key = 'nVDmr3VPouFNbkfjwueMLM0h2'
consumer_secret = 'qM0i6m1qekPWIxIax2NLmdV8h9YbpKzCeaxOg4D4mePnf0sIku'
access_token = '743458442933764096-uKATZfEjJ1jpITtqoGAcgnc6mIpQHLR'
access_token_secret = 'Sd70yJoimaLYcF95yd54DK6NvlokqUEPLLY0PR9KevGia'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])