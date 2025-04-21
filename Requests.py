import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


url = "https://www.facebook.com"
response = requests.get(url)
# it will show the HTTP status code
print(response)
print(response.status_code)


response = requests.get("https://www.facebook.com")
print(response.content)

#POST Request
data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"
response = requests.post(url, json=data)

response_data = response.json()
#Shows the data as a dictionary
print(response_data)

#Handling Errors
# here we use an endpoint that always gives a 404 status error
response = requests.get("https://httpbin.org/status/404")
# if status code is not 200 (successful response), then show error message
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")

#Setting a Timeout
url = "https://httpbin.org/delay/10"

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout as err:
    print(err)

#HTTP Request Headers
auth_token = "XXXXXXXX"

# here we set the authorization header with the 'bearer token' for authentication purposes.
headers = {
    "Authorization": f"Bearer {auth_token}"
}

url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())

#Web Scraping with BeautifulSoup
url = "https://www.facebook.com"
# this will get all the HTML, javascript, css code
response = requests.get(url)



url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print(title, content, links)

#Requests vs urllib


# Prepare data
data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")

# Add headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Create the request with headers
req = urllib.request.Request(
    "https://www.example.com",
    data=data,
    headers=headers,
    method="POST"
)

# Send the request
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
    print(html)
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")

