class first():
    def one(self,a):
        self.a=a
        return self.a

    def two(self):
        self.a+=2
        return self.a

    def three(self):
        self.a+=7
        return self.a
x=first()
print(x.one(7))
print(x.two())
