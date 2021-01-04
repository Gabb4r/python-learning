"""

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def male(self):
        print(f"{self.name} you are male!")

    def female(self):
        print(f"{self.name}you are female!")

ramesh = Person("Ramesh", "5.6", "75")

shruti = Person("Shruti", "5.3", "65")


# Another Example :

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family","With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

"""

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_song(self):
        for lines in self.lyrics:
            print(lines)

sad_songs = Song(["Tum hi ho , kyuki tum hi ho ", "Me tenu samjavan ki me tere bin lgta ji", "Tu hi hai aasihqui"])

love_songs = Song(["Tere liye duniya chod di hai", "love me thoda"])

sad_songs.sing_song()