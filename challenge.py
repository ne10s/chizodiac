#!/usr/bin/env python3
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},
"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},
"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
def main():
    char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk) ")
    char_stat = input("  What statistic do you want to know about? (real name, powers, archenemy)")
    
    # .title() is the correct method for char_name, as it capitalizes the first word; but .title() doesn't permanently change the string its attached to
    #char_name.title() 

    # so you'd have to do this to save the change:
    char_name= char_name.title()

    # now for char_stat, we DON'T want that capitalized, because all those keys (real name, powers, archenemy) are LOWERCASE in the dictionary
    # so let's force it to be lowercase instead
    #char_stat.title() 

    char_stat= char_stat.lower()

    # this f string is ALMOST perfect-- what's annoying is that we need quotes around the whole string AND quotes around each key
    # this is confusing python because we keep using double quotes
    #print(f"{{marvelchars["char_name"]}'s {marvelchars["char_name"]["char_stat"]} is: {marvelchars["char_name"].get("char_stat"))

    # the solution is to use one type of quotes on the "outside" and the other type of quotes on the 'keys'
    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name].get(char_stat)}")

main()
