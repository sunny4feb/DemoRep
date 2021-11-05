import elasticsearch
from flask import Flask, request, redirect, render_template
from elasticsearch import Elasticsearch

def updatepasswords():
    if request.method == 'GET':
        return render_template('updatepassword.html')
    else:
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        print("Read the data")
        es = Elasticsearch()
        e5 ={
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "Username.keyword" : name
                                }
                                },
                                {
                                    "match": {
                                        "email_id.keyword": email
                                        }
                                }
                            ]
                        }
                    }
        }
        resp = es.search(index = 'emps', body = e5)
        hits = resp["hits"]["hits"]
        if hits:
            try:

                es = Elasticsearch()
                e1  ={
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "match": {
                                        "Username.keyword" :name
                                        }
                                },
                                {
                                    "match": {
                                        "email_id.keyword": email
                                        
                                        }
                                }
                                ]
                                }
                            },
                            "script" : {
                                "source": "ctx._source.password=params.tag",
                                "lang": "painless",
                                "params": {
                                    "tag" : password
                                    }
                                    }
                                    }
                es.update_by_query(index = "emps", doc_type = 'detail', body = e1)
            except Exception as e:
                pass
            finally:
                return '''Hi {}, You have Successfully changed your number !!,
                Please <a href="http://localhost:5050/">click here </a> to LogIn'''.format(name)
            
        else:
            error = "Invalid Username/Phone"
            return error
    #                                     "script" : {
    #                                         "source": "ctx._source.password=params.tag",
    #                                         "lang": "painless",
    #                                         "params": {
    #                                             "tag" : password
    #                                         }
    #                                         }
    #     }
    #     es.update_by_query(index = "emps", doc_type = 'detail', body = e5)
    #     print("data Updated")
    #     return '''Hi {}, You have Successfully updated your password !!,
    # Please <a href="http://localhost:5050/">click here </a> to LogIn'''.format(name)

        