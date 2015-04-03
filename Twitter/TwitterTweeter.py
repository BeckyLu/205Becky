import twitter, datetime


user = 1898676804


file = open("TwitterCredentials.txt")
cred = file.readline().strip().split(',')


api = twitter.Api(

consumer_key="5HlfJs6N70i0N9y0z2nmy1MOV",
consumer_secret="KX2om4lFxKNTBm7Lsve9g3enLBjl57nCmGPqSD47ZWzn8TJsIf",
access_token_key="1898676804-sZlf8R5VmAourSLpPiCPqcich7Etp7Wz8K4XjUZ",
access_token_secret="hlI9YiDk5rSLHTToE1zt9wzj59S1PlhMpK8XuEL1l9lpX")

print api.VerifyCredentials()

statuses = api.GetUserTimeline(user)

timestamp = datetime.datetime.utcnow

response = api.PostUpdate("This is being Tweeted from a python sketch. Tweeted at " + str(timestamp))

print("Status updated to: " + response.text)

print (statuses[0].text)
