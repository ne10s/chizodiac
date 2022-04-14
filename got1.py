#!/usr/bin/env python3
"""Converting API JSON to Pandas Dataframe and to Excel """

import requests
import pandas as pd
import pyexcel

def main():
    """data conversion from GOT API"""

    # use requests to fetch JSON and convert to Python dictionary
    url= "https://anapioficeandfire.com/api/characters?page=4&pageSize=20"
    r= requests.get(url).json()

    # using json_normalize() to create a flat table
    df = pd.json_normalize(r)
   
   # pop/remove url column 
    df.pop('url')
   
    #converting df to excel & give a sheet name
    df.to_excel('/home/student/static/TEST.xlsx',sheet_name='Session1') 

    # print off the top 20 lines of the dataframe
    print(df.head(20))

if __name__ == "__main__":
    main()
