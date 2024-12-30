movies= {
    'RRR':'11:00 A.M',
    'Saaho':'1:00 P.M',
    'Don':'3:00 P.M',
    'Speed':'8:00 P.m'
}

print('We are showing the following movies\n')
print(movies)

movie=input('Enter the movie you would like to watch\n')

showTime=movies.get(movie)
if showTime==None:
    print("Requested showtime isn't playing")
else:
    print(movie, ' is playing at ',showTime) 