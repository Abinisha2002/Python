# mulitiple inheritance
class one():
    def name(self):
        print("am abhi")
class two(one):
    def age(self):
        print("am 23")
class three(two):
    def name3(self):
        print("from myd")
final=three()
final.name()
final.age()
final.name3()
# hierarchical
class parent():
    def name(self):
        print("father name.krish")
class child1(parent):
    def childname(self):
        print("child1 name is arsha")
class child2(parent):
    def child2name(self):
        print("child2 name is arshi")
obj=child1()
obj2=child2()
obj.name()
obj.childname()
obj2.child2name()
    