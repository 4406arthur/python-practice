#implement data structure like list with integer sort.
#!/usr/bin/python

class myDataStructure(list):
    def __init__(self,s):
        self.n = s
        self.l = []
    def putIn(self,element):
        self.l.extend(element)
        if (len(element) > self.n ):
            flag = len(element)% self.n
            if (flag != 0):
                for x in range(flag):
                    self.l.pop(0)
    def extrac_asc(self,n):
        self.l.sort()
        print(self.l[0:n])

    def extrac_dec(self,j):
        self.l.sort(reverse = True)
        print(self.l[0:j])



print ("input the size u want")
s = input()
box = myDataStructure(s)

print ("input ur element")
data = raw_input()
numbers = map(int, data.split())

box.putIn(numbers)

print ("print the nTH by asceding u want")
x = input()
box.extrac_asc(x)

print ("the reverse")
y = input()
box.extrac_dec(y)

print ("thank u!")
