class Essai():

    def __init__(self,*args):
        self.no1 = args[0]
        self.no2 = None
        if len(args) > 1:
            self.no2 = args[1]
    def fnct1(self):
        print(self.no1)


    def fnct2(self):
        print(self.no2)

if __name__ == '__main__':
    test = Essai('a','c')
    test.fnct1()
    test.fnct2('b')
