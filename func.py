from test__mysqlmetaclass import Mysqlserver, MysqlDB, MysqlTable


class DBserver(Mysqlserver):
    pass


class Crm(MysqlDB, DBserver):
    pass


class Employee(MysqlTable, Crm):
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.search()


class Orderlist(MysqlTable, Crm):
    @classmethod
    def kw_fetchall(cls):
        __SQL = cls.select(DISTINCT='distinct', COLNAMES='order_Id', TABLES=cls.table_name)
        print(__SQL)
        res = cls.getdata(__SQL)
        print(res)


class Product(MysqlTable, Crm):
    pass


class Customer(MysqlTable, Crm):
    pass

class Colnamesmap(MysqlTable,Crm):
    pass

e='''
      <div class="col-sm-2">
        <input type="text" class="form-control" list="test_list"><input type="number" class="form-control" aria-label="...">
      </div>

            '''
if __name__ == '__main__':
    print(Orderlist.desc())
    Orderlist.kw_fetchall()
