# Define the base class Chair
class Chair:
    def __init__(self, chair_type, usage, material, color):
        self.chair_type = chair_type
        self.usage = usage
        self.material = material
        self.color = color

    def __str__(self):
        return f"{self.chair_type} chair used for {self.usage}, made of {self.material}, color {self.color}"

# first  child class OfficeChair 
class OfficeChair(Chair):
    def __init__(self, chair_type, usage, material, color, adjustable_height, has_wheels):
        super().__init__(chair_type, usage, material, color)
        self.adjustable_height = adjustable_height
        self.has_wheels = has_wheels

    def __str__(self):
        return super().__str__() + f", adjustable height: {self.adjustable_height}, has wheels: {self.has_wheels}"

# second child class DiningChair 
class DiningChair(Chair):
    def __init__(self, chair_type, usage, material, color, has_armrest, stackable):
        super().__init__(chair_type, usage, material, color)
        self.has_armrest = has_armrest
        self.stackable = stackable

    def __str__(self):
        return super().__str__() + f", has armrest: {self.has_armrest}, stackable: {self.stackable}"

# Example usage
office_chair = OfficeChair("Office", "working", "leather", "black", True, True)
dining_chair = DiningChair("Dining", "eating", "wood", "brown", False, True)

print(office_chair)
print(dining_chair)
