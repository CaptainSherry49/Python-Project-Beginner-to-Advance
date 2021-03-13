"""
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)


# ------------- Status Code -----------------#
Status codes are issued by a server in response to a client's request made to the server. ... All HTTP response status
codes are separated into five classes or categories. The first digit of the status code defines the class of response,
while the last two digits do not have any classifying or categorization role.


print(x.status_code)

"""

