"Simulation db client"
import requests

API_KEY = 'ad666b87-3b17-427f-bd11-24f1fa9b9bb2'
MODEL_SERVER_URL = "http://traindb.danbots.com/"
API = "api/savesim"

_DEBUG = False

if _DEBUG:
    MODEL_SERVER_URL = "http://localhost:8000/"
URL = MODEL_SERVER_URL + API

def save_simulation_result(paramlist):
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

# eksempel

if __name__ == "__main__":
    myparamlist = {"description": "API test", "simulation_path": "/abc/api/path"}
    result = save_simulation_result(myparamlist)
    if not result:
        print("saving simulation data went wrong")
