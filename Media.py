from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod    
    def get_info(self):
        pass


class Song(Media):
    def __init__(self, title, duration, artist):
        super().__init__(title, duration)
        self.artist = artist
        
    def get_info(self):
        return f'''Title:{self.title}
Artist:{self.artist}
Duration:{self.duration}'''
        
    def __str__(self):
        return self.get_info()
                   
    def __add__(self, other):
        return self.duration + other.duration


class Podcast(Media):
    def __init__(self, title, duration, host):
        super().__init__(title, duration)
        self.host = host
        
    def get_info(self):
        return f'''Title:{self.title}
Duration:{self.duration}
Host:{self.host}'''


class Playlist():
    def __init__(self):
        self.media_list = []
        
    def add_media(self, media):
        self.media_list.append(media)
        
    def show_all(self):
        for media in self.media_list:
            print(media.get_info())
            
    def total_duration(self):
        return sum(media.duration for media in self.media_list)
    
    def longest(self):
        return max(self.media_list, key=lambda d: d.duration)
    
    def shortest(self):
        return min(self.media_list, key=lambda d: d.duration)


s1 = Song("Arz kiya hai", 5, "Anuv jain")
s2 = Song("husn", 4, "Anuv")
s3 = Song("Barishein", 3, "Jain")

p1 = Podcast("king", 1, "Srk")
p2 = Podcast("Queen", 2, "Ma")
p3 = Podcast("Crown", 3, "Ameer")

playlist = Playlist()

playlist.add_media(s1)
playlist.add_media(s2)
playlist.add_media(s3)
playlist.add_media(p1)
playlist.add_media(p2)
playlist.add_media(p3)

playlist.show_all()

print("Total Duration:", playlist.total_duration())
print("Longest:", playlist.longest())
print("Shortest:", playlist.shortest())

