# class is an user defined data type
# A 'Blue print' Andrei says

# cats everywhere exercise

class Cat:  # creating a class
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    # ignore this part for now. from this
    @classmethod
    def creating_another_object(cls, num1, num2):
        return cls('Anu', num1+num2)
    # to this


cat1 = Cat('Boosan', 4)  # instatiating an object
cat2 = Cat('Feline', 6)
cat3 = Cat('Joy', 5)

cats = [cat1.age, cat2.age, cat3.age]

def oldest_cat(cats):
    oldest = max(cats)
    print(f"The oldest cat is {oldest} yeras old")


oldest_cat(cats)
print('-'*8, 'ignore this', '-'*8)
new_cat = Cat.creating_another_object(1, 3)
print(new_cat.name, new_cat.age)
print('-'*29)


# CLASS METHODS --> decorator

# remember the inbuilt operations (or inbuilt functions) in a data types?
# int type  --> sum(), add() etc.
# list type --> append(), remove(), etc.
# dict type -->  dict['key'] = 'value'
# class is an user defined data type
# @classmethods are used to create methods on that data type

class PlayerCharachter:
    def __init__(self):
        self.name = input("Enter the name of Charachter:")
        self.age = int(input("Enter the age:"))

    @classmethod
    def is_eligible(cls, age):
        if age >= 18:
            return('eligible')
        else:
            return('not eligible')


player1 = PlayerCharachter()
print(player1.is_eligible(player1.age))

print('\b we can also create an object using @class methods\b\n try nad understand the ignored part')

# STATIC METHODS --> @classmethods have access over class but Qstaticmethods don't

# INHERITANCE by Ravi (NOT ZTM COURSE)


class Dog:
    def bark(self):
        print('Dog Barks')


class Cat:  # creating a class
    def meow(self):
        print('Cat meows')


class Child(Dog, Cat):
    def speak(self):
        print('Child Speaks')


class Man(Child):
    def Result(self):
        print('The man has grown')


pomeranian = Dog()  # instanciating
Boosan = Cat()
Kutty = Child()
Abi = Man()

Boosan.meow()
Kutty.meow()
Abi.Result()
pomeranian.bark()

#polymorphism

