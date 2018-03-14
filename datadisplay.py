from func import DBserver, Crm, Product, Orderlist, Employee, Customer,Colnamesmap
class Datatojson(dict):
    def __init__(self,obj,step = 30):
        d={}
        d["tablename"]=obj.table_name
        d["desc"]=obj.desc()
        colnames = obj.colnames()
        chinese = []
        for name in colnames:
            aa = Colnamesmap(colname=name)
            chinese.append(aa.search()[0][2])
        coltuple = list(zip(colnames, chinese))
        d["colnames"]=coltuple
        try:
            d["data"] = obj.search()#实例
        except:
            d["data"] = obj.fetchall()#类数据
        d["step"]=step
        if len(d["data"])/d["step"]>1 and len(d["data"])%d["step"]!=0:
            pages = int(len(d["data"])/d["step"])+1
        elif len(d["data"])/d["step"]>1 and len(d["data"])%d["step"]==0:
            pages = int(len(d["data"])/d["step"])
        else:
            pages=1
        d["pages"]=pages
        dict.__init__(self,**d)
def getobj(**kw):
    tablename=kw['tablename']
    kw.pop('tablename')
    print(kw)
    if kw=={}:
        return eval(tablename)
    else:
        ins=eval('%s(**kw)'%tablename)
        return ins


if __name__=='__main__':
    from func import Product
    d=Datatojson(Product,step = 2)
    print(d)
    p=Product()
    d1=Datatojson(p)
    print(d1)
