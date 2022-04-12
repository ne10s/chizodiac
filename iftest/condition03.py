#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

# this is an indentation error
# your print below needs to either be all the way to the left,
# or in line with the prints up above
# if you want the print below to run no matter what (even if the IF is false)
# then push it to the left
# and then it'll work :)
    print("Exiting the script")
