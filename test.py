
def buffer(*args,BUFFERSIZE=2):
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
def getbuf(message,f):
    try:
        val=f.send(message)
    except:
        f.send(None)
        val=f.send(message)
    finally:
        return val



if __name__=='__main__':
    from func import Product
    l = Product.fetchall()
    b = buffer(*l)
    print(getbuf(1,b))
    print(getbuf('next', b))
    print(getbuf('next', b))
