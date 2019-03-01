import requests
import json
Url="http://saral.navgurukul.org/api/courses"
get_data=requests.get(Url)#here we are getting data
resp=get_data.json()#changing in json
data=json.dumps(resp)#dictnory to string
file =open("courses.json","w")#open file and writing in that
file.write(data)#writing data 
file.close()#closing the file
print (resp)