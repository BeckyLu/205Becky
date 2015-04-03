import twitter, datetime, sqlite3
google = sqlite3.connect("C:\Users\Steve\AppData\Local\Google\Chrome\User Data\Default\History")
cursor = google.cursor()

cursor = google.cursor()
cursor.execute("SELECT * FROM urls")
rows = cursor.fetchall()
#data = " "
for line in rows :
    global data 
    data = line[1]
print data

user = 1898676804


file = open("TwitterCredentials.txt")
cred = file.readline().strip().split(',')


api = twitter.Api(

consumer_key="5HlfJs6N70i0N9y0z2nmy1MOV",
consumer_secret="KX2om4lFxKNTBm7Lsve9g3enLBjl57nCmGPqSD47ZWzn8TJsIf",
access_token_key="1898676804-1SFQSCITWTfI49crXNwP6vuUEoBIWZrcXuUNUar",
access_token_secret="g0FguJruvzD3hAmwd6yTdHe4xGFrJN5jTCX05EppXCpTf")

#print api.VerifyCredentials()

statuses = api.GetUserTimeline(user)

timestamp = datetime.datetime.utcnow()

response = api.PostUpdate("This is being Tweeted from a python sketch. Tweeted at " + str(timestamp))

lastWebsite = api.PostUpdate("The last website I Visited was: " + data)

print("Status updated to: " + response.text)

print("Status updated to: " + lastWebsite.text)

print (statuses[0].text)
