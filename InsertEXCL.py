#coding=UTF-8
import urllib2
import urllib
import sys
import json
import xlwt
book=xlwt.Workbook(encoding="utf-8",style_compression=0)

sheet=book.add_sheet('test',cell_overwrite_ok=True)
url = 'http://202.207.247.42/Hander/Students/StudentsAjax.ashx?rnd%20=%200.9671627628659423'

typeEncode = sys.getfilesystemencoding()

id=2013000001
i=1
while id<2013000010:
    jsons = ""
    stuId = id
    form = {}
    form['xh'] = stuId
    form['do'] = 'getlist'
    form['limit'] = '40'
    form['offset'] = '0'
    form['order'] = 'desc';
    form['sort'] = 'xh'
    post_data = urllib.urlencode(form)
    req = urllib2.urlopen(url, post_data)
    content = req.read()
    jsons = json.loads(content)
    rows = jsons["rows"]
    for entry in rows:

        xh = entry["xh"]
        xm = entry["xm"]
        xb =entry["xb"]
        sfzh = entry["sfzh"]
        jg = entry["jg"]
        byzx = entry["byzx"]
        bjh = entry["bjh"]
        kqmc = entry["kqmc"]
        xsm = entry["xsm"]
        zymc = entry["zymc"]

        sheet.write(i, 0, xh)
        sheet.write(i, 1, xm)
        sheet.write(i, 2, xb)
        sheet.write(i, 3, sfzh)
        sheet.write(i, 4, jg)
        sheet.write(i, 5, byzx)
        sheet.write(i, 6, bjh)
        sheet.write(i, 7, kqmc)
        sheet.write(i, 8, xsm)
        sheet.write(i, 9, zymc)
    i=i+1
    id = id + 1
    book.save('/Users/dubo/Desktop/2013.xls')
    if id%100==0:
        print id



print "ok"
