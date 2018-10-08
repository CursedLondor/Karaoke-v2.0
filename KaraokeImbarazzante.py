import random
import json

with open('./Canzoni.json') as songs:
    songs = json.load(songs)
    
with open('./Invitati.json') as singers:
    singers = json.load(singers)

while True:
    randomsong = random.randint(0,len(songs)-1)
    numberofsingers = int(songs[randomsong]["numberofsingers"])
    if(numberofsingers==2 and songs[randomsong]["sex"]=="MF"):
        boolean = True
        while boolean:
            theyhavetosing = random.sample(singers, numberofsingers)
            if((theyhavetosing[0]["sex"] == "M" and theyhavetosing[1]["sex"] == "F") or (theyhavetosing[0]["sex"] == "F" and theyhavetosing[1]["sex"] == "M")):
                boolean = False
    else :
        theyhavetosing = random.sample(singers, numberofsingers)
    print("Autore: " + songs[randomsong]["author"] + "\tCanzone: " + songs[randomsong]["name"] + "\n")
    print("Cantanti:")
    for number in range(0, numberofsingers):
        print (theyhavetosing[number]["name"])
    print("\n\n\n")
    raw_input()