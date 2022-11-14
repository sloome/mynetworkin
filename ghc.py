import os
import requests
os.system ("clear")
print ("type link *before the (www.)type the http://&https://:")
url = input ()
req = requests.get(url).text
print (url)
print(req)

