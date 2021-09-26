class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Hello {}! How are you?".format(self.name))
        
    def setNewAge(self, value):
        self.age = value
        
    def minusAge(self):
        self.age = self.age - 2
 
	
#reverse array
    def print5to1(self):
        arr = []
        # range(start, stop, step)
        for i in range(5,0,-1):
            arr.append(i)
        print(arr)
        
p1 = Person("john", 12)

p1.greet()

p1.setNewAge(17)
p1.minusAge()

print(p1.age)

p1.print1to10()