
class Student:

    # [assignment from Zuri/I4G Fullstack Scholarship Training]
   
   def __init__(self, name, age, tracks, score):
      self.name = name
      self.age = age
      self.tracks = ["FE","BE"]
      self.score = float(score)
            
   def change_name(self, name):
      self.name = name
      return name

   def change_age(self, age):
      self.age = age
      return int(age)

   def add_track(self, track):
      self.tracks.append("track")
      return self.tracks

   def set_score(self, score):
      self.score = score

   def get_score(self):
      return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())



