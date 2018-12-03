class a():
    def __init__(self):
        pass

    def say(self):
        print('a')



class b():
    def __init__(self):
        self.a=a()


b=b()
b.a.say()