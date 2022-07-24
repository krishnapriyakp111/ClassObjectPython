class Mammal:
    def walk(self):
        print('walk')


class Domestic:
    def fond(self):
        print('fond')


class Dog(Mammal, Domestic):
    def bark(self):
        print('bark')


Dog1=Dog()
Dog1.bark()
Dog1.fond()

