
import os
from random import randint
diru = 'C:\\Windows\\System32'

list_of_dir = os.listdir(diru)
# print(list_of_dir)
print(list_of_dir.index('cmd.exe'))
a = list_of_dir.index('cmd.exe')

# print(Counter(list_of_dir))
# print(''.join(list_of_dir))
# os.startfile(list_of_dir.join(a))

yu = ['dfk', 'dfkdj', 'dkjfkdsjkska']
b = yu.index('dfk')

print(b)
print(a)
print(os.startfile(os.path.join(diru, list_of_dir[a])))
dfj = os.path.join(diru, list_of_dir[a])
print(dfj)


music_dir = 'D:\\cp77music'
songs = os.listdir(music_dir)
songs_no = randint(0,len(music_dir))
print(songs_no)
song_name = songs[songs_no]

print((os.path.join(music_dir, songs[songs_no])))