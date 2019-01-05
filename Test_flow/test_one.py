
def one():
    def inner():
        print('aaa')

@one
def two():
    print('haha')


two()



