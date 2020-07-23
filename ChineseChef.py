#inherit functions of another class
# : is necessary for class
from chef import chef
class ChineseChef(chef): #() when importing
    def make_chicken(self):
        print("the chef makes a orange chicken")

        # from...import...   class class_name(impoted_class_name):