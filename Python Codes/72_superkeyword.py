class ParentClass:
    def parent_method(self):
        print("This is the parent method 1")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method 2")
        super().parent_method()
    
child_object = ChildClass()
child_object.child_method()
child_object.parent_method()