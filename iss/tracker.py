#!/usr/bin/env python3
import requests

URL = "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    
    for response in resp["iss_position"]:
        print(response.get("latitude"))

if __name__== "__main__":
    main()
