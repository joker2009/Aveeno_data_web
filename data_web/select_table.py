__author__ = 'joker_jiang'


class list_search_data():
    def __init__(self, json):
        if json['barcode'] != [None]:
            self.barcode = json['barcode']
        else:
            self.barcode = ''
        if json['sku_name'] != [None]:
            self.sku_name = json['sku_name']
        else:
            self.sku_name = ''
        if json['wcc_id'] != [None]:
            self.wcc_id = json['wcc_id']
        else:
            self.wcc_id = ''
        if json['packagecode'] != [None]:
            self.packagecode = json['packagecode']
        else:
            self.packagecode = ''
        if json['createtime'] != [None]:
            self.createtime = json['createtime']
        else:
            self.createtime = ''

    # def makeup_search_sql(self):



