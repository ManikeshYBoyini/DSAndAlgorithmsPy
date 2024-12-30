import Monk

def monkey_f(self):
    print("monkey function is being called")


Monk.Monk.MemberFunction=monkey_f
obj=Monk.Monk()

obj.MemberFunction()