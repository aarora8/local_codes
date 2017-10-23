class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def sayhello(self):
        print ("hello my name is {} {}".format(self.name, self.surname))


A = Person('Ashish','arora')
B = int(9)
print B
A.sayhello()
print A.name
print A.surname

A.surname = 'aarora8'

print A.name
print A.surname
