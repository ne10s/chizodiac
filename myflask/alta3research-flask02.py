#!/usr/bin/env python3
"""Requesting JSON"""
import requests
#from pprint import pprint

URL= "http://127.0.0.1:2224/login"

resp= requests.post(URL,json={"solution":"All and more!"}).json()
print(f"""
        {resp['name']} is everything and more""")
#pprint(resp)
