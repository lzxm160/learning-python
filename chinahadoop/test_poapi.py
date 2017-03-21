import urllib2
import json


data = {
   "operation":"SubmitPO",
   "data":{
      "request_system":1,
"request_time":"2017-02-16 08:00:00",
      "purchase_order":{
         "website":"France",
         "company":"ReneSola France",
         "bill_type":"Purchase Order",
         "po_no":"PO-FR-20170216-001014",
         "po_url":"/root/go_fcgi/go_fcgi",
         "po_date":"2017-02-16 18:00:00",
         "created_by":"po_no",
"approved_by":"",
         "status":1,
"supplier":"Renesola Shanghai",
         "requested_delivery_date":"2017-03-20 24:00:00",
"trade_term":"EXW",
         "payment_terms":"30 Days EOM The 15",
         "ship_via":"Sea",
         "export_country":"P.R.China",
         "loading_port":"Shenzhen",
         "import_country":"France",
         "unloading_port":"Amsterdam",
         "certificate":"",
         "total_quantity":2400,
         "total_amount":5690.47,
         "currency":"EUR",
         "comments":"comments1",
         "note":"note1",
         "detail":[{
            "product_name":"Highbay",
            "product_code":"RHB120X0302",
            "item_no":"3518020400845",
            "unit_price":3.64,
            "quantity":1000,
            "uom":"PCS",
            "sub_total":3640.00,
            "warranty":3,
            "comments":"detail comments1",
"note":"detail note1"
},{
            "product_name":"Flood Light",
            "product_code":"RFL400AK01D06",
            "item_no":"3518030601741",
            "unit_price":6.89,
            "quantity":200,
            "uom":"PCS",
            "sub_total":1378.00,
            "warranty":3,
            "comments":"detail comments2",
"note":"detail note2"
}]
}
   }
}
json_data = json.dumps(data)
from time import clock
from time import time
import commands

def test_po_api():
	req = urllib2.Request("http://172.18.100.72:9888/po/submit")
	result = urllib2.urlopen(req, json_data)
	print '\n'.join(result.readlines())
gdn_data='''{
    "operation": "DeliverGoods",
    "data": {
        "request_system": 1,
        "request_time": "2017-02-16 08:00:00",
        "deliver_notes": [
            {
                "bill_type": "Goods Delivery Note",
                "gdn_no": "GDN-FR-20170216-001014-001",
                "po_no": "PO-FR-20170216-001014",
                "supplier": "Renesola Shanghai",
                " buyer": "George Wang",
                "trade_term": "CIF",
                "ship_via": "Sea",
                "packing_method": "Pallet",
                "export_country": "P.R.China",
                "loading_port": "Shenzhen",
                "import_country": "France",
                "unloading_port": "Amsterdam",
                "logistic": "DHL",
                "logistic_contact": "",
                "logistic_contact_email": "",
                "logistic_contact_telephone_number": "",
                "etd": "2017-02-28 17:00:00",
                "eta": "2017-03-17 10:00:00",
                "customs_clearance_date": "2017-03-18 10:00:00",
                "total_freight_charges": 879.65,
                "total_insurance_fee": 262,
                "total_excluded_tax": 3650.65,
                "currency": "EUR",
                "commercial_invoice": {
                    "ci_no": "CI-FR-20170226-000196",
                    "ci_url": "/opt/renesola/apollo/file/ci/CI-FR-20170226-000196.pdf",
                    "ci_date": "2017-02-16 18:00:00",
                    "status": 1,
                    "company": "Renesola France",
                    "invoice_type": 0,
                    "total_amount": 5690.47,
                    "currency": "EUR",
                    "created_by": "",
                    "approved_by": "",
                    "note": ""
                },
                "packing_list": {
                    "pl_no": "PKL-FR-20170226-000196",
                    "pl_url": "/opt/renesola/apollo/file/pkl/PKL-FR-20170226-000196.pdf"
                },
                "bill_of_lading": {
                    "bl_no": "bl_no",
                    "bl_url": "/opt/renesola/apollo/file/ci/CI-FR-20170226-000196.pdf"
                },
                "associated_so": {
                    "associated_so_no": "SC-FR-20170226-000196",
                    "associated_so_url": "/opt/renesola/apollo/file/sc/SC-FR-20170226-000196.pdf"
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
                "comments": "",
                "note": ""
            }
        ]
    }
}'''
json_gdn_data = json.dumps(gdn_data)

def test_gdn_data_api():
	req = urllib2.Request("http://172.18.100.72:9888/po/deliver_goods")
	result = urllib2.urlopen(req, json_gdn_data)
	print '\n'.join(result.readlines())
if __name__ == '__main__':
	# test_po_api()
	test_gdn_data_api()