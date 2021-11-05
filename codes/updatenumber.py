from flask import Flask, render_template, request, session
from elasticsearch import Elasticsearch

def updatenumbers():
    if request.method == 'GET':
        return render_template('updatenumber.html')
    else:
        name = request.form["name"]
        password = request.form["password"]
        phone = request.form["phone"]
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
                                        "password.keyword": password
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
                                        "password.keyword": password
                                        }
                                }
                                ]
                                }
                            },
                            "script" : {
                                "source": "ctx._source.phone=params.tag",
                                "lang": "painless",
                                "params": {
                                    "tag" : phone
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
            error = "Invalid Username/Password"
            return error

        # es = Elasticsearch(hosts="http://elastic:4586929688@localhost:9200/")
        # e5 ={
        #     "query": {
        #         "bool": {
        #             "must": [
        #                 {
        #                     "match": {
        #                         "Username.keyword" : name
        #                         }
        #                         },
        #                         {
        #                             "match": {
        #                                 "password.keyword": password
        #                             }
        #                         }
        #                     ]
        #                 }
        #             }
        #     }
                                        
        # resp = es.search(index = 'emps', body = e5)
        # hits = resp["hits"]["hits"]
        # if hits:
        #     try:
        #         es = Elasticsearch(hosts="http://elastic:4586929688@localhost:9200/")
        #         e9 = {
        #             "script" : {
        #                 "source": "ctx._source.phone=params.tag",
        #                 "lang": "painless",
        #                 "params": {
        #                     "tag" : phone
        #                     }
        #                     }
        #         }
        #         es.update_by_query(index = "emps", doc_type = 'detail', body = e9)
        #     except Exception as e:
        #         pass
        #     finally:
        #         return '''Hi {}, You have Successfully changed your number !!,
        #         Please <a href="http://localhost:5050/">click here </a> to LogIn'''.format(name)
            
        # else:
        #     error = "Invalid Username/Password"
        #     return error
            