#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json

test_no="001294"
data = {
    "request_system": 2,
    "request_time": "2017-02-16 08:00:00",
    "operation": "SubmitPO",
    "data": {
        "purchase_order": {
            "company": "ReneSola France",
            "bill_type": "Purchase Order",
            "po_no": "PO-FR-20170216-"+test_no,
            "po_url": "/file/ci/CI-FR-20170226-000196.pdf",
            "po_date": "2017-02-16 18:00:00",
            "created_by": "Siyabonga gura",
            "approved_by": "approved_by",
            "status": 1,
            "supplier": "Renesola Shanghai",
            "requested_delivery_date": "2017-03-20 24:00:00",
            "trade_term": "EXW",
            "payment_terms": "Bank Acceptance|45 Days Net",
            "ship_via": "Sea",
            "export_country": "P.R.China",
            "loading_port": "Shenzhen",
            "import_country": "France",
            "unloading_port": "Amsterdam",
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
                    "certificate": "certificate",
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
                    "certificate": "certificate",
                    "warranty": 3,
                    "comments": "comments2",
                    "note": "note2"
                }
            ]
        }
    }
}

json_data = json.dumps(data)
from time import clock
from time import time
import commands


def test_po_api85():
	start=time()
	req = urllib2.Request("http://172.18.100.85:9888/po/submit")
	result = urllib2.urlopen(req, json_data)
	print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000,"ms"
def test_po_check():
    start=time()
    req = urllib2.Request("http://172.18.100.85:9888/po/check")
    result = urllib2.urlopen(req, json_data)
    print '\n'.join(result.readlines())
    finish=time()
    print (finish-start)*1000,"ms"
gdn_data1={
    "request_system": 1,
    "request_time": "2017-02-16 08:00:00",
    "operation": "DeliverGoods"}
json_gdn_data1 = json.dumps(gdn_data1,ensure_ascii=False)
def test_json():
    start=time()
    req = urllib2.Request("http://172.18.100.85:8877/json")
    result = urllib2.urlopen(req, json_gdn_data1)
    print '\n'.join(result.readlines())
    finish=time()
    print (finish-start)*1000,"ms"
if __name__ == '__main__':
	# test_po_api85()
	# test_gdn_data_api85()
   # test_json() 
    test_po_check() 