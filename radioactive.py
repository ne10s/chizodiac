#!/usr/bin/python3
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

a= challenge[2][1]
b= challenge[2][0]
c= challenge[3]
print(f'my{a}! The{b} do {c}!')

    #      0           1    --------------------2---------------      3
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

a= trial[2]["eyes"]
b= trial[2]["goggles"]
c= trial[3]
print(f'my{b}! The{a} do{c}!')

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

eyes= nightmare[0]["user"]["name"]["first"]
gogs= nightmare[0]["kumquat"]
noth= nightmare[0]["d"]
print(f"My {eyes}! The {gogs} do {noth}!")

