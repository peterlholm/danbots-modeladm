"Training Model client"
import requests

MODEL_SERVER_URL = "http://traindb.danbots.com/"
API = "api/save"
URL = MODEL_SERVER_URL + API

_DEBUG = False

def save_training_result(paramlist):
    resp = requests.post(URL, json=paramlist )
    if not resp.ok:
        print("API call went wrong", resp.status_code)
        print (resp.text)
        return False
    if _DEBUG:
        print(resp.text)
        print (resp)
    return True

# eksempel

if __name__ == "__main__":
    myparamlist = {"model1": "mymodel1", "model2": "mymodel2"}
    result = save_training_result(myparamlist)
    if not result:
        print("saving training data went wrong")
