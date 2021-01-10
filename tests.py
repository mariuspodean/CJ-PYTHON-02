class Duck:
    def fly(self):
        print("Duck is flying")


class Stork:
    def fly(self):
        print("Stork is flying")


class Dog:
    def run(self):
        print("Dog is running")


instances = [Duck(), Stork(), Dog()]
for animal in instances:
    animal.fly()

    id(Dog)