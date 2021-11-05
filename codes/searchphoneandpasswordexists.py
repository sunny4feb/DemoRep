from flask import Flask
from elasticsearch import Elasticsearch

def phoneandpasswordexists(email, password):
    es = Elasticsearch()
    e2 ={
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "phone.keyword" : email
                            }
                            },
                            {
                                "match": {
                                    "password.keyword": password
                                    }
                                    }
                                    ]
                                    }
                                    }
                                    }
    resp = es.search(index = 'emps', body = e2)
    hits = resp["hits"]["hits"]
    if  hits:
        for hit in hits:
            print(hits)
            source = hit['_source']
            return source
            signinname = source['Username']
            signinemail = source['email_id']
            signinphone = source['phone']
            # print(signinname)
            # print(signinemail)
            # print(signinphone)
        # return True
            
    else:
        False