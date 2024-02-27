"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
import urllib.request

def make_request(url):
    response=urllib.request.urlopen(url)
    status_code=response.getcode()
    data=response.read().decode('utf-8')
    return status_code,data
status_code,data=make_request('https://www.google.com')
if status_code:
    print("Status Code :"+str(status_code))
    print("Response :"+data[:200])
else:
    print("Error :"+data)    