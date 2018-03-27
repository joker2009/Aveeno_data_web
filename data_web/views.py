from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


import MySQLdb
import xlwt
from django.shortcuts import render_to_response, render, HttpResponse
from io import StringIO, BytesIO

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from data_web.models import AveenoDataException

# from django.contrib.auth import login, logout, authenticate
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


@login_required
def test(request):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='root',
                           db='aveeno_databag', port=3306, charset="utf8")
    cur = conn.cursor()
    global current_page
    current_page = request.GET["page"]
    a = int(current_page)*3
    sql = "select *,(select count(*) from aveeno_data_exception) from aveeno_data_exception limit " + str(a) + ", 3;"
    cur.execute(sql)
    infos = cur.fetchall()

    results = []
    for info in infos:
        results.append({'barcode': info[1], 'sku_name': info[2], 'wcc_id': info[3],
                        'packagecode': info[4], 'createtime': info[5]})

    count = int(info[6])
    # print(info[6])
    # print(info[5])
    # print(count)
    # print(requests)

    if count % 3 == 0:
        num_pages = count/3
    else:
        num_pages = count/3 + 1
    num_pages = int(num_pages)
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
    cur.close()
    conn.close()
    # print(results)
    # return render_to_response('test.html', {'results': results, 'count': count, 'num_pages': num_pages,
    #                                         'current_page': current_page, 'last_page': last_page,
    #                                         'previous_page_number': previous_page_number,
    #                                         'next_page_number': next_page_number,
    #                                         'has_previous': has_previous,
    #                                         'has_next': has_next})
    return render(request, 'test.html', {'results': results, 'count': count, 'num_pages': num_pages,
                                            'current_page': current_page, 'last_page': last_page,
                                            'previous_page_number': previous_page_number,
                                            'next_page_number': next_page_number,
                                            'has_previous': has_previous,
                                            'has_next': has_next})


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('data_web:index'))


def search(request):
    barcode = request.GET.get('barcode')
    sku_name = request.GET.get('sku_name')
    wcc_id = request.GET.get('wcc_id')
    packagecode = request.GET.get('packagecode')
    createtime = request.GET.get('createtime')

    # kwargs = {
    #     # 动态查询字段
    # }
    # if barcode is not None:
    #     kwargs['barcode'] = barcode
    # if sku_name is not None:
    #     kwargs['sku_name'] = sku_name
    # if wcc_id is not None:
    #     kwargs['wcc_id'] = wcc_id
    # if packagecode is not None:
    #     kwargs['packagecode'] = packagecode
    #
    # if createtime:
    #     kwargs['createtime__contains'] = createtime
    # print(kwargs)

    global results
    # results = AveenoDataException.objects.filter(**kwargs)
    # print(results)
    # conn = MySQLdb.connect(host='localhost', user='root', passwd='root',
    #                        db='aveeno_databag', port=3306, charset="utf8")
    # cur = conn.cursor()
    # if request.method == 'POST':
    #     resp = json.loads(request.body.decode())
    #     sql =

    results = AveenoDataException.objects.filter(Q(barcode__contains=barcode) & Q(sku_name__contains=sku_name) &
                                                 Q(wcc_id__contains=wcc_id) & Q(packagecode__contains=packagecode)
                                                 & Q(createtime__contains=createtime))
    print(results)
    return render(request, 'test.html', {'results': results})


@login_required
def output(request):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='root',
                           db='aveeno_databag', port=3306, charset="utf8")
    cur = conn.cursor()
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=Aveeno.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet(u'数据表单')
    sheet.write(0, 0, '商品条码')
    sheet.write(0, 1, '产品名称')
    sheet.write(0, 2, '二维码')
    sheet.write(0, 3, '箱码')
    sheet.write(0, 4, '创建时间')
    # global current_page
    # b = int(current_page)*3
    # sql = "select * from aveeno_data_exception limit " + str(b) + ",3;"
    # # sql = "select * from aveeno_data_exception ;"
    # cur.execute(sql)
    # results = cur.fetchall()
    # print(results)
    global results
    row = 1
    for result in results:
        # sheet.write(row, 0, result['barcode'])
        # sheet.write(row, 1, result['sku_name'])
        # sheet.write(row, 2, result['wcc_id'])
        # sheet.write(row, 3, result['packagecode'])
        # sheet.write(row, 4, result['createtime'])
        barcode = result.barcode
        sku_name = result.sku_name
        wcc_id = result.wcc_id
        packagecode = result.packagecode
        createtime = result.createtime
        sheet.write(row, 0, barcode)
        sheet.write(row, 1, sku_name)
        sheet.write(row, 2, wcc_id)
        sheet.write(row, 3, packagecode)
        sheet.write(row, 4, str(createtime))
        # sheet.write(row, 0, result[1])
        # sheet.write(row, 1, result[2])
        # sheet.write(row, 2, result[3])
        # sheet.write(row, 3, result[4])
        # sheet.write(row, 4, str(result[5]))
        row += 1

    output = BytesIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    cur.close()
    conn.close()
    return response


@login_required
def down(request):
    return render(request, 'down.html')

