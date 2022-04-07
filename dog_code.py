#!/usr/bin/env python3

import random

def apigrabber():
    status_codes= [200, 302, 307, 401, 403, 404, 418, 502]
    x= random.choice(status_codes)
    return x

def main():
# all of your code will be written in the main function
    x= apigrabber()
    if x > 200 and x <300: 
        print(f"{x} OK!")
        print("OK!")
    elif x >= 300 and x <400:
        print(x)
        print("Redirecting!")
    elif x >= 400 and x <500:
        print(x)
        print("You done screwed up, son!")
    elif x >=500 and x <600:
        print(x)
        print("We done screwed up, son!")
main()
