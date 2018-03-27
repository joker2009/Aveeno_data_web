from django.test import TestCase

# Create your tests here.
from django.db import models

import MySQLdb
from django.shortcuts import render_to_response


conn = MySQLdb.connect(host='localhost', user='root',
                       passwd='root', db='aveeno_databag',
                       port=3306)
cur = conn.cursor()

# current_page = request.GET["Page"]
current_page = 4
a = int(current_page)*3
sql = "select *,(select count(*) from aveeno_data_exception) from aveeno_data_exception limit " + str(a) + ", 3;"
cur.execute(sql)
infos = cur.fetchall()
results = []
for info in infos:
    results.append({'barcode': info[1], 'sku_name': info[2], 'wcc_id': info[3],
                    'packagecode': info[4], 'createtime': info[5]})

count = info[6]
print(count)


cur.close()
conn.close()


def test(count, current_page, results):
    if count % 3 == 0:
        num_pages = count/3
    else:
        num_pages = count/3 + 1

    last_page = int(num_pages) - 1
    int_curr_page = int(current_page)
    if int_curr_page == 0:
        has_previous = False
    else:
        has_previous = True
    if int_curr_page == int(num_pages) - 1:
        has_next = False
    else:
        has_next = True

    previous_page_number = int_curr_page - 1
    next_page_number = int_curr_page + 1

    return render_to_response('test.html', {'results': results, 'count': count, 'num_pages': num_pages,
                                 'last_page': last_page, 'precious_page_number': previous_page_number,
                                 'next_page_number': next_page_number, 'has_next': has_next})





