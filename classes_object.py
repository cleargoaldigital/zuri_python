class FIRSTCLASS:
   def __init__(self, time, name, age):
      self.time = time
      self.name = name
      self.age = age

   def my_comment(self):
      print("The boy who came in the "+ self.time + " is "+ self.name + "." + " He is " + str(self.age))

person1 = FIRSTCLASS("evening", "Akanbi", 36)
person1.my_comment()
person1.name = "Ayeloyun"
person1.age = 43

person1.my_comment()

print(person1.name)
        
# Creating a child class that uses parent property.
# This is done by creating a new class
# passing the parent class as parameter.

class secondclass(FIRSTCLASS):
   pass

x = secondclass("morning", "Owolabi", 35)
x.my_comment()


# Super() function: makes the child inherits
# all the properties and methods from its parents

class thirdclass(FIRSTCLASS):
   def __init__(self, time, name, age):
      super().__init__(self, time, name, age)


# add properties to a class

class thirdclass(FIRSTCLASS):
   def __init__(self, time, name, age, year):
      super().__init__(self, time, name, age)
      self.graduationyear = year

y = thirdclass("afternoon", "Oriyomi", 25, 2019)
print(y.graduationyear)

# Add a method to the class

   def greetings(self):
      print("We welcome ", self.time, self.name, "aged ", self.age, "a member of ", self.graduationyear, " class.")

a = thirdclass("night", "Ajibade", 32, 2004)
a.greetings()