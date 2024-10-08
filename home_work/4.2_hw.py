class Math:
 def __init__(self, a, b):
  self.a = a
  self.b = b

 def addition(self):
  result = self.a + self.b
  print(f"Addition: {self.a} + {self.b} = {result}")

 def multiplication(self):
  result = self.a * self.b
  print(f"Multiplication: {self.a} * {self.b} = {result}")

 def division(self):
  if self.b != 0:
   result = self.a / self.b
   print(f"Division: {self.a} / {self.b} = {result}")
  else:
   print("Cannot divide by zero.")

 def subtraction(self):
  result = self.a - self.b
  print(f"Subtraction: {self.a} - {self.b} = {result}")


math_operations = Math(a =10, b = 5)
math_operations.addition()
math_operations.multiplication()
math_operations.division()
math_operations.subtraction()