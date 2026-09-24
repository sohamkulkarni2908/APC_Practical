class Media:
    def play(self):
        print("Playing media")

class Audio(Media):
    def play(self):
        print("Playing Audio")

class Video(Media):
    def play(self):
        print("Playing Video")

class Podcast(Media):
    def play(self):
        print("Playing Podcast")

media = [Audio(), Video(), Podcast()]
for item in media:
    item.play()