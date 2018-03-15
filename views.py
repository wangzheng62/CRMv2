from flask import Flask, redirect, url_for, render_template, request, flash,session,g
from func import DBserver, Crm, Product, Orderlist, Employee, Customer,Colnamesmap
from flask_login import LoginManager, login_user, login_required, logout_user
from datadisplay import Datatojson,getobj
from pages import pagedata01
app = Flask(__name__)
app.secret_key = 'some_secret'
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/test",methods=['GET','POST'])
def test():
    if request.method =='GET':
        d={'product_price':15000}
        table = Datatojson(Product(**d),step=2)
        pagedata01['table']=table
        g.name = 1
        print(g)
        print(table)
        return render_template('main.html',pages=pagedata01)
    else:
        d=request.form.to_dict()
        print(d)
        p=getobj(**d)
        table=Datatojson(p)
        return render_template('datapage.html',testdict=table)
@app.route("/test01",methods=['GET','POST'])
def test01():
    print(request.method)
    if request.method =='GET':
        return 'aa'
    elif request.method =='POST':
        print(request.data)
        return 'test_list'
    else:
        return 'lalal'
@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return Employee(user_id=user_id)


@app.route('/')
def root():
    return render_template('main.html',login=True,pages=False)


@app.route('/login', methods=['get', 'post'])
def login():
    kw = request.form.to_dict()
    e = Employee(user_id=kw['username'])
    if e.count() == 1 and kw['password']==e.search()[0][9]:
        print('1')
        login_user(e)
        flash('登陆成功')
        return redirect(url_for('test'))
    else:
        print('1')
        flash('账户或密码不对')
        return render_template('main.html', login=True, pages=False)


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/customermain')
def customermain():
    return render_template('customermain.html')


@app.route('/ordermain')
def ordermain():
    return render_template('ordermain.html')


@app.route('/productmain')
def prouductmain():
    return render_template('productmain.html')


@app.route('/employeemain')
def employeemain():
    return render_template('employeemain.html')


# 客户页
@app.route('/customernow')
def customernow():
    return render_template('customermain.html', welcome="本功能尚未开放")


@app.route('/customersearch')
def customersearch():
    res = Customer.fetchall()
    res.insert(0, Customer.colnames())
    return render_template('customermain.html', customerlist=res)


@app.route('/customeradd')
def customeradd():
    res = Customer.desc()
    return render_template('customermain.html', customerform=res, bindurl='addcustomer')


@app.route('/customeranalyze')
def customeranalyze():
    return render_template('customermain.html', welcome="本功能尚未开放")


# 客户页功能
@app.route('/nowcustomer', methods=["get", "post"])
def nowcustomer():
    return render_template('customermain.html', welcome="本功能尚未开放")


@app.route('/searchcustomer', methods=["get", "post"])
def searchcustomer():
    return render_template('customermain.html', welcome="本功能尚未开放")


@app.route('/addcustomer', methods=["get", "post"])
def addcustomer():
    res = request.form.to_dict()
    p = Customer(**res)
    if p.save():
        flash("添加成功")
    else:
        flash("添加失败")
    return redirect(url_for("customeradd"))


@app.route('/analyzecustomer', methods=["get", "post"])
def analyzecustomer():
    return render_template('customermain.html', welcome="本功能尚未开放")


# 产品页
@app.route('/productnow')
def productnow():
    return render_template('test.html', pages=pagedata01)


@app.route('/productsearch')
def productsearch():
    return render_template('test.html', pages=pagedata01)


@app.route('/productadd')
def productadd():
    return render_template('test.html', pages=pagedata01)


@app.route('/productanalyze')
def productanalyze():
    return render_template('test.html', pages=pagedata01)


# 产品页功能
@app.route('/nowproduct', methods=["get", "post"])
def nowproduct():
    return render_template('productmain.html', welcome="本功能尚未开放")


@app.route('/searchproduct', methods=["get", "post"])
def searchproduct():
    return render_template('productmain.html', welcome="本功能尚未开放")


@app.route('/addproduct', methods=["get", "post"])
def addproduct():
    res = request.form.to_dict()
    p = Product(**res)
    if p.save():
        flash("添加成功")
    else:
        flash("添加失败")
    return redirect(url_for("productadd"))


@app.route('/analyzeproduct', methods=["get", "post"])
def analyzeproduct():
    return render_template('productmain.html', welcome="本功能尚未开放")


# 订单页
@app.route('/ordernow')
def ordernow():
    return render_template('ordermain.html', welcome="本功能尚未开放")


@app.route('/ordersearch')
def ordersearch():
    res = Orderlist.fetchall()
    res.insert(0, Orderlist.colnames())
    return render_template('ordermain.html', orderlist=res)


@app.route('/orderadd')
def orderadd():
    res = Orderlist.desc()
    return render_template('ordermain.html', orderform=res, bindurl='addorder')


@app.route('/orderanalyze')
def orderanalyze():
    return render_template('ordermain.html', welcome="本功能尚未开放")


# 产品页功能
@app.route('/noworder', methods=["get", "post"])
def noworder():
    return render_template('ordermain.html', welcome="本功能尚未开放")


@app.route('/searchorder', methods=["get", "post"])
def searchorder():
    return render_template('ordermain.html', welcome="本功能尚未开放")


@app.route('/addorder', methods=["get", "post"])
def addorder():
    res = request.form.to_dict()
    o = Orderlist(**res)
    if o.save():
        flash("添加成功")
    else:
        flash("添加失败")
    return redirect(url_for("orderadd"))


@app.route('/analyzeorder', methods=["get", "post"])
def analyzeorder():
    return render_template('ordermain.html', welcome="本功能尚未开放")


# 员工页
@app.route('/employeenow')
def employeenow():
    return render_template('employeemain.html', welcome="本功能尚未开放")


@app.route('/employeesearch')
def employeesearch():
    res = Employee.fetchall()
    res.insert(0, Employee.colnames())
    return render_template('employeemain.html', employeelist=res)


@app.route('/employeeadd')
def employeeadd():
    res = Employee.desc()
    return render_template('employeemain.html', employeeform=res, bindurl='addemployee')


@app.route('/employeeanalyze')
def employeeanalyze():
    return render_template('employeemain.html', welcome="本功能尚未开放")


# 员工页功能
@app.route('/nowemployee', methods=["get", "post"])
def nowemployee():
    return render_template('employeemain.html', welcome="本功能尚未开放")


@app.route('/searchemployee', methods=["get", "post"])
def searchemployee():
    return render_template('employeemain.html', welcome="本功能尚未开放")


@app.route('/addemployee', methods=["get", "post"])
def addemployee():
    res = request.form.to_dict()
    p = Employee(**res)
    if p.save():
        flash("添加成功")
    else:
        flash("添加失败")
    return redirect(url_for("employeeadd"))


@app.route('/analyzeemployee', methods=["get", "post"])
def analyzeemployee():
    return render_template('employeemain.html', welcome="本功能尚未开放")

@app.route('/fliter', methods=["get", "post"])
def fliter():
    d=request.args.to_dict()
    print(d)
    return render_template('employeemain.html', welcome="本功能尚未开放")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
