import random
import json

#Open JSON files
with open('./Canzoni.json') as songs:
    songs = json.load(songs)
    
with open('./Invitati.json') as singers:
    singers = json.load(singers)

#Loop
while True:

    #Select random song and singer/singers
    randomsong = random.randint(0,len(songs)-1)
    numberofsingers = int(songs[randomsong]["numberofsingers"])

    #If the song is performed by a duet
    if numberofsingers==2 and songs[randomsong]["sex"]=="MF" :
        boolean = True
        x = 1

        #Continue until two singers of different sex are selected, abort after 30 tryes
        while boolean:

            #Insufficient number of singers
            if len(singers) < numberofsingers :
                print("Non ci sono abbastanza cantanti!")
                exit(0)
            
            #Choose singers
            theyhavetosing = random.sample(singers, numberofsingers)

            #Verify the sex
            if (theyhavetosing[0]["sex"] == "M" and theyhavetosing[1]["sex"] == "F") or (theyhavetosing[0]["sex"] == "F" and theyhavetosing[1]["sex"] == "M") :
                boolean = False

            #After 30 tryes, abort
            x = x+1
            if x == 30 :
                print("Non trovo cantanti per un duetto!")
                exit(0)

    #If is not performed by a duet, select the number of singers required
    else :
        theyhavetosing = random.sample(singers, numberofsingers)

    #Print singer/singers and song
    print("Autore: " + songs[randomsong]["author"] + "\tCanzone: " + songs[randomsong]["name"] + "\n")
    print("Cantanti:")
    for number in range(0, numberofsingers):
        print (theyhavetosing[number]["name"])
    print("\n\n\n")

    #Remove song and singer/singers
    songs.pop(randomsong)
    for num in range(0, len(theyhavetosing)):
        singers.pop(singers.index(theyhavetosing[num]))

    #Write remaining singer/singers and song (in case of problem in the program)
    with open('CanzoniRestanti.json', 'w') as remainingsongs:
        json.dump(songs, remainingsongs)
    with open('InvitatiRestanti.json', 'w') as remainingsingers:
        json.dump(singers, remainingsingers)

    #Verify if songs and singers are not empty
    if len(songs) == 0 :
        print("Le canzoni sono finite!")
        exit(0)
    if len(singers) == 0 :
        print("I cantanti sono finiti!")
        exit(0)
        
    raw_input()