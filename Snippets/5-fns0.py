def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats

repeat_stuff("Row ", 3)

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "

song = repeat_stuff(lyrics, 2)
print(song)