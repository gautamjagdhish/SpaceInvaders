class test :
    def __init__(self, a) :
        self.name = "username"
        print(a,a)
        self.a = a

    def pp(self) :
        print(self.a)

z = [test(5)]*5
z[4].pp()