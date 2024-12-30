class person:
    def __init__(self,name) :
        self.neme=name

    def PrintName(self):
        print("Hello "+self.neme)

p=person("world")
p.PrintName()
    