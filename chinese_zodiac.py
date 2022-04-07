#!/usr/bin/env python3
#Game that will output user chinese zodiac sign
#Characterstics & food if time permits.

zodiacs = {
 "Rat":
        {"personality" : " artistic, sociable, industrious, charming, and intelligent"},

 "Ox":
        {"personality" : " strong, thorough, determined, loyal, and reliable"},
        
 "Tiger":
        {"personality" : " courageous, enthusiastic, confident, charismatic, and a leader"},

 "Rabbit":
        {"personality" : " vigilant, witty, quick-minded, and ingenious"},
 
 "Dragon":
        {"personality" : " talented, powerful, lucky, and successfull"},
 
 "Snake":
        {"personality" : " wise, like to work alone, and determined"},

 "Horse":
        {"personality" : " animated, active, and energetic"},
 
 "Sheep":
        {"personality" : " creative, resilient, gentle, mild-mannered, and shy"},

 "Monkey":
        {"personality" : " sharp, smart, curious, and mischievious"},

 "Rooster":
        {"personality" : " hardworking, resourceful, courageous, and talented"},

 "Dog":
        {"personality" : " loyal, honest, cautious, and kind"},

 "Pig":
        {"personality" : "a symbol of wealth, honesty, and practicality"},
          }


def main():    
    usr_name = input("Please, enter your name->") 
              
    usr_name = usr_name.title()    
    usr_date = int(input("Please, enter your birth year in YYYY format, e.g 2010->"))
        
    if usr_date in [2011, 1999, 1987, 1975, 1963]:
        print(f"{usr_name} your zodiac sign is Rabbit, You are {zodiacs['Rabbit'].get('personality')}")
    elif usr_date in [2020, 2008, 1996, 1984, 1972, 1960]:
        print(f"{usr_name} your zodiac sign is Rat, You are {zodiacs['Rat'].get('personality')}")
    elif usr_date in [2010, 1998, 1986, 1974, 1962]:
        print(f"{usr_name} your zodiac sign is Tiger, You are {zodiacs['Tiger'].get('personality')}")
    elif usr_date in [2021, 2009, 1997, 1985, 1973, 1961]:
        print(f"{user_name} your zodiac sign is Ox, You are {zodiacs['Ox'].get('personality')}")
    elif usr_data in [2012, 2000, 1988, 1976, 1964]:    
        print(f"{usr_name} your zodiac sign is Dragon, You are {zodiacs['Dragon'].get('personality')}")
    elif usr_date in [2013, 2001, 1989, 1977, 1965]:
 	print(f"{usr_name} your zodiac sign is Snake, You are {zodiacs['Snake'].get('personality')}")
    elif usr_date in [2014, 2002, 1990, 1978, 1966]:
 	print(f"{usr_name} your zodiac sign is Horse, You are {zodiacs['Horse'].get('personality')}")
    elif usr_date in [2015, 2003, 1991, 1979, 1967]:
      	print(f"{usr_name} your zodiac sign is Sheep, You are {zodiacs['Sheep'].get('personality')}")
    elif usr_date in [2016, 2004, 1992, 1980, 1968]:
 	print(f"{usr_name} your zodiac sign is Monkey, You are {zodiacs['Monkey'].get('personality')}")
    elif usr_date in [2017, 2005, 1993, 1981, 1969]:
 	print(f"{usr_name} your zodiac sign is Rooster, You are {zodiacs['Rooster'].get('personality')}")
    elif usr_date in [2018, 2006, 1994, 1982, 1970]:
 	print(f"{usr_name} your zodiac sign is Dog, You are {zodiacs['Dog'].get('personality')}")
    elif usr_date in [2019, 2007, 1995, 1983, 1971]:
 	print(f"{usr_name} your zodiac sign is Pig, You are {zodiacs['Pig'].get('personality')}")


main()
