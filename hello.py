class Parent:
    def hello(self):
        print("Hello from Parent")

class Child(Parent):
    def hello(self):
        print("Hello from Child")

class GrandChild(Child):
    def hello(self):
        print("Hello from GrandChild")
        print("---------- call Child.hello() ---------")
        super(GrandChild, self).hello()
        print("---------- call Parent.hello() ---------")
        super(Child, self).hello()

grand_child = GrandChild()
grand_child.hello()
