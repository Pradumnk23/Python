def div(a, b):
    print(a/b)

def smart_work(function):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return function(a,b)
    return inner

div2 = smart_work(div)
div2(2,4)