genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results)
print(survey_genres)
for word in survey_genres:
    survey_abbreviated = {word[:3] for word in survey_genres}
print(survey_abbreviated)
names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'William', 'Sophia', 'Ethan', 'Isabella', 'Mason']
names_repated = names *10
names_with_E ={names for names in names_repated if names[0] == 'E'}
print(names_with_E)
set_names = set(names_repated)
print(set_names)
for name in set_names:
    nick_names = {name[0:3] for name in set_names if len(name)>=3}
print(nick_names)

print('      ')
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'
tag_list = [user_tag_1, user_tag_2, user_tag_3]
# Write your code below!
tag_set = set(song_data['Retro Words'])
tag_set.update(tag_list)
song_data['Retro Words'] = tag_set
print(song_data)
print('    ')

def sub_generator():
    yield 1
    yield 2
    yield 3

def main_generator():
    yield 'a'
    yield from sub_generator()
    yield 'b'

for item in main_generator():
    print(item)
