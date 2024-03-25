"""
                UTS
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative
Soal 3:
Write a Python class that calculates and stores the height and weight of a person in metric.
The BMI is calculated using this formula:
Weight/Height^2
Weight is in pound and height is in feet.
The class should have two properties named: Weight and Height
The class should have two methods:
• BMI-Value This takes no arguments and returns a decimal value of the BMI;
Equals - This should override the equals method from the object class to compare the weight and height of two BMI objects. To override the equal method you should implement this method: eq (self, other) and return a boolean.
"""

class BMI:
    def __init__(self, weight_kg, height_m):
        self.weight_kg = weight_kg
        self.height_m = height_m

    def bmi_value(self):
        return self.weight_kg / (self.height_m ** 2)

    def __eq__(self, other):
        return isinstance(other, BMI) and self.weight_kg == other.weight_kg and self.height_m == other.height_m

person1 = BMI(50, 1.70) 
person2 = BMI(40, 1.68)  

print("BMI person1:", person1.bmi_value())
print("BMI person2:", person2.bmi_value())
print("Apakah person1 dan person2 sama?", person1 == person2)
