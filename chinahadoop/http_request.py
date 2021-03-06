import urllib2
import json


data = {    "operation": "DeliverGoodsForPO",    "data": {        "request_system": 1,        "request_time": "2017-02-16 08:00:00",        "purchase_order": {            "bill_type": "Purchase Order",            "po_no": "PO-FR-20170216-001014",            "po_url": "/root/go_fcgi/go_fcgi",            "po_date": "2017-02-16 18:00:00",            "created_by": "",            "approved_by": "",            "status": 1,            "supplier": "Renesola Shanghai",            "website": "France",            "company": "ReneSola France",            "requested_delivery_date": "2017-03-20 24:00:00",            "trade_term": "EXW",            "payment_terms": "",            "ship_via": "Sea",            "destination_country": "France",            "loading_port": "Amsterdam",            "certificate": "",            "total_quantity": 2400,            "total_amount": 5690.47,            "currency": "EUR",            "comments": "",            "note": "",            "detail": [                {                    "product_name": "Highbay",                    "product_code": "RHB120X0302",                    "item_no": "3518020400845",                    "unit_price": 3.64,                    "quantity": 1000,                    "uom": "PCS",                    "sub_total": 3640,                    "warranty": 3,                    "comments": "",                    "note": ""                },                {                    "product_name": "Flood Light",                    "product_code": "RFL400AK01D06",                    "item_no": "3518030601741",                    "unit_price": 6.89,                    "quantity": 200,                    "uom": "PCS",                    "sub_total": 1378,                    "warranty": 3,                    "comments": "",                    "note": ""                }            ]        },        "deliver_notes": [            {                "supplier": "Renesola Shanghai",                "buyer": "",                "loading_port": "Amsterdam",                "trade_term": "CIF",                "ship_via": "Sea",                "packing_method": "Pallet",                "logistic": "DHL",                "logistic_contact": "",                "logistic_contact_email": "",                "logistic_contact_telephone_number": "",                "etd": "2017-02-28 17:00:00",                "eta": "2017-03-17 10:00:00",                "customs_clearance_date": "2017-03-18 10:00:00",                "total_freight_charges": 879.65,                "total_insurance_fee": 262,                "total_excluded_tax": 3650.65,                "currency": "EUR",                "commercial_invoice": {                    "ci_no": "CI-FR-20170226-000196",                    "ci_url": "/opt/renesola/apollo/file/ci/CI-FR-20170226-000196.pdf",                    "ci_date": "2017-02-16 18:00:00",                    "status": 1,                    "company": "ReneSola France",                    "invoice_type": 0,                    "total_amount": 5690.47,                    "currency": "EUR",                    "created_by": "",                    "approved_by": "",                    "note": ""                },                "packing_list": {                    "pl_no": "PKL-FR-20170226-000196",                    "pl_url": "/opt/renesola/apollo/file/pkl/PKL-FR-20170226-000196.pdf"                },                "bill_of_lading": {                    "bl_no": "",                    "bl_url": "/opt/renesola/apollo/file/pkl/PKL-FR-20170226-000196.pdf"                },                "associated_so": {                    "associated_so_no": "SC-FR-20170226-000196",                    "associated_so_url": "/opt/renesola/apollo/file/sc/SC-FR-20170226-000196.pdf"                },                "detail": [                    {                        "product_name": "Highbay",                        "product_code": "RHB120X0302",                        "item_no": "3518020400845",                        "unit_price": 3.64,                        "quantity": 500,                        "uom": "PCS",                        "sub_total": 1820                    },                    {                        "product_name": "Flood Light",                        "product_code": "RFL400AK01D06",                        "item_no": "3518030601741",                        "unit_price": 6.89,                        "quantity": 100,                        "uom": "PCS",                        "sub_total": 689                    }                ]            }        ]    }}
json_data = json.dumps(data)
from time import clock
from time import time
import commands
def benchmark():
	start=time()

    
	for num in range(0,50):
		req = urllib2.Request("http://172.18.100.72:9888/po/deliver_goods")
		result = urllib2.urlopen(req, json_data)
		# print '\n'.join(result.readlines())


	finish=time()
	print (finish-start)*1000/50,"ms"

	# start1=time()
	# query_data={"operation":"QUERY_SESSION","requestData":[{"sessionId":"J57B5D55ERJHZXDPL1R2"}],"requestor":"apollo-employee-portal","requestTime":"2015-05-25 08:00:00"}
	# json_data1 = json.dumps(query_data)
	# for num in range(0,50):
	# 	req = urllib2.Request("http://172.18.100.85:8088/apollo")
	# 	result = urllib2.urlopen(req, json_data1)
	# 	# print '\n'.join(result.readlines())


	# finish1=time()
	# print (finish1-start1)*1000/50,"ms"

	# start2=time()
	# for num in range(0,50):
	# 	print urllib2.urlopen("http://127.0.0.1:9888/pdf").read()

	# finish2=time()
	# print (finish2-start2)*1000/50,"ms"

def test_check_deliver_notes_commercial_invoice():
	req = urllib2.Request("http://172.18.100.72:9888/po/deliver_goods")
	result = urllib2.urlopen(req, json_data)
	print '\n'.join(result.readlines())
# pdf_data={"src":"/root/Newshop_International/WEB-INF/quotation_pdf.html","dst":"test.pdf"}
pdf_data={"src":"/root/Newshop_International/WEB-INF/quotation_pdf.html","dst":"/root/go_fcgi/test.pdf"}
json_pdf_data = json.dumps(pdf_data)

def test_process_pdf():
	

	start=time()
	for num in range(0,50):
		status, output = commands.getstatusoutput("/usr/local/wkhtmltox/bin/wkhtmltopdf /root/Newshop_International/WEB-INF/quotation_pdf.html /root/go_fcgi/testprocess.pdf")
		print status,output
	finish=time()
	print (finish-start)*1000/50,"ms"	


def test_asiofcgi_pdf():
	start=time()
	for num in range(0,10):
		req = urllib2.Request("http://172.18.100.85/pdf")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
def test_process_pdf_online():
	start=time()
	for num in range(0,50):
		status, output = commands.getstatusoutput("/usr/local/wkhtmltox/bin/wkhtmltopdf http://wkhtmltopdf.org/libwkhtmltox/pagesettings.html#pageLoad /root/go_fcgi/testprocess.pdf")
		print status,output
	finish=time()
	print (finish-start)*1000/50,"ms"
def test_pdf_online():
	start=time()
	pdf_data={"src":"http://news.baidu.com/","dst":"/root/go_fcgi/test.pdf"}
	json_pdf_data = json.dumps(pdf_data)
	for num in range(0,10):
		req = urllib2.Request("http://127.0.0.1:9888/pdf")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
def python_pdf():
	import pdfkit
	config = pdfkit.configuration(wkhtmltopdf='/usr/local/wkhtmltox/bin/wkhtmltopdf')
	# pdfkit.from_string(html_string, output_file, configuration=config)
	# pdfkit.from_url('http://wkhtmltopdf.org/libwkhtmltox/pagesettings.html#pageLoad', '/root/go_fcgi/python_test_online.pdf', configuration=config)
	start=time()
	for num in range(0,10):
		try:
			pdfkit.from_file('/root/Newshop_International/WEB-INF/quotation_pdf.html', '/root/go_fcgi/python_test.pdf', configuration=config)
		except:
		    print "11111"
		else:
		    print "22222"

	finish=time()
	print (finish-start)*1000/10,"ms"
def test_redis():
	start=time()
	pdf_data={"operation":"QUERY_SESSION","requestData":[{"sessionId":"J57B5D55ERJHZXDPL1R2"}],"requestor":"apollo-employee-portal","requestTime":"2015-05-25 08:00:00"}
	json_pdf_data = json.dumps(pdf_data)
	for num in range(0,10):
		req = urllib2.Request("http://172.18.100.85:8088/apollo")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"

def test_pdf():
	
	start=time()
	for num in range(0,1):
		pdf_data="{\"src\":\"/root/Newshop_International/WEB-INF/quotation_pdf"+str(num)+".html\",\"dst\":\"/root/go_fcgi/test"+str(num)+".pdf\"}"
		# print pdf_data
		# json_pdf_data = json.dumps(pdf_data)	
		req = urllib2.Request("http://127.0.0.1:9888/pdf")
		result = urllib2.urlopen(req,pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/50,"ms"
def test_redis_scm_day():
	start=time()
	for num in range(0,50):
		req = urllib2.Request("http://172.18.100.85:8088/scm_flow_no/JP/PO/day")
		result = urllib2.urlopen(req)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/50,"ms"
def test_redis_scm_month():
	start=time()
	for num in range(0,50):
		req = urllib2.Request("http://172.18.100.85:8088/scm_flow_no/JP/PO/month")
		result = urllib2.urlopen(req)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/50,"ms"
def test_redis_scm_year():
	start=time()
	for num in range(0,50):
		req = urllib2.Request("http://172.18.100.85:8088/scm_flow_no/JP/PO/year")
		result = urllib2.urlopen(req)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/50,"ms"
def test_athenapdf():
	start=time()
	file_name="out.pdf"
	for num in range(0,10):
		req = urllib2.Request("http://127.0.0.1:8080/convert\?auth\=arachnys-weaver\&url\=http://news.baidu.com/")
		u = urllib2.urlopen(req)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		file_size_dl = 0
		block_sz = 8192
		while True:
		    buffer = u.read(block_sz)
		    if not buffer:
		        break

		    file_size_dl += len(buffer)
		    f.write(buffer)
		    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		    status = status + chr(8)*(len(status)+1)
		    print status,

		f.close()
	finish=time()
	print (finish-start)*1000/10,"ms"
def test_pdf2_online():
	start=time()
	pdf_data={"src":"http://news.baidu.com/","dst":"/root/go_fcgi/test.pdf"}
	json_pdf_data = json.dumps(pdf_data)
	for num in range(0,10):
		req = urllib2.Request("http://127.0.0.1:9888/pdf2")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
def test_weasyprint_process_pdf():
	
	start=time()
	for num in range(0,10):
		status, output = commands.getstatusoutput("weasyprint /root/Newshop_International/WEB-INF/quotation_pdf.html /root/learning-python/flask.pdf")
		print status,output
	finish=time()
	print (finish-start)*1000/10,"ms"	
def test_go_process_local():
	start=time()
	pdf_data={"src":"/root/Newshop_International/WEB-INF/quotation_pdf.html","dst":"/root/go_fcgi/test.pdf"}
	json_pdf_data = json.dumps(pdf_data)
	for num in range(0,10):
		req = urllib2.Request("http://127.0.0.1:9888/pdf2")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
def test_go_process_online():
	start=time()
	pdf_data={"src":"/root/Newshop_International/WEB-INF/quotation_pdf.html","dst":"/root/go_fcgi/test.pdf"}
	json_pdf_data = json.dumps(pdf_data)
	for num in range(0,10):
		req = urllib2.Request("http://127.0.0.1:9888/pdf2")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
def test_asio_process_online():
	start=time()
	pdf_data={"src":"/root/Newshop_International/WEB-INF/quotation_pdf.html","dst":"/root/asio_coro_frame/build/release/bin/test.pdf"}
	json_pdf_data = json.dumps(pdf_data)
	for num in range(0,10):
		req = urllib2.Request("http://127.0.0.1/pdf")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
data = {
    "request_system": 1,
    "request_time": "2017-02-16 08:00:00",
    "operation": "SubmitPO",
    "data": {
        "purchase_order": {
            "company": "ReneSola France",
            "bill_type": "Purchase Order",
            "po_no": "PO-FR-20170216-0016",
            "po_url": "/file/ci/CI-FR-20170226-000196.pdf",
            "po_date": "2017-02-16 18:00:00",
            "created_by": "Siyabonga gura",
            "approved_by": "approved_by",
            "status": 1,
            "supplier": "Renesola Shanghai",
            "requested_delivery_date": "2017-03-20 24:00:00",
            "trade_term": "EXW",
            "payment_terms": "payment_terms",
            "ship_via": "Sea",
            "export_country": "P.R.China",
            "loading_port": "Shenzhen",
            "import_country": "France",
            "unloading_port": "Amsterdam",
            "certificate": "certificate",
            "total_quantity": 2400,
            "total_amount": 5690.47,
            "currency": "EUR",
            "comments": "comments",
            "note": "note",
            "detail": [
                {
                    "product_name": "Highbay",
                    "product_code": "RHB120X0302",
                    "item_no": "3518020400845",
                    "unit_price": 3.64,
                    "quantity": 1000,
                    "uom": "PCS",
                    "sub_total": 3640,
                    "warranty": 3,
                    "comments": "comments1",
                    "note": "note1"
                },
                {
                    "product_name": "Flood Light",
                    "product_code": "RFL400AK01D06",
                    "item_no": "3518030601741",
                    "unit_price": 6.89,
                    "quantity": 200,
                    "uom": "PCS",
                    "sub_total": 1378,
                    "warranty": 3,
                    "comments": "comments2",
                    "note": "note2"
                }
            ]
        }
    }
}
json_data = json.dumps(data)
def test_single_mysql_time():
	start=time()
	for num in range(0,10):
		req = urllib2.Request("http://172.18.100.85:9888/test_mysql_time")
		result = urllib2.urlopen(req,json_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
if __name__ == '__main__':
	# test_po_api()
	test_single_mysql_time()
	# test_asio_process_online()
	# test_go_process_online()
	# test_athenapdf()
	# test_pdf()
	# test_process_pdf()
	# test_asiofcgi_pdf()
	# test_process_pdf_online()
	# test_pdf_online()
	# python_pdf()
	# test_redis() #1ms
	# test_redis_scm_day()
	# test_redis_scm_month()
	# test_redis_scm_year()