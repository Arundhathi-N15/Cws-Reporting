from flask import Flask
from flask import request
from pymongo import MongoClient
import json
from bson import json_util


client = MongoClient("mongodb+srv://db_admin:VO0usJYgofYmc6is@cluster0.lnt3z.mongodb.net/?retryWrites=true&w=majority")
db = client.test

app = Flask(__name__)

@app.route("/add_seller_ageing_bucket_details", methods = ['POST'])
def add_seller_ageing_bucket_details():
    data=request.get_json()
    print("default_data",data.get("default"))
    customer_gstin=data.get("customer_gstin")
    try:
        if data.get("default")=="false":
            
            customer_ageing_bucket_data={"customer_gstin":customer_gstin,"seller_code":data.get("seller_id"),"slabs_data":data.get("slabs"),"default":data.get("default")}
        else:
            customer_ageing_bucket_data={"default":data.get("default"),
            "customer_gstin":customer_gstin,"seller_code":data.get("seller_id"),
                "slabs":[

                    {"slab_name":"ageing bucket 1-30",
                    "slab_id":1,
                    "from":1,
                    "to":30
                },
                {"slab_name":"ageing bucket 31-60",
                    "slab_id":2,
                    "from":31,
                    "to":60
                },
                {"slab_name":"ageing bucket 61-90",
                    "slab_id":3,
                    "from":61,
                    "to":90
                },
                {"slab_name":"ageing bucket 91-120",
                    "slab_id":4,
                    "from":91,
                    "to":120
                },
                {"slab_name":"ageing bucket  121-180",
                    "slab_id":5,
                    "from":121,
                    "to":180
                },
                {"slab_name":"ageing bucket  181-270",
                    "slab_id":6,
                    "from":181,
                    "to":270
                },
                {"slab_name":"ageing bucket  271-360",
                    "slab_id":7,
                    "from":271,
                    "to":360
                },
                {"slab_name":"ageing bucket  >360",
                    "slab_id":8,
                    "from":360,
                    "to":"+"
                }
                ]
                }
        
     
        collection_name=f"{customer_gstin}_seller_Agieng_bucket"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            collection.drop()
            customer_agieng_bucket_collection=db[collection_name]
            customer_agieng_bucket_collection.insert_one(customer_ageing_bucket_data)
            return {"status":True,
                "message":"Seller Ageing bucket details updated successfully"},200
        else :  
            customer_agieng_bucket_collection=db[collection_name]
            customer_agieng_bucket_collection.insert_one(customer_ageing_bucket_data)
            
            return {"status":True,
                "message":"Seller Ageing bucket details added successfully"},200
        
        
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in adding seller ageing bucket details,Please contact system administrator"},400



@app.route("/ageing/ageingSummary", methods = ['POST'])
def get_seller_ageing_summary_details():
    data=request.get_json()
    print("default_data",data)

    summary_response={
  "status":True,
  "seller_id": "768",
  "data":[{"As of Date":"22-05-2022",
  "Total Monthly Sales":4354,
  "Total Receivables":4545,
  "Not Yet Due":56656,
  "Total Overdue":64565,
  "% Overdue":10,
  "# Invoices Due":100,
  "Advance / Excess Received":34234,
  "# Invoices Advance / Excess":32,
  "DSO":34,
  "Due - B1":4545,
  "Due - B2":0,
  "Due - B3":0,
  "Due - B4":0},
  {"As of Date":"20-05-2022",
  "Total Monthly Sales":435,
  "Total Receivables":455,
  "Not Yet Due":556,
  "Total Overdue":645,
  "% Overdue":13,
  "# Invoices Due":10,
  "Advance / Excess Received":234,
  "# Invoices Advance / Excess":32,
  "DSO":34,
  "Due - B1":45457880,
  "Due - B2":0,
  "Due - B3":0,
  "Due - B4":0}]}
      
        # customer_gstin=data.get("customer_gstin")
    try:
        # 33BACDS7654A2Z3_Receivables_Summary_Data
        # collection_name= {customer_gstin}_Receivables_Summary_Data
        collection_name="33BACDS7654A2Z3_Receivables_Summary_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ doc for doc in cursor]
        
        
        
            
            return {"status":True,"data":json_docs},200
        else:
            return {"status":False,"data":[]},200
        
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Please contact system administrator"},400






@app.route("/ageing/ageingCustomer", methods = ['POST'])
def get_seller_ageing_customer_details():
    data=request.get_json()
    print("default_data",data)
    # 33BACDS7654A2Z3_Receivables_Customer_Data
    customer_details={"status":True,
        "seller_code":4,
        "data":[{"Customer GSTIN":"29ABCDE1234C1ZJ",
        "Customer PAN":"ABCDE1234C",
        "Customer Name":"ZAHORANSKY MOULDS AND MACHINES PRIVATE LIMITED",
        "Customer Code":"2232",
        "Account Manager":"ABC",
        "Registration Type":"GST Registered",
        "As of Date":"22-05-2022",
        "Total Monthly Sales":34,
        "Total Outstanding":45453,
        "Not Yet Due":4534,
        "# Invoices Due":10,
        "Total Overdue":6757,
        "Due - B1":766,
        "Due - B2":0,
        "Due - B3":0,
        "Due - B4":0
        },
        {"Customer GSTIN":"29ABCDE1244C1KJ",
        "Customer PAN":"ABCDE1244C",
        "Customer Name":"ABC PRIVATE LIMITED",
        "Customer Code":"1000",
        "Account Manager":"ABCD",
        "Registration Type":"GST UnRegistered",
        "As of Date":"23-05-2022",
        "Total Monthly Sales":30,
        "Total Outstanding":100,
        "Not Yet Due":1000,
        "# Invoices Due":11,
        "Total Overdue":7000,
        "Due - B1":900,
        "Due - B2":0,
        "Due - B3":0,
        "Due - B4":0}]}
    # customer_gstin=data.get("customer_gstin")
    try:
        # collection_name= {customer_gstin}_Receivables_Customer_Data
        collection_name="33BACDS7654A2Z3_Receivables_Customer_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ doc for doc in cursor]
                # payload={   
                # "Customer GSTIN":document.get("Customer GSTIN"),
                # "Customer PAN":document.get("Customer PAN"),
                # "Customer Name":document.get("Customer Name"),
                # "Customer Code":document.get("Customer Code"),
                # "Account Manager":document.get("Account Manager"),
                # "Registration Type":document.get("Registration Type"),
                # "Invoice Number":document.get("Invoice Number"),
                # "Invoice Date":document.get("Invoice Date"),
                # "Due Date":document.get("Due Date"),
                # "Taxable Amount":document.get("Taxable Amount"),
                # "Non Taxable Amount":document.get("Non Taxable Amount"),
                # "GST Amount":document.get("GST Amount"),
                # "Total Invoice Amount":document.get("Total Invoice Amount"),
                # "As of Date":document.get("As of Date"),
                # "TDS Collected":document.get("TDS Collected"),
                # "Amount Collected":document.get("Amount Collected"),
                # "Amount Outstanding":document.get("Amount Outstanding"),
                # "Advance / Excess Amount":document.get("Advance / Excess Amount"),
                # "Days past due date":document.get("Days past due date"),
                # "Ageing Bucket":document.get("Ageing Bucket")
                # } 
            return {"status":True,
                "data":json_docs},200
        else :  
            return {"status":False,
                "message":"No records found","data":[]},200
        
    
        
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Please contact system administrator"},400



@app.route("/ageing/ageingCustomer/topCustomers", methods = ['POST'])
def get_seller_ageing_top_customer_details():
    data=request.get_json()
    print("default_data",data)
    top_customer_details={"status":True,
        "seller_code":4,
        "data":[{"Customer GSTIN":"29ABCDE1234C1ZJ",
        "Customer Name":"ZAHORANSKY MOULDS AND MACHINES PRIVATE LIMITED",
        "Total Outstanding":45453
        },
        {"Customer GSTIN":"29ABCDE1244C1KJ",
        "Customer Name":"ABC PRIVATE LIMITED",
        "Total Outstanding":100,
       }]}


    try:
        
        # collection_name= {customer_gstin}_Receivables_Customer_Data
        collection_name="33BACDS7654A2Z3_Receivables_Customer_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ doc for doc in cursor]

            return top_customer_details,200
        else:
            return {"status":False,"data":[]},200

    
        
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Please contact system administrator"},400




@app.route("/ageing/ageingInvoiceDetails", methods = ['POST'])
def get_seller_ageing_invoice_details():
    data=request.get_json()
    try:
        # collection_name=f"{customer_gstin}_Receivables_InvoiceData"
        collection_name="test_Receivables_InvoiceData"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            
            json_docs = [ json.loads(json_util.dumps(doc)) for doc in cursor]
            # for document in cursor:
            #     payload={   
            #     "Customer GSTIN":document.get("Customer GSTIN"),
            #     "Customer PAN":document.get("Customer PAN"),
            #     "Customer Name":document.get("Customer Name"),
            #     "Customer Code":document.get("Customer Code"),
            #     "Account Manager":document.get("Account Manager"),
            #     "Registration Type":document.get("Registration Type"),
            #     "Invoice Number":document.get("Invoice Number"),
            #     "Invoice Date":document.get("Invoice Date"),
            #     "Due Date":document.get("Due Date"),
            #     "Taxable Amount":document.get("Taxable Amount"),
            #     "Non Taxable Amount":document.get("Non Taxable Amount"),
            #     "GST Amount":document.get("GST Amount"),
            #     "Total Invoice Amount":document.get("Total Invoice Amount"),
            #     "As of Date":document.get("As of Date"),
            #     "TDS Collected":document.get("TDS Collected"),
            #     "Amount Collected":document.get("Amount Collected"),
            #     "Amount Outstanding":document.get("Amount Outstanding"),
            #     "Advance / Excess Amount":document.get("Advance / Excess Amount"),
            #     "Days past due date":document.get("Days past due date"),
            #     "Ageing Bucket":document.get("Ageing Bucket")
            #     }
            #     Invoice_details.append(payload)
            
            return {"status":True,
                "data":json_docs},200
        else :  
            return {"status":True,
                "message":"No records found","data":[]},200
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing invoice details,Please contact system administrator"},400



"""Get api for dropdown details"""
@app.route("/ageing/ageingInvoiceDetails/dropdown/test", methods = ['POST'])
def get_seller_ageing_dropdown_details():
    data=request.get_json()
    customer_gstin=data.get("customer_gstin")
    cust_gstin_list,registration_type_list,agieng_list,as_of_date_list,cust_pan_list=[],[],[],[],[]
    try:
        # collection_name=f"{customer_gstin}_Receivables_InvoiceData"
        collection_name="test_Receivables_InvoiceData"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            for document in cursor:
                cust_gstin_list.append(document.get("Customer GSTIN"))
                registration_type_list.append(document.get("Registration Type"))
                agieng_list.append(document.get("Days past due date"))
                as_of_date_list.append(document.get("As of Date"))
                cust_pan_list.append(document.get("Customer PAN"))

            payload={"cust_gstin_list":cust_gstin_list,
            "registration_type_list":registration_type_list,
            "agieng_list":agieng_list,
            "as_of_date_list":as_of_date_list,
            "cust_pan_list":cust_pan_list}
            return {"status":True,
                "data":payload},200
        else :  
            return {"status":True,
                "message":"No records found","data":[]},200
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing dropdown details,Please contact system administrator"},400



"""Get api for Cards Data"""

@app.route("/ageing/ageing_receivables/cards_details", methods = ['POST'])
def get_seller_ageing_receivables_card_details():
    data=request.get_json()
    # print(data)

    seller_gstin=data.get("seller_gstin")
    try:

        # Total Receivables		Not Yet Due %		Total Overdue %		Advance / Excess Received
						
# DSO		# Invoices Not Yet Due		# Invoices Overdue		# Invoices Advance / Excess

        total_receivables,not_yet_due,total_overdue_percent,advance_excess_received,dso,no_of_invoices_not_yet_due,no_of_invoices_overdue,no_of_advance_excess=0,0,0,0,0,0,0,0
        collection_name=f"{seller_gstin}_Receivables_Summary_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ json.loads(json_util.dumps(doc)) for doc in cursor]
            for doc in json_docs:
                not_yet_due+=float(doc.get("Not Yet Due")) if doc.get("Not Yet Due")!=None else 0
                total_receivables+=float(doc.get("Total Recievables"))  if doc.get("Total Recievables")!=None else 0
                total_overdue_percent+=float(doc.get("% overdue")) if doc.get("% overdue")!=None else 0
                # no_of_invoices_not_yet_due+=float(doc.get("Not Yet Due")) if doc.get("Not Yet Due")!=None else 0
                advance_excess_received+=float(doc.get("Advance / Excess Recievables")) if doc.get("Advance / Excess Recievables")!=None else 0
                # no_of_invoices_overdue+=int(doc.get("Invoices Due")) if doc.get("Invoices Due")!=None else 0
                no_of_advance_excess+=int(doc.get("Invoices Advance / Excess"))  if doc.get("Invoices Advance / Excess")!=None else 0
                dso+=int(doc.get("DSO")) if doc.get("DSO")!=None else 0

        
            return {"status":True,
                    "seller_id": data.get("seller_code"),
                    "seller_gstin": data.get("seller_gstin"),
                    "cards_data": {
                        # "
                        "total_receivables":total_receivables,
                        "not_yet_due": not_yet_due,
                        "total_overdue_percent": round(total_overdue_percent,2),
                        "advance_excess_received":advance_excess_received,
                        "dso": dso,
                        "no_of_invoices_not_yet_due": no_of_invoices_not_yet_due,
                        "no_of_invoices_overdue": no_of_invoices_overdue

                    }
                }


        else:
            return {"status":False,
                    "seller_id": data.get("seller_code"),
                    "seller_gstin": data.get("seller_gstin"),
                    "cards_data": {
                        "total_receivables":0.0,
                        "not_yet_due": 0.0,
                        "total_overdue_percent": 0.0,
                        "overdue_percent":0.0,
                        "invoice_due": 0,
                        "adv_recieved": 0.0,
                        "adv_invoice_count": 0

                    }
                }

    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing dropdown details,Please contact system administrator"},400



"""Get api for Pie Graph"""

@app.route("/ageing/ageing_receivables/pie_graph_details", methods = ['POST'])
def get_seller_ageing_receivables_pie_graph_details():
    data=request.get_json()
    print(data)
    customer_gstin=data.get("customer_gstin")
    try:
        pie_graph_details={
            "status":True,
  "seller_id": "768",
  "data": [
    {
      "name": "1-30",
      "y": 0.0
    },
    {
      "name": "31-60",
      "y": 0.0
    },
    {
      "name": "61-90",
      "y": 0.0
    },
    {
      "name": "91-120",
      "y": 1043034.59
    },
    {
      "name": "121-180",
      "y": 0.0
    },
    {
      "name": "181-270",
      "y": 77154.1
    },
    {
      "name": "271-360",
      "y": 791298.15
    },
    {
      "name": "361-plus",
      "y": 596093.8
    }
  ]
}

        # total_receivables,not_yet_due,total_overdue,overdue_percent,invoice_due,adv_recieved,advance_invoice_count=0,0,0,0,0,0,0
        collection_name="33BACDS7654A2Z3_Receivables_Summary_Data"
        collist = db.list_collection_names()
        print(collist)
        if collection_name in collist:
            print("yes colleciton")
            collection = db[collection_name]
            cursor = collection.find({})
            print(cursor)
            for doc in cursor:
                print(doc)
                not_yet_due+=doc.get("Not Yet Due")
                total_receivables+=doc.get("Total Recievables")
                total_overdue+=doc.get("Total Overdue")
                overdue_percent+=doc.get("% overdue")
                adv_recieved+=doc.get("Advance / Excess Received")
                invoice_due+=doc.get("Invoices Due")
                advance_invoice_count+=doc.get("Invoices Advance / Excess")
                
            # return {"status":True,
            #         "seller_id": data.get("seller_code"),
            #         "seller_gstin": data.get("seller_gstin"),
            #         "cards_data": {
            #             "total_receivables":round(total_receivables,2),
            #             "not_yet_due": round(not_yet_due,2),
            #             "total_overdue": round(total_overdue,2),
            #             "overdue_percent": round(overdue_percent,2),
            #             "invoice_due": invoice_due,
            #             "adv_recieved": round(adv_recieved,2),
            #             "adv_invoice_count": advance_invoice_count

            #         }
            #     
            return pie_graph_details
        else:
            return {"status":False,
                    "seller_id": data.get("seller_code"),
                    "seller_gstin": data.get("seller_gstin"),
                    "cards_data": {
                        "total_receivables":0.0,
                        "not_yet_due": 0.0,
                        "total_overdue": 0.0,
                        "overdue_percent":0.0,
                        "invoice_due": 0,
                        "adv_recieved": 0.0,
                        "adv_invoice_count": 0

                    }
                }

    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing dropdown details,Please contact system administrator"},400




# """Get api for bar Graph"""

# @app.route("/ageing/ageing_receivables/bar_graph_details", methods = ['POST'])
# def get_seller_ageing_receivables_card_details():
#     data=request.get_json()
#     customer_gstin=data.get("customer_gstin")
#     try:
#         bar_graph_details={
#   "seller_id": "768",
#   "data": [
#     {
#       "name": "1-30",
#       "y": 0.0
#     },
#     {
#       "name": "31-60",
#       "y": 0.0
#     },
#     {
#       "name": "61-90",
#       "y": 0.0
#     },
#     {
#       "name": "91-120",
#       "y": 1043034.59
#     },
#     {
#       "name": "121-180",
#       "y": 0.0
#     },
#     {
#       "name": "181-270",
#       "y": 77154.1
#     },
#     {
#       "name": "271-360",
#       "y": 791298.15
#     },
#     {
#       "name": "361-plus",
#       "y": 596093.8
#     }
#   ]
# }

#         total_receivables,not_yet_due,total_overdue,overdue_percent,invoice_due,adv_recieved,advance_invoice_count=0,0,0,0,0,0,0
#         collection_name="33BACDS7654A2Z3_Receivables_Summary_Data"
#         collist = db.list_collection_names()
#         if collection_name in collist:
#             collection = db[collection_name]
#             cursor = collection.find({})

#             for doc in cursor:
#                 not_yet_due+=doc.get("Not Yet Due")
#                 total_receivables+=doc.get("Total Recievables")
#                 total_overdue+=doc.get("Total Overdue")
#                 overdue_percent+=doc.get("% overdue")
#                 adv_recieved+=doc.get("Advance / Excess Received")
#                 invoice_due+=doc.get("Invoices Due")
#                 advance_invoice_count+=doc.get("Invoices Advance / Excess")
                
#             return {"status":True,
#                     "seller_id": data.get("seller_code"),
#                     "seller_gstin": data.get("seller_gstin"),
#                     "cards_data": {
#                         "total_receivables":round(total_receivables,2),
#                         "not_yet_due": round(not_yet_due,2),
#                         "total_overdue": round(total_overdue,2),
#                         "overdue_percent": round(overdue_percent,2),
#                         "invoice_due": invoice_due,
#                         "adv_recieved": round(adv_recieved,2),
#                         "adv_invoice_count": advance_invoice_count

#                     }
#                 }


#         else:
#             return {"status":False,
#                     "seller_id": data.get("seller_code"),
#                     "seller_gstin": data.get("seller_gstin"),
#                     "cards_data": {
#                         "total_receivables":0.0,
#                         "not_yet_due": 0.0,
#                         "total_overdue": 0.0,
#                         "overdue_percent":0.0,
#                         "invoice_due": 0,
#                         "adv_recieved": 0.0,
#                         "adv_invoice_count": 0

#                     }
#                 }

#     except Exception as e:
#         print(str(e))
#         return {"status":False,
#                 "message":"Error in fetching seller ageing dropdown details,Please contact system administrator"},400






if __name__ == "__main__":
    app.run(debug=True)


 