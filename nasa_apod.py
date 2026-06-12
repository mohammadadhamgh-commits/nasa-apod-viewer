import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv('NASA_API_KEY')

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
response= requests.get(url)

print('Status', response.status_code)
print('API key loaded:', API_KEY is not None)

if response.status_code !=200:
    print('Error:',response.text)
    exit()

data=response.json()

print('NASA APOD')
print('Title:', data['title'])
print('Explanation:', data['explanation'])
print('Date:', data['date'])
print('\nImage will open in...')

for i in range(5,0,-1):
    print(i)
    time.sleep(1)

print('Opening Image:')

print('Image URL:', data['url'])