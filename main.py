import json
import random
import re
import sys

args = sys.argv[1:]

# Open JSON files to import songs and users
with open('songs/songs.json') as songs:
    songs = json.load(songs)
    #print('\n'.join([str(lst["name"]) for lst in songs]))

with open('users/users.json') as singers:
    singers = json.load(singers)
    male_singers = [x for x in singers if x["sex"] == "M"]
    female_singers = [x for x in singers if x["sex"] == "F"]

counter_drop = int(args[0])
print("\n\n\n")

# Loop
while len(male_singers) + len(female_singers) > 0 and len(songs) > 0 and counter_drop != 0:

    random.shuffle(songs)
    random.shuffle(male_singers)
    random.shuffle(female_singers)

    # Select random song and count the number of singer/singers
    random_song = random.randint(0, len(songs)-1)
    male_occurrence = len(re.findall("M", songs[random_song]["sex"]))
    female_occurrence = len(re.findall("F", songs[random_song]["sex"]))
    number_of_singers = male_occurrence + female_occurrence

    # Verify the number of singers
    if male_occurrence <= len(male_singers) and female_occurrence <= len(female_singers):

        male_chosen = random.sample(male_singers, male_occurrence)
        female_chosen = random.sample(female_singers, female_occurrence)
        all_chosen = male_chosen + female_chosen

        print("Autore: " + songs[random_song]["author"] + "\t\tCanzone: " + songs[random_song]["name"] + "\n")
        print("Cantanti:", '\n'.join([str(lst["name"]) for lst in all_chosen]), sep='\n')
        print("\n\n\n")

        male_singers = [x for x in male_singers if x not in male_chosen]
        female_singers = [x for x in female_singers if x not in female_chosen]

    else:
        counter_drop -= 1

    songs.pop(random_song)

    # Create a backup in case of fail
    with open('songs/backupSongs.json', 'w') as remaining_songs:
        json.dump(songs, remaining_songs)
    with open('users/backupUsers.json', 'w') as remaining_singers:
        json.dump(male_singers + female_singers, remaining_singers)

    input()

print("Il Karaoke si conclude qui!")
exit(0)