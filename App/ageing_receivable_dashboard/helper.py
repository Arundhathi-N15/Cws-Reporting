from flask import Flask
from flask import request
from pymongo import MongoClient
import json
from bson import json_util
import datetime


client = MongoClient("mongodb+srv://db_admin:VO0usJYgofYmc6is@cluster0.lnt3z.mongodb.net/?retryWrites=true&w=majority")
db = client.test

app = Flask(__name__)

@app.route("/add_seller_ageing_bucket_details", methods = ['POST'])
def add_seller_ageing_bucket_details():
    """function to generate zoho access token from grant code

    Args:
        client_id (str): client id
        client_secret (str): client spassword
        redirect_uri (str): the data gets redirected to this url
        code (str): grant code
    """
    data=request.get_json()
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
    seller_gstin=data.get("seller_gstin")
    try:
        collection_name=f"{seller_gstin}_Receivables_Summary_Data"
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
    seller_gstin=data.get("seller_gstin")

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
    try:
        collection_name=f"{seller_gstin}_Receivables_Customer_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ doc for doc in cursor] 
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
    seller_gstin=data.get("seller_gstin")
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
        collection_name=f"{seller_gstin}_Receivables_Customer_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ doc for doc in cursor] 
            return {"status":True,
                "data":json_docs},200
        else:
            return {"status":False,"data":[]},200

    
        
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Please contact system administrator"},400




@app.route("/ageing/ageingInvoiceDetails", methods = ['POST'])
def get_seller_ageing_invoice_details():
    data=request.get_json()
    seller_gstin=data.get("seller_gstin")
    try:
       
        collection_name=f"{seller_gstin}_Receivables_InvoiceData"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ json.loads(json_util.dumps(doc)) for doc in cursor]
            return {"status":True,
                "data":json_docs},200
        else :  
            return {"status":True,
                "message":"No records found","data":[]},200
    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing receivables invoice details,Please contact system administrator"},400



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
                no_of_invoices_not_yet_due+=float(doc.get("Not Yet Due")) if doc.get("Not Yet Due")!=None else 0
                advance_excess_received+=float(doc.get("Advance / Excess Recievables")) if doc.get("Advance / Excess Recievables")!=None else 0
                no_of_invoices_overdue+=int(doc.get("Invoices Due")) if doc.get("Invoices Due")!=None else 0
                no_of_advance_excess+=int(doc.get("Invoices Advance / Excess"))  if doc.get("Invoices Advance / Excess")!=None else 0
                dso+=int(doc.get("DSO")) if doc.get("DSO")!=None else 0

        
            return {"status":True,
                    "seller_id": data.get("seller_code"),
                    "seller_gstin": data.get("seller_gstin"),
                    "cards_data": {
                        "total_receivables":total_receivables,
                        "not_yet_due": not_yet_due,
                        "total_overdue_percent": round(total_overdue_percent,2),
                        "advance_excess_received":advance_excess_received,
                        "dso": dso,
                        "no_of_invoices_not_yet_due": no_of_invoices_not_yet_due,
                        "no_of_invoices_overdue": no_of_invoices_overdue,
                        "no_of_advance_excess":no_of_advance_excess
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
                        "advance_excess_received":0.0,
                        "dso": 0.0,
                        "no_of_invoices_not_yet_due": 0,
                        "no_of_invoices_overdue": 0,
                        "no_of_advance_excess":0
                    }
                }

    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing cards details,Please contact system administrator"},400



"""Get api for Pie Graph"""

@app.route("/ageing/ageing_receivables/pie_graph_details", methods = ['POST'])
def get_seller_ageing_receivables_pie_graph_details():
    data=request.get_json()
    # print(data)
    try:
        pie_graph_data_list=[]
        seller_gstin=data.get("seller_gstin")
        # try:
        # collection_name=f"{seller_gstin}_Receivables_Summary_Data"
        collection_name="33BACDS7654A2Z3_Receivables_Summary_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            import datetime
            startdate = datetime.datetime(int(data.get("as_of_date").split("-")[0]), int(data.get("as_of_date").split("-")[1]), int(data.get("as_of_date").split("-")[2]))
            
            for document in list(collection.find({'As of Date': {'$gt': startdate}})):
                if str(document.get('As of Date')).split(" ")[0]==data.get("as_of_date"):
                    print(str(document.get('As of Date')).split(" ")[0])
                    print(document.get('Ageing Bucket'))
                    print(document.get('Total Recievables'))
                    payload={"ageing_bucket_name":document.get('Ageing Bucket'),
                            "total_receivable_amount":document.get('Total Recievables')}
                    print("payload",payload)
                    pie_graph_data_list.append(payload)
            return {"status":True,"seller_id":data.get("seller_code"),"seller_gstin":data.get("seller_gstin"),"pie_graph_data":pie_graph_data_list}
        else:
            return {"status":False,"seller_id":data.get("seller_code"),"seller_gstin":data.get("seller_gstin"),"pie_graph_data":[]}


    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing pie graph details,Please contact system administrator"},400


"""Get sub pie graph details"""
@app.route("/ageing/ageing_receivables/sub_pie_graph_details", methods = ['POST'])
def get_seller_ageing_receivables_sub_pie_graph_details():
    data=request.get_json()
    try:
        pie_graph_data_list=[]
        seller_gstin=data.get("seller_gstin")
        # collection_name=f"{seller_gstin}_Receivables_InvoiceData"
        collection_name="33BACDS7654A2Z3_Receivables_InvoiceData"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
         
            startdate = datetime.datetime(int(data.get("as_of_date").split("-")[0]), int(data.get("as_of_date").split("-")[1]), int(data.get("as_of_date").split("-")[2]))
            documents=[]
            for document in list(collection.find({'As of Date': {'$gt': startdate}})):
                
                if str(document.get('As of Date')).split(" ")[0]==data.get("as_of_date"):
                    if document.get("Ageing Bucket")==data.get("seller_ageing_receivable_bucket_name"):
                        payload={"customer_name":document.get('Customer Name'),
                            "total_receivable_amount":document.get('Amount Outstanding')}
                        documents.append(payload)
            return {"status":True,"seller_id":data.get("seller_code"),"seller_gstin":data.get("seller_gstin"),"sub_pie_graph_data":documents}
        else:
            return {"status":False,"seller_id":data.get("seller_code"),"seller_gstin":data.get("seller_gstin"),"sub_pie_graph_data":[]}


    except Exception as e:
        print(str(e))
        return {"status":False,
                "message":"Error in fetching seller ageing pie graph details,Please contact system administrator"},400



"""Get api for bar Graph"""

@app.route("/ageing/ageing_receivables/bar_graph_details", methods = ['POST'])
def get_seller_ageing_receivables_bar_graph_details():
    data=request.get_json()
    seller_gstin=data.get("seller_gstin")
    try:
        collection_name=f"{seller_gstin}_Receivables_Summary_Data"
        collist = db.list_collection_names()
        if collection_name in collist:
            collection = db[collection_name]
            cursor = collection.find({})
            json_docs = [ doc for doc in cursor]
            ageing_bucket_data_for_bar_graph=[]
            for summary_record in json_docs:
                payload={"customer_manager":summary_record.get("Ageing Bucket"),"customer_name":summary_record.get(""),
                "total_receivables":summary_record.get("Total Recievables")
                }
                ageing_bucket_data_for_bar_graph.append(payload)
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






if __name__ == "__main__":
    app.run(debug=True)


 