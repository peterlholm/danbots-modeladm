#!/bin/python3

"RunQueue job"
import os
from time import sleep
import subprocess
import requests


API_KEY = 'ad666b87-3b17-427f-bd11-24f1fa9b9bb2'
SERVER_URL = "http://traindb.danbots.com/"
API = "runqueue/"
HOST='sal5'
CHECKTIME = 10

_DEBUG = True

if _DEBUG:
    SERVER_URL = "http://localhost:8000/"
URL = SERVER_URL + API

def get_next_job(hostname):
    url = URL + "jobnext?host="+ hostname + "&apikey=" + API_KEY
    resp = requests.get(url)
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        return None
    # if _DEBUG:
    #print(resp.text)
    #     print (resp)
    return resp.json()

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

def send_status(jobid, status, result=None):
    #paramlist['api-key'] = API_KEY
    url = URL + "jobstatus?id="+ str(jobid) + "&status=" + str(status)
    if result is not None:
        url += "&result=" + str(result)
    resp = requests.get(url)
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        print (resp.text)
        return False
    if _DEBUG:
        print(resp.text)
        print (resp)
    return True

def run_job(command):
    rescall = os.system(command)
    print("result", rescall)
    return rescall

def run_sub(command):
    print ("Command:", command)
    procres = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, check=False )
    print ("Returncode", procres.returncode)
    print(procres)
    return procres.returncode

if __name__ == "__main__":
    # job = get_next_job("sal5")
    # print("NextJob", job)

    #res = run_sub('dir')
    if _DEBUG:
        print("Starting")
    running = True
    while running:
        job = get_next_job(HOST)
        if job and 'jobid' in job:
            print(job)
            jobid = job['jobid']
            command = job['command']
            if _DEBUG:
                #print (job)
                print (jobid, command)
            send_status(jobid, 1)
            jobreturn = run_sub(command)
            if jobreturn == 0:
                send_status(jobid, 2, 0)
            else:
                send_status(jobid, 3, jobreturn)
        else:
            print('No Jobs')
        sleep(CHECKTIME)



    # print ("slutresult", res)
    