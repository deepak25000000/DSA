class Bike:

  gear = 0
  name = ""

#Object of the class Bike
suzuki = Bike()
#Accessing attributes of class Bike 
suzuki.name = 'Ghostrider'
suzuki.gear = 5

print(f"Name : {suzuki.name}, Gears : {suzuki.gear}")

class employee:
    emp_id = 0
    emp_role = ""
    emp_salary = 0

#Creating objects of the class employee
Deepak = employee()

Deepak.id = 75
Deepak.role = "AI DEVELOPER"
Deepak.salary = 10000
print(f"Employee ID: {Deepak.id}")
print(f"Employee Role: {Deepak.role}")
print(f"Employee Salary: {Deepak.salary}")


#Area Of circle
class Circle:
  radius = 0
  pi = 3.141

circle1 = Circle()
circle1.radius = 27
circle1.area = 0
print(f"Area of cricle : {circle1.pi * circle1.radius**circle1.radius}")

#using method
def Areaofcircle():
  return circle1.pi * circle1.radius**circle1.radius
print("Area Of circle", Areaofcircle())