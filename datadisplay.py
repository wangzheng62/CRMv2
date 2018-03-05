from func import Colnamesmap
class Datatojson(dict):
    def __init__(self,obj,step = 30):
        d={}
        d["table_name"]=obj.table_name
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
if __name__=='__main__':
    from func import Product
    d=Datatojson(Product,step = 2)
    print(d)
    p=Product()
    d1=Datatojson(p)
    print(d1)
