

def calculate(n,**kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2,add=3,multiply=5)


class Car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seat = kw.get('seat')

my_car = Car(make='Ford', model='Mustang', color='red', seat=4)
print(my_car.make)