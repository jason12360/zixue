class Composable(object):
    def __init__(self, *args):
        print(args)
        # object.__init__(self)
        # for f in args:
        #     assert(f.__call__)
        self.func = args

    def __call__(self, x):
        for i in range(len(self.func)-1,-1,-1):
            func = self.func[i]
            assert(func.__call__)
            x = func(x)
            
        return x

    def __mul__(self, rv):
        print('jjj')
        assert(isinstance(rv, Composable))
        return Composable(*(self.func + rv.func))

composable = Composable

@composable
def add2(x):
    return x + 2

@composable
def mul3(x):
    return x * 3

@composable
def pow2(x):
    return x ** 2

# fn = add2 * mul3 * pow2
# equivalent to `add2(mul3(pow2(n)))`
# print (fn(5)) # 77