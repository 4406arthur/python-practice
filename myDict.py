#!/usr/bin/python
import operator

class myDic:
    def __init__(self):
        while True:
         try:
            size = int(input("give a size:"))
            break
         except ValueError:
            print("not a integer")
        self.n = size
        self.dic = {}
    def checkout(self):
        if (len(self.dic)>=self.n):
            return 0;
        else:
            return 1;
    def dicAdd(self):
        while True:
            try:
                name, age = raw_input("input name,age: ").split(",")
                name = str(name)
                age = int(age)
                break
            except ValueError:
                print("wrong value assign!")
        
        if self. checkout() == 0 :
           self.dicPop();
        self.dic.update({name:age})

    def dicPop(self):
        for item in self.dic:
            self.dic.popitem()
            break
    def dicPrint(self):
        print (self.dic)

    def dicSort(self,n):
        sorted_dic = sorted(self.dic.iteritems(), key=operator.itemgetter(1))
        print (sorted_dic[0:n])

    def dicSort_inverse(self,n):
        sorted_dic = sorted(self.dic.iteritems(),key=operator.itemgetter(1),reverse=True)
        print (sorted_dic[0:n])

