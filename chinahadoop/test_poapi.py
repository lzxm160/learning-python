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

if __name__ == '__main__':
	test_po_api()