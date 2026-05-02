
class Movie():
    def __init__(self,name,genre,rating,watched):
        self.name=name
        self.genre=genre
        self.rating=rating
        self.watched=watched
        
    def get_info(self):
        return f"name:{self.name}\ngenre:{self.genre}\nrating:{self.rating}\nwatched:{self.watched}"
    
    
class MovieManager():
    def __init__(self):
        self.movies=[]
        
    def add_movie(self,movie):
        self.movies.append(movie)
        
    def mark_watched(self,name):
        # if self.Watched==True:
        #    self.watched.append(name)
        for movie in self.movies:
          if movie.name == name:
            movie.watched = True
               
    def show_all(self):
        for movie in self.movies:
            print(movie.get_info())
            
    def show_unwatched_movies(self):
        # if self.watched=="Avatar":
        #     print(self.movies)\
            for movie in self.movies:
             if not movie.watched:
               print(movie.get_info())
            
    def avg(self):
    #   print((sum(Movie.rating for rating in self.movies))/len(self.movies))
        sum(m.rating for m in self.movies)
        
m1=Movie("Avatar","Sci-Fi",8.0,True)
m2=Movie("Martian","Adventure",8.5,False)
m3=Movie("Interstellar","Sci-Fi",10.0,True)
m4=Movie("Moon","Love",9.0,False)

m=MovieManager()
m.add_movie(m1)
m.add_movie(m2)
m.add_movie(m3)
m.add_movie(m4)

m.mark_watched("Avatar")
m.show_all()
m.show_unwatched_movies()
m.avg()
