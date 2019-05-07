from db import Db


class Check(object):
    '''
    本类主要用于在跟k3进行数据同步时的错误信息的查验
    '''

    def __init__(self):
        db = Db()
        self.cursor = db.cursor
        self.conn = db.conn

    def formatter(self, sql):
        '''
        执行指定的sql查询，并格式化输出
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        i = 1
        for r in result:
            for k in r:
                print(str(k).rjust(25) + ':' + ' ' + str(r[k]))
            print(str(i) + '*' * 100)
            i += 1

    def yarn_stock_in(self, code):
        '''
        用于查询yarn_stock_in以及yarn_stock_in_details 以及对应的往来户的关联信息
        :param code:
        :return:
        '''
        sql = 'select a.code,a.knit_order_code,a.yarn_suppliers_id,e.code as "供应商",d.name,a.approve_date,a.status,a.knit_factory_id,a.is_success,from_unixtime(a.transmission_created)' \
              ' as transmission_created,a.deleted_at,a.sys_cargo_owner_id,a.create_type_info,a.yarn_stock_out_id,b.delivery_number,b.yarn_attr,c.code as "仓库编码",b.id detail_id,c.name as "仓库"' \
              ' from yarn_stock_in as a,yarn_stock_in_details as b,company_accounts as c,company_accounts as d,company_accounts as e where a.id =b.yarn_delivery_order_id and a.knit_factory_id=c.id and      a.yarn_suppliers_id=d.id and a.yarn_suppliers_id=e.id and a.code="%s"' % (code)
        self.formatter(sql)

    def dye_stock_in(self, code):
        '''
        用于查询dye_stock_in以及dye_stock_in_details 以及对应的往来户的关联信息
        :param code:
        :return:
        '''
        sql = 'select a.code,a.order_code,a.approve_date,a.status,a.deleted_at,a.sys_cargo_owner_id,a.factory_id,a.is_success,from_unixtime(a.transmission_created),' \
              'b.id as detail_id,c.code as factory_code,c.name,d.id as "产品id",d.code as "产品编码",d.name as "产品名称" ' \
              'from dye_stock_in as a,dye_stock_in_details as b,company_accounts as c,new_products as d where a.id =b.dye_stock_in_id and a.factory_id=c.id and b.product_id =d.id and a.code="%s"' % (
            code)
        self.formatter(sql)

    def knit_stock_in(self, code):
        '''
        用于查询knit_stock_in以及knit_stock_in_details 以及对应的往来户的关联信息
        :param code:

        :return:
        '''
        sql = 'select a.code,a.order_code,a.approve_date,a.status,a.deleted_at,a.sys_cargo_owner_id,a.factory_id,a.out_factory_id as "调出地址",a.is_success,from_unixtime(a.transmission_created),' \
              'b.id as detail_id,d.id as "产品ID",d.code as "产品编码",c.code as factory_code,c.name from knit_stock_in as a,knit_stock_in_details as b,company_accounts as c,new_products as d,new_products as e where a.id =b.knit_stock_in_id and a.factory_id=c.id and b.product_id=d.id and a.code="%s"' % (
            code)
        self.formatter(sql)

    def printing_stock_in(self, code):
        '''
        用于查询printing_stock_in以及printing_stock_in_detail 以及对应的往来户的关联信息
        :param code:
        :return:
        '''
        sql = 'select a.code,a.source_order_code,a.approve_date,a.deleted_at,a.from_factory_id,a.is_success,from_unixtime(a.transmission_created),b.id as detail_id,' \
              'b.sys_cargo_owner_id,c.code as factory_code,c.name from printing_stock_in as a,printing_stock_in_detail as b,company_accounts as c  where a.id =b.printing_stock_in_id and a.from_factory_id=c.id and a.code="%s"' % (
            code)
        self.formatter(sql)

    def yarn_stock_out(self, code):
        """
        用于查询yarn_stock_out以及yarn_stock_out_details 以及对应的往来户的关联信息
        :param code:
        :return:
        """
        sql = 'select a.code,a.produce_order_code,a.factory_id,a.to_factory_id,a.approve_date,a.status,a.is_success,from_unixtime(a.transmission_created) as transmission_created,' \
              'a.deleted_at,a.sys_cargo_owner_id,c.code as factory_code,c.name,b.id as detail_id,d.id as "物料id",d.code as "物料编码",d.name as "物料名称"' \
              ' from yarn_stock_out as a,yarn_stock_out_details as b,company_accounts as c,yarns as d ' \
              'where a.id =b.yarn_stock_out_id and a.factory_id=c.id and b.yarn_id=d.id and a.code="%s"' % (
            code)
        self.formatter(sql)

    def get_company(self, id=''):
        sql = 'select * from company_accounts where id=%d' % id
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for r in result:
            for k in r:
                print(str(k).rjust(25) + ':' + ' ' + str(r[k]))

    def dye_stock_out(self, code):
        """
        用于查询dye_stock_out以及dye_stock_details 以及对应的往来户的关联信息
        :param code:
        :return:
        """
        sql = 'select a. code,a.order_code,a.approve_date,a. status,a.deleted_at,a.sys_cargo_owner_id,a.factory_id,a.is_success,from_unixtime(a.transmission_created),b.id as detail_id,c.code as factory_code,c.name as "存放地址",d.code as "客户编码",d.name as "客户名称" from dye_stock_out as a,dye_stock_out_details as b,company_accounts as c,company_accounts as d where a.id = b.dye_stock_out_id and a.factory_id = c.id and a.out_factory_id=d.id and a.code="%s"' % (code)
        print(sql)
        self.formatter(sql)

    def knit_stock_out(self, code):
        """
        用于查询knit_stock_out以及knit_stock_details 以及对应的往来户的关联信息
        :param code:
        :return:
        """
        sql = 'select a.code,a.order_code,a.approve_date,a.status,a.deleted_at,a.sys_cargo_owner_id,a.factory_id,a.is_success,from_unixtime(a.transmission_created),' \
              'b.id as detail_id,c.code as factory_code,c.name from knit_stock_out as a,knit_stock_out_details as b,company_accounts as c  where a.id =b.knit_stock_out_id and a.factory_id=c.id and a.code="%s"' % (code)
        self.formatter(sql)

    def printing_stock_out(self, code):
        """
        用于查询printing_stock_out以及printing_stock_details 以及对应的往来户的关联信息
        :param code:
        :return:
        """
        sql = 'select a.code,a.source_order_code,a.approve_date,a.deleted_at,a.from_factory_id,a.is_success,from_unixtime(a.transmission_created),b.id as detail_id,' \
              'b.sys_cargo_owner_id,c.code as factory_code,c.name from printing_stock_out as a,printing_stock_out_detail as b,company_accounts as c  where a.id =b.printing_stock_out_id and a.from_factory_id=c.id and a.code="%s"' % (code)
        self.formatter(sql)



if __name__ == '__main__':
    check = Check()
    # check.yarn_stock_in('YPI181222013')
    # check.dye_stock_in('DTI181221006')
    # check.knit_stock_in('KTI181226026')
    # check.printing_stock_in('PPI180131001')
    # check.get_all(1, 'YPI181031018')
    # check.yarn_stock_out('YRO181228005')
    # check.dye_stock_out('DSO181226001')
    # check.knit_stock_out('KRO181121082')
    check.printing_stock_out('PSO180831062')
    # check.get_company(849)
