song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users["Retro Words"])
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')
song_data_users = {'Retro Words': tag_set}
print(song_data_users)


allowed_tags = ['pop', 'hip-hop', 
'rap', 'dance', 'electronic', 
'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 
'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}
tag_set = set(song_data_users['Retro Words'])
bad_tags = []
for tag in tag_set:
    if tag not in allowed_tags:
        bad_tags.append(tag)
for tags in bad_tags:
    tag_set.remove(tags)
print(tag_set)



#Union set

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
new_song_data = {}

for key,value in song_data.items():
    song_data_set = set(value)
    user_tag_data_set =set(user_tag_data[key])
    intersections = song_data_set & user_tag_data_set
    print(intersections)
    new_song_data[key] = song_data_set | user_tag_data_set
print(new_song_data)
print('       ')
#Intersection set 
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
song_data_set_1 = set(song_data['Retro Words'])
user_recent_songs_set= set(user_recent_songs['Lowkey Space'])
tags_int = song_data_set_1 & user_recent_songs_set
print(tags_int)

recommended_songs = {}
nl = []
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = tag
            

   
#Different set
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

song_data_set_03 = set(song_data)
song_data_set_diff_disliked = set(song_data['Retro Words'])
user_liked_song_set = set(user_liked_song['Back To Art'])
user_disliked_song_set = set(user_disliked_song['Retro Words'])
tag_diff =user_liked_song_set - user_disliked_song_set
count = 0
recommended_song_1 = {}
nl = []
for key,value in song_data.items():
    for song in value:
        for tag in value:
            if tag in tag_diff:
                if key not in user_disliked_song and key not in user_liked_song:
                    recommended_song_1[key] = tag
print(recommended_song_1)
    
    
    
    user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}
                     

for key, value in user_song_history.items():
    new_set = set(user_song_history[key])


    
    user_tags = set(new_set)
print(user_tags)
