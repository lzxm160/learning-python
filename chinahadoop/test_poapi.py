#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json

test_no="001293"
data = {
    "request_system": 1,
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

def test_po_api():
	start=time()
	req = urllib2.Request("http://172.18.100.72:9888/po/submit")
	result = urllib2.urlopen(req, json_data)
	print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000,"ms"

gdn_data={
    "request_system": 1,
    "request_time": "2017-02-16 08:00:00",
    "operation": "DeliverGoods",
    "data": {
        "deliver_notes": [
            {
                "company": "ReneSola France",
                "bill_type": "Goods Delivery Note",
                "gdn_no": "GDN-FR-20170216-"+test_no+"-009",
                "po_no": "PO-FR-20170216-"+test_no,
                "supplier": "Renesola Shanghai",
                "buyer": "George Wang",
                "trade_term": "CIF",
                "ship_via": "Sea",
                "packing_method": "Pallet",
                "export_country": "China",
                "loading_port": "Shenzhen",
                "import_country": "France",
                "unloading_port": "Amsterdam",
                "logistic": "DHL",
                "logistic_contact": "test",
                "logistic_contact_email": "logistic_contact_email",
                "logistic_contact_telephone_number": "logistic_contact_telephone_number",
                "etd": "2017-02-28 17:00:00",
                "eta": "2017-03-17 10:00:00",
                "customs_clearance_date": "2017-03-18 10:00:00",
                "total_freight_charges": 879.65,
                "total_insurance_fee": 262,
                "total_excluded_tax": 3650.65,
                "currency": "EUR",
                "commercial_invoice": {
                    "ci_no": "CI-FR-20170226-000196",
                    "ci_url": "/file/ci/CI-FR-20170226-000196.pdf",
                    "ci_date": "2017-02-16 18:00:00",
                    "status": 1,
                    "company": "Renesola France",
                    "invoice_type": 0,
                    "total_amount": 5690.47,
                    "currency": "EUR",
                    "created_by": "Siyabonga gura",
                    "approved_by": "Siyabonga gura",
                    "note": "note"
                },
                "packing_list": {
                    "pl_no": "PKL-FR-20170226-000196",
                    "pl_url": "/file/ci/CI-FR-20170226-000196.pdf"
                },
                "bill_of_lading": {
                    "bl_no": "bl_no",
                    "bl_url": "/file/ci/CI-FR-20170226-000196.pdf"
                },
                "associated_so": {
                    "associated_so_no": "SC-FR-20170226-000196",
                    "associated_so_url": "/file/ci/CI-FR-20170226-000196.pdf"
                },
                "detail": [
                    {
                        "product_name": "Highbay",
                        "product_code": "RHB120X0302",
                        "item_no": "3518020400845",
                        "unit_price": 3.64,
                        "quantity": 500,
                        "uom": "PCS",
                        "sub_total": 1820
                    },
                    {
                        "product_name": "Flood Light",
                        "product_code": "RFL400AK01D06",
                        "item_no": "3518030601741",
                        "unit_price": 6.89,
                        "quantity": 100,
                        "uom": "PCS",
                        "sub_total": 689
                    }
                ],
                "created_by": "Siyabonga gura",
                "approved_by": "Siyabonga gura",
                "comments": "comments",
                "note": "note"
            }
        ]
    }
}
json_gdn_data = json.dumps(gdn_data,ensure_ascii=False)

def test_gdn_data_api():
	start=time()
	req = urllib2.Request("http://172.18.100.72:9888/po/deliver_goods")
	result = urllib2.urlopen(req, json_gdn_data)
	print '\n'.join(result.readlines())
	finish=time()
	print (finish-start)*1000,"ms"
def test_po_check():
    start=time()
    req = urllib2.Request("http://172.18.100.72:9888/po/check")
    result = urllib2.urlopen(req, json_data)
    print '\n'.join(result.readlines())
    finish=time()
    print (finish-start)*1000,"ms"
if __name__ == '__main__':
	# test_po_api()
	# test_gdn_data_api()
   test_po_check() 