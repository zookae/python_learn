class Song(object):

    # self used to reference variables of the instance
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "so I'll stop right there"])

bulls_on_parade = Song(["they rally around the family", "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
