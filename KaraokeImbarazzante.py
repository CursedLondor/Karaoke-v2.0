import random
import json

with open('./Canzoni.json') as songs:
    songs = json.load(songs)
    
with open('./Invitati.json') as singers:
    singers = json.load(singers)

while True:
    randomsong = random.randint(0,len(songs)-1)
    numberofsingers = int(songs[randomsong]["numberofsingers"])
    if numberofsingers==2 and songs[randomsong]["sex"]=="MF" :
        boolean = True
        x = 1
        while boolean:
            if len(singers) < numberofsingers :
                print("Non ci sono abbastanza cantanti!")
                exit(0)
            theyhavetosing = random.sample(singers, numberofsingers)
            if (theyhavetosing[0]["sex"] == "M" and theyhavetosing[1]["sex"] == "F") or (theyhavetosing[0]["sex"] == "F" and theyhavetosing[1]["sex"] == "M") :
                boolean = False
            x = x+1
            if x == 30 :
                print("Non trovo cantanti per un duetto!")
                exit(0)
    else :
        theyhavetosing = random.sample(singers, numberofsingers)
    print("Autore: " + songs[randomsong]["author"] + "\tCanzone: " + songs[randomsong]["name"] + "\n")
    print("Cantanti:")
    for number in range(0, numberofsingers):
        print (theyhavetosing[number]["name"])
    print("\n\n\n")
    songs.pop(randomsong)
    for num in range(0, len(theyhavetosing)):
        singers.pop(singers.index(theyhavetosing[num]))
    with open('CanzoniRestanti.json', 'w') as remainingsongs:
        json.dump(songs, remainingsongs)
    with open('InvitatiRestanti.json', 'w') as remainingsingers:
        json.dump(singers, remainingsingers)
    if len(songs) == 0 :
        print("Le canzoni sono finite!")
        exit(0)
    if len(singers) == 0 :
        print("I cantanti sono finiti!")
        exit(0)
    raw_input()