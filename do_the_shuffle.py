#!/usr/bin/python3
# CCC08J2 - Do the Shuffle
playlist = 'ABCDE'
button = 0
while button != 4:
    button = int(input())
    press = int(input())
    for i in range(press):
        if button == 1:
            playlist = playlist[1:] + playlist[0]
        elif button == 2:
            playlist = playlist[-1] + playlist[0:-1]
        elif button == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:]
output = '' 
for song in playlist:
    output += song + ' '
print(output[:-1])
