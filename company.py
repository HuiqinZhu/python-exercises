#information below things like "def" "if" "else" should be blocked strictly
#functions of attributes should be below the class definition?
class company:
    def __init__(self, type, place, position, salary, is_good):
        self.type = type
        self.place = place
        self.position = position
        self.salary = salary
        self.is_good = is_good
        #class class_name:                    self,    _init_
        #     def _init_(self, , , , ):
         #       self. =
         #       self. =
        # to define a new class and its attributes. Original attribute value in the left and public attribute value in the right
    def is_good_salary(self):
        if self.salary >= 250000:
           return True
        else:
           return False

def pow(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    print(result)
# attributes of object in the left(use self.attribute), attributes of class in the right