import urllib2
import json


data = {    "operation": "DeliverGoodsForPO",    "data": {        "request_system": 1,        "request_time": "2017-02-16 08:00:00",        "purchase_order": {            "bill_type": "Purchase Order",            "po_no": "PO-FR-20170216-001014",            "po_url": "/root/go_fcgi/go_fcgi",            "po_date": "2017-02-16 18:00:00",            "created_by": "",            "approved_by": "",            "status": 1,            "supplier": "Renesola Shanghai",            "website": "France",            "company": "ReneSola France",            "requested_delivery_date": "2017-03-20 24:00:00",            "trade_term": "EXW",            "payment_terms": "",            "ship_via": "Sea",            "destination_country": "France",            "loading_port": "Amsterdam",            "certificate": "",            "total_quantity": 2400,            "total_amount": 5690.47,            "currency": "EUR",            "comments": "",            "note": "",            "detail": [                {                    "product_name": "Highbay",                    "product_code": "RHB120X0302",                    "item_no": "3518020400845",                    "unit_price": 3.64,                    "quantity": 1000,                    "uom": "PCS",                    "sub_total": 3640,                    "warranty": 3,                    "comments": "",                    "note": ""                },                {                    "product_name": "Flood Light",                    "product_code": "RFL400AK01D06",                    "item_no": "3518030601741",                    "unit_price": 6.89,                    "quantity": 200,                    "uom": "PCS",                    "sub_total": 1378,                    "warranty": 3,                    "comments": "",                    "note": ""                }            ]        },        "deliver_notes": [            {                "supplier": "Renesola Shanghai",                "buyer": "",                "loading_port": "Amsterdam",                "trade_term": "CIF",                "ship_via": "Sea",                "packing_method": "Pallet",                "logistic": "DHL",                "logistic_contact": "",                "logistic_contact_email": "",                "logistic_contact_telephone_number": "",                "etd": "2017-02-28 17:00:00",                "eta": "2017-03-17 10:00:00",                "customs_clearance_date": "2017-03-18 10:00:00",                "total_freight_charges": 879.65,                "total_insurance_fee": 262,                "total_excluded_tax": 3650.65,                "currency": "EUR",                "commercial_invoice": {                    "ci_no": "CI-FR-20170226-000196",                    "ci_url": "/opt/renesola/apollo/file/ci/CI-FR-20170226-000196.pdf",                    "ci_date": "2017-02-16 18:00:00",                    "status": 1,                    "company": "ReneSola France",                    "invoice_type": 0,                    "total_amount": 5690.47,                    "currency": "EUR",                    "created_by": "",                    "approved_by": "",                    "note": ""                },                "packing_list": {                    "pl_no": "PKL-FR-20170226-000196",                    "pl_url": "/opt/renesola/apollo/file/pkl/PKL-FR-20170226-000196.pdf"                },                "bill_of_lading": {                    "bl_no": "",                    "bl_url": "/opt/renesola/apollo/file/pkl/PKL-FR-20170226-000196.pdf"                },                "associated_so": {                    "associated_so_no": "SC-FR-20170226-000196",                    "associated_so_url": "/opt/renesola/apollo/file/sc/SC-FR-20170226-000196.pdf"                },                "detail": [                    {                        "product_name": "Highbay",                        "product_code": "RHB120X0302",                        "item_no": "3518020400845",                        "unit_price": 3.64,                        "quantity": 500,                        "uom": "PCS",                        "sub_total": 1820                    },                    {                        "product_name": "Flood Light",                        "product_code": "RFL400AK01D06",                        "item_no": "3518030601741",                        "unit_price": 6.89,                        "quantity": 100,                        "uom": "PCS",                        "sub_total": 689                    }                ]            }        ]    }}
json_data = json.dumps(data)
from time import clock
from time import time

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
def test_pdf():
	start=time()
	for num in range(0,50):
		req = urllib2.Request("http://172.18.100.85:9888/pdf")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/50,"ms"
def test_process_pdf():
	import commands

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
	pdf_data={"src":"http://wkhtmltopdf.org/libwkhtmltox/pagesettings.html#pageLoad","dst":"/root/go_fcgi/test.pdf"}
	json_pdf_data = json.dumps(pdf_data)
	for num in range(0,10):
		req = urllib2.Request("http://172.18.100.85:9888/pdf")
		result = urllib2.urlopen(req,json_pdf_data)
		print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000/10,"ms"
if __name__ == '__main__':
	# test_pdf()
	# test_process_pdf()
	# test_asiofcgi_pdf()
	test_process_pdf_online()
	test_pdf_online()
