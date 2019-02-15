class Classy(object):
    items = []
    def __init__(self):
        self.items = []
    def addItem(self,str):
        self.items.append(str)
    def getClassiness(self):
        value = 0
        for i in self.items:
            if i == "tophat":
                value += 2
            elif i == "bowtie":
                value += 4
            elif i == "monocle":
                value += 5
            else:
                value += 0
        return value        
    

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())