# class Movie:
#     #Using Parameterized Constructor
#     def __init__(self,title,director,rating):
#         self.title = title
#         self.director = director
#         self.rating = rating
#     def display(self):
#         print(f"title is: {self.title}\n director is: {self.director}\n rating is : {self.rating}")

# m1 = Movie("EndGame","Anthony Russo",5)
# m1.display()


##Using Default Constructor
class Movie:
    def __init__(self):
        print('This is default Constructor')
    def display(self,title,director,rating):
        print(f"title: {title}, director: {director}, rating: {rating}")

m1 = Movie()
m1.display("EndGame","Anthony Russo",5)