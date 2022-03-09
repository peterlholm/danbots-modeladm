#!/bin/python3
"RunQueue job"
import os
import requests

API_KEY = 'ad666b87-3b17-427f-bd11-24f1fa9b9bb2'
SERVER_URL = "http://traindb.danbots.com/"
API = "runqueue/"

_DEBUG = True

if _DEBUG:
    SERVER_URL = "http://localhost:8000/"
URL = SERVER_URL + API

def get_next_job(hostname):
    url = URL + "jobnext?host="+ hostname
    paramlist = {}
    paramlist['api-key'] = API_KEY
    print (url)
    #resp = requests.post(url, json=paramlist )
    resp = requests.get(url)
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        #print (resp.text)
        return False
    if _DEBUG:
        print(resp.text)
        print (resp)
    return True

def send_result(paramlist):
    paramlist['api-key'] = API_KEY
    resp = requests.post(URL, json=paramlist )
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        print (resp.text)
        return False
    if _DEBUG:
        print(resp.text)
        print (resp)
    return True

def run_job(command):
    
    res = os.system(command)
    print("result", res)
    return res
    
if __name__ == "__main__":
    # job = get_next_job("sal5")
    # print("NextJob", job)

    res = run_job('dir')
    print ("slutresult", res)
    