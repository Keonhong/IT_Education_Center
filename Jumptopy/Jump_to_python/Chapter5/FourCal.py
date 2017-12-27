class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    # def sum(self):
    #    result = self.first + self.second
    #    return result
    def sum(self):
        return self.first+self.second


a = FourCal()
a.setdata(1,2)
# FourCal.setdata(a,4,2)

print(a.first)
print(a.second)

a.first = 3
a.second = 4

print(a.first)
print(a.second)

print(a.sum())