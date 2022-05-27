'''
class Person:
   "This is the first class created"
   age = 10

   def greetings(self):
      print("Hello guys")

Ajibade = Person()

print(Person.age)
print(Person.__doc__)
Ajibade.greetings()

'''


# Example 2
'''
class ComplexNumber:
   def __init__(self, a=0, b=0):
      self.one = a
      self.two = b
   def get_data(self):
      print("These are the numbers: ", self.one, ", ", self.two)

num1 = ComplexNumber(5, 7)
num1.get_data()

num2 = ComplexNumber(10, 15)
num2.three = 26

print((num2.one, num2.two, num2.three))
'''


# Example 3: Inheritance
'''
class Polygon:
   def __init__(self, sides):
      self.n sides
      self.sides = [0 for i in range(sides)]

   def input_sides(self):
      self.sides = [float(input("Enter number of sides " + str(i + 1)+" : ")) for i in range(self.n)]

   def display_sides(self):
      for i in range(self.n):
         print("Sides", i+1, "is", self.sides[i])
'''


class Animal:
   def __init__(self, grain, millet, leg):
      self.e = grain
      self.c = millet

   def food(self):
      print("Sometimes, I eat ", self.e, "and ", self.c)

   def get_play(self):
      print("I play with my kids always.")

   def get_leg(self):
      num_leg = self.leg
      return num_leg

   def set_name(self, name):
      self.name = name

   def get_name(self):
      return self.name

class Cat(Animal):
   def sound(self):
      print("I mew always")

suru = Cat("rice", "beans", 4)
suru.food()
suru.get_play()
suru.sound()

class Goat(Animal):
   def __init__(self, grain, millet, leg):
      super().__init__(grain, millet, leg)

   def supply_water(self):
      print("I pass water through my stomach")


gbebe = Goat("Eeri", "Agbado", 8)
gbebe.food()
gbebe.supply_water()
gbebe.get_play()


gbebe.set_name('aderogba')
print(gbebe.get_name())
gbebe.get_leg()

# Example 5

class Calculator:
   def __init__(self, x, z):
      self.first = x
      self.second = z

   def display_add(self):
      print("First number is: ", self.first)
      print("Second number is: ", self.second)
      print("The total is: ", self.first + self.second)
      # return result

student_score = Calculator(75, 25)
student_score.display_add()