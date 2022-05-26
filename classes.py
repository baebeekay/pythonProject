class Student:


    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name
        return self.name

    def change_age(self, age):
        self.age = age
        return self.age

    def add_track(self, track):
        self.track = track
        return self.track

    def get_score(self, score):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score(1))
