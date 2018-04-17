import CONFIG
import mysql.connector

#列
class Column(dict):
    def __init__(self,*args):
        __d={}
        __d['field']=args[0]
        __d['type']=args[1]
        __d['null']=args[2]
        __d['key']=args[3]
        __d['default']=args[4]
        __d['extra']=args[5]
        dict.__init__(self,**__d)
    def isnull(self):
        if self['null']=='NO':
            return False
        else:
            return True
    def isprimary(self):
        if self['key']=='PRI':
            return True
        else:
            return False
    def isunique(self):
        if self['key']=='UNI':
            return True
        else:
            return False
# 元类
class Mysqlservermetaclass(type):
    def __new__(mcs, name, bases, attrs):
        attrs['DBSERVER'] = CONFIG.MYSQLDBSERVER
        return type.__new__(mcs, name, bases, attrs)


class MysqlDBmetaclass(Mysqlservermetaclass):
    def __new__(mcs, name, bases, attrs):
        attrs['db_name'] = name
        attrs['dbconn'] = {'database': name}
        return type.__new__(mcs, name, bases, attrs)


class MysqlTableMetaclass(MysqlDBmetaclass):
    def __new__(mcs, name, bases, attrs):
        attrs['table_name'] = name
        return type.__new__(mcs, name, bases, attrs)


# 基类
class MysqlserverBase(metaclass=Mysqlservermetaclass):
    @classmethod
    def __getconn(cls):
        conn = mysql.connector.connect(**cls.DBSERVER)
        return conn

    @classmethod
    def databases(cls):
        conn = cls.__getconn()
        cr = conn.cursor()
        sql = 'show databases;'
        cr.execute(sql)
        t = cr.fetchall()
        __databases = []
        for tp in t:
            __databases.append(tp[0])
        return __databases


class MysqlDBBase(metaclass=MysqlDBmetaclass):
    @classmethod
    def __getconn(cls):
        LOCAL_DB = dict(cls.DBSERVER, **cls.dbconn)
        conn = mysql.connector.connect(**LOCAL_DB)
        return conn

    @classmethod
    def fetchalldata(cls, sql):
        conn = cls.__getconn()
        cr = conn.cursor()
        cr.execute(sql)
        t = cr.fetchall()
        return t

    @classmethod
    def changedata(cls, sql):
        conn = cls.__getconn()
        cr = conn.cursor()
        cr.execute(sql)
        conn.commit()

    @classmethod
    def tables(cls):
        conn = cls.__getconn()
        cr = conn.cursor()
        sql = 'show tables;'
        cr.execute(sql)
        t = cr.fetchall()
        __tables = []
        for tp in t:
            __tables.append(tp[0])
        return __tables


class MysqlTableBase(metaclass=MysqlTableMetaclass):
    #表定义
    @classmethod
    def desc(cls):
        sql = 'desc %s;' % cls.table_name
        __desc = cls.fetchalldata(sql)
        res=[]
        for tp in __desc:
            __d=Column(*tp)
            res.append(__d)
        return res

    # 获取列名
    @classmethod
    def colnames(cls):
        sql = 'desc %s;' % cls.table_name
        t = cls.fetchalldata(sql)
        __colnames = []
        for tp in t:
            __colnames.append(tp[0])
        return __colnames

    # DML增删改查
    @classmethod
    def select(cls, DISTINCT='', FIELD='', TABLES='', WHERE='', LIMIT='', ORDER_BY=''):
        __SELECT = "select {} {} from {} {} {} {};".format(DISTINCT, FIELD, TABLES, WHERE, LIMIT, ORDER_BY)
        return __SELECT

    @classmethod
    def insert(cls, TABLES='', FIELD='', VALUES=''):
        __INSERT = "insert into {} {} values {};".format(TABLES, FIELD, VALUES)
        return __INSERT

    @classmethod
    def update(cls, TABLES='', KEYWORDS='', WHERE=''):
        __UPDATE = "update {} set {} {};".format(TABLES, KEYWORDS, WHERE)
        return __UPDATE

    @classmethod
    def delete(cls, TABLES='', WHERE=''):
        __DELECT = "delete from {} {};".format(TABLES, WHERE)
        return __DELECT
    #DDL更改表
    @classmethod
    def addcol(cls,TABLES='',FIELD='',DATATYPE=''):
        __ADDCOL="ALTER TABLE {} ADD {} {};".format(TABLES,FIELD,DATATYPE)
        return __ADDCOL
    @classmethod
    def altercol(cls,TABLES='',FIELD=''):
        __ALTERCOL = "ALTER TABLE {} ALTER COLUMN {};".format(TABLES, FIELD)
        return __ALTERCOL
    @classmethod
    def dropcol(cls,TABLES='',FIELD='',DATATYPE=''):
        __DROPCOL = "ALTER TABLE {} DROP COLUMN {} {};".format(TABLES, FIELD,DATATYPE)
        return __DROPCOL
    # 查询数据
    @classmethod
    def fetch(cls,BUFFERSIZE=0, OFFSET=1):
        if BUFFERSIZE == 0:
            __SQL = cls.select(FIELD='*', TABLES=cls.table_name)
        else:
            __SQL = cls.select(FIELD='*', TABLES=cls.table_name,LIMIT='LIMIT {},{};'.format((OFFSET - 1) * BUFFERSIZE, BUFFERSIZE))
        return cls.fetchalldata(__SQL)

    # 列出表内总数
    @classmethod
    def count(cls):
        __SQL = cls.select(FIELD='count(*)', TABLES=cls.table_name)
        print(__SQL)
        __NUM = cls.fetchalldata(__SQL)
        return __NUM[0][0]


# 类
class Mysqlserver(MysqlserverBase):
    pass


class MysqlDB(MysqlDBBase):
    pass


class MysqlTable(dict,MysqlTableBase):
    #记录查询条件
    def __init__(self,**kw):
        for key in kw:
            assert key in self.colnames(), "当前表中没有->{}<-列".format(key)
        dict.__init__(self, **kw)
    #符合条件的数据
    def data(self, BUFFERSIZE=0, OFFSET=1):
        if self =={}:
            return []
        else:
            __condition = 'where'
            for key in self:
                __condition = __condition + ' {}=\'{}\' and'.format(key, self[key])
            __condition = __condition[:-4]
            if BUFFERSIZE == 0:
                __SQL = self.select(FIELD='*', TABLES=self.table_name,WHERE=__condition)
            else:
                __SQL = self.select(FIELD='*', TABLES=self.table_name,WHERE=__condition,LIMIT='LIMIT {},{};'.format((OFFSET - 1) * BUFFERSIZE, BUFFERSIZE))
            return self.fetchalldata(__SQL)
    #子查询
    def fliter(self,obj):
        pass
    #insert 单列，批量
    def add(self):
        pass
    #update 单列，批量
    def change(self):
        pass
    #delete 单列，批量
    def remove(self):
        pass



    def save(self):
        __COLNAME='( '
        __VALUES='( '
        for key in self:
            if self[key]=='':
                pass
            else:
                __COLNAME=__COLNAME+key+','
                __VALUES=__VALUES+'\''+self[key]+'\''+','
        __COLNAME=__COLNAME[:-1]+')'
        __VALUES=__VALUES[:-1]+')'
        __SQL=self.insert(TABLES=self.table_name,FIELD=__COLNAME,VALUES=__VALUES)
        print(__SQL)
        try:
            self.changedata(__SQL)
            return True
        except Exception as e:
            print(e)
            return False




    # 辅助功能


if __name__ == '__main__':
    class DBserver(Mysqlserver):
        pass


    class Groupdata1(MysqlDB, DBserver):
        pass


    class Group10(MysqlTable, Groupdata1):
        def p(self):
            print(self.__class__.__name__)


    class Crm(MysqlDB, DBserver):
        pass
    class Product(MysqlTable, Crm):
        pass
    db = DBserver()
    l = Group10(**{'QunNum': 900002})
    p1=Product()
    print(l.data(2))
    print(l.desc())
    p2=Product(product_price=15000)

