
def buffer(step=2,*args):
    i=0
    m=0
    n=step
    while(True):
        if args[m:n]==():
            m=m-step
            n=n-step
            i=i-1
            p=yield args[m:n]
        else:
            p = yield args[m:n]
        if p == 'next' or p == None:
            i = i + 1
            m = i * step
            n = (i + 1) * step
        elif p == 'last':
            i = i - 1
            m = i * step
            n = (i + 1) * step
        elif isinstance(p, int):
            i=p-1
            m = i * step
            n = (i + 1) * step
        else:
            pass
if __name__=='__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = buffer(3,*l)
    print(b.send(None))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("next"))
    print(b.send("last"))
    print(b.send(3))
    print(b.send("next"))
    print(b.send("next"))

