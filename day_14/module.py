import math
import os
import myModule
import requests
print(math.sqrt(16))
myModule.hello()
# two types of module - built in and external module
r=requests.get("https://www.google.com")
print(r.text)