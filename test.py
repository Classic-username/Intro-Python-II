
class Person():
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def isAdult(self):
        if self.age > 17:
            return True
        else:
            return False




class Mutation(Person):
    def __init__(self, name, age, powers):

        super().__init__(name, age)

        self.powers = powers
        

    