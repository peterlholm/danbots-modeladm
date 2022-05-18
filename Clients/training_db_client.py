"Training Model client"
import requests

API_KEY = 'ad666b87-3b17-427f-bd11-24f1fa9b9bb2'
MODEL_SERVER_URL = "http://traindb.danbots.com/"

_DEBUG = False

if _DEBUG:
    MODEL_SERVER_URL = "http://localhost:8000/"
SaveAPI = MODEL_SERVER_URL + "api/savetrain"
LogAPI = MODEL_SERVER_URL + "api/trainlog"


def save_training_result(paramlist):
    paramlist['api-key'] = API_KEY
    resp = requests.post(SaveAPI, json=paramlist )
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        print (resp.text)
        return False
    if _DEBUG:
        print(resp.text)
        #print (resp)
    return int(resp.text)

def update_training_result(jobno, paramlist):
    paramlist['api-key'] = API_KEY
    paramlist['jobno'] = jobno
    resp = requests.post(SaveAPI, json=paramlist )
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        print (resp.text)
        return False
    if _DEBUG:
        print(resp.text)
        #print (resp)
    return int(resp.text)

def update_training_log(jobno, text):
    paramlist = {}
    paramlist['api-key'] = API_KEY
    paramlist['jobno'] = jobno
    paramlist['text'] = text
    resp = requests.post(LogAPI, json=paramlist )
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        #print (resp.text)
        return False
    if _DEBUG:
        print(resp.text)
        #print (resp)
    return True


# eksempel

if __name__ == "__main__":
    myparamlist = {"description": "mymodel1", "model2": "mymodel2", 'epochs': 33}
    result = save_training_result(myparamlist)
    if not result:
        print("saving training data went wrong")
    else:
        print("jobnr: ", result)
        jobno = result

    mytext = "Dette er første linie\n og her kommer nr 2\n"
    
    result = update_training_log(jobno, mytext)
    if not result:
        print("saving logdata went wrong")
    else:
        print("result: ", result)
