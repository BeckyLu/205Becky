import twitter, datetime


user = 1898676804


file = open("TwitterCredentials.txt")
cred = file.readline().strip().split(',')


api = twitter.Api(

consumer_key=cred[1],
consumer_secret=cred[2],
access_token_key=cred[3],
access_token_secret=cred[4])


statuses = api.GetUserTimeline(user)

timestamp = datetime.datetime.utcnow

response = api.PostUpdate("This is being Tweeted from a python sketch. Tweeted at " + str(timestamp))

print("Status updated to: " + response.text)

print (statuses[0].text)
