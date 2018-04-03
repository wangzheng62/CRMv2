
def buffer(BUFFERSIZE,*args):
    i=0
    m=0
    n=BUFFERSIZE
    while(True):
        if args[m:n]==():
            m=m-BUFFERSIZE
            n=n-BUFFERSIZE
            i=i-1
            p=yield args[m:n]
            try:
                p=int(p)
                print(p)
            except:
                pass
        else:
            p = yield args[m:n]
            try:
                p=int(p)
                print(p)
            except:
                pass
        if p == 'next' or p == None:
            i = i + 1
            m = i * BUFFERSIZE
            n = (i + 1) * BUFFERSIZE
        elif p == 'last':
            i = i - 1
            m = i * BUFFERSIZE
            n = (i + 1) * BUFFERSIZE
        elif isinstance(p, int):
            i=p-1
            m = i * BUFFERSIZE
            n = (i + 1) * BUFFERSIZE
        else:
            pass
def getbuf(message,*args,BUFFERSIZE=2):
    while 1:
        t=yield from buffer(BUFFERSIZE,*args)
        b.send(None)
    while(True):
        b.send(message)


if __name__=='__main__':
    from func import Product
    l = Product.fetchall()
    b = buffer(*l)
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
    print(b.send("last"))

