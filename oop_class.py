""" <=== 1 ===> """

# class Car:
#     brand = "BMW"
#     color = "black"
#
#
# car1 = Car()
# car1.brand = "Mercedes"
# car2 = Car()
#
# print(car1.brand)
# print(car2.brand)

""" <=== 2 ===> """

# class Person:
#     def __init__(self, name, age, experience):
#         self.name = name
#         self.age = age
#         self.experience = experience
#     # def person_info(self):
#     #      return f"Name: {self.name}, Age: {self.age}, Experience: {self.experience}"
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, Experience: {self.experience}"
#
# obj1 = Person("Azizbek", 16, 4)
# obj2 = Person("Shaman", 13, 3)
# obj3 = Person("Mirsodick", 14, 2)
#
#
# print(obj1)
# print(obj2)
# print(obj3)

""" <=== 3 ===> """

# class Movie:
#     def __init__(self, title, genre, caption):
#         self.title = title
#         self.genre = genre
#         self.caption = caption
#
#     def movie_info(self):
#         return f" Title: {self.title}\n Genre: {self.genre}\n Caption: {self.caption}\n"
#
#
# film1 = Movie("Dune: Part Two", "Action",
#               "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who "
#               "destroyed his family.")
# film2 = Movie("A Quiet Place: Day One", "Horror", "Experience the day the world went quiet.")
# film3 = Movie("Furiosa: A Mad Max Saga", "Adventure",
#               "The origin story of renegade warrior Furiosa before her encounter and team up with Mad Max.")
#
# print(film1.movie_info())
# print(film2.movie_info())
# print(film3.movie_info())

""" <=== 4 ===> """

# class Person:
#   def __init__(self, name, gender):
#     self.name = name
#     self.gender = gender
#     self.country = "USA"
#
# person_1 = Person("Bob", "Male")
# person_2 = Person("Kate", "Female")
#
# print(f"{person_1.name}, {person_1.gender}, {person_1.country}")

""" <=== 5 ===> """


# class Ota:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name}, {self.age}"
#
#
# class Bola(Ota):
#     pass
#
#
# obj1 = Bola("Azizbek", 16)
# print(obj1)


class Bot:
    def __init__(self, gender: str, skin: str, color: str, is_active: bool, is_weapon: bool, drive: bool,
                 is_smoking: bool, is_police: bool, location: str):
        self.gender = gender
        self.skin = skin
        self.color = color
        self.is_active = is_active
        self.is_weapon = is_weapon
        self.drive = drive
        self.is_smoking = is_smoking
        self.is_police = is_police
        self.location = location

    def info(self):
        return f"Gender: {self.gender}\nSkin: {self.skin}\nColor: {self.color}\nIs Active: {self.is_active}\nIs Weapon: {self.is_weapon}\nDrive: {self.drive}, Smoke: {self.is_smoking}, Location: {self.location}"

    def is_running(self):
        if self.is_active:
            return True
        else:
            return False

    def attack(self):
        if self.is_weapon:
            return True
        else:
            return False

    def police(self):
        if self.is_police:
            return True
        else:
            return False

    def smoke(self):
        if self.is_smoking:
            return True
        else:
            return False

    def position(self):
        if self.location == 1:
            return "village"
        elif self.location == 2:
            return "city"
        elif self.location == 3:
            return "oversea"


bot1 = Bot('Male', 'Jeans', 'black', True, False, False, True, False, "city")
bot2 = Bot('Female', 'T-shirt', 'white', False, False, True, False, False, 1)
bot3 = Bot('Male', 'short', 'brown', True, True, False, True, True, 3)

print("|Bot1| Running:", bot3.is_running())
print("|Bot2| Attacking:", bot1.attack())
print("|Bot3| Smoking:", bot2.smoke(), ",", bot2.position())

