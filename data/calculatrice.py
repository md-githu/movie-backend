# %%
class Calculator:
    def __init__(self, a, b):
        if not all(isinstance(x, (int, float)) for x in (a, b)):
            raise TypeError("Les deux arguments doivent être des entiers ou des flottants.")
        self.a = a
        self.b = b
 
    def add(self):
        return self.a + self.b
 
    def multiply(self):
        return self.a * self.b
 
calc = Calculator(3, 5)
print(calc.add())
print(calc.multiply())