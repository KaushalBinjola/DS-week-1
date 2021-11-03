from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from fastapi.param_functions import Query
from pydantic import BaseModel

app = FastAPI()

multiParams = {
    1: {
        "Data": "One"
    },
    2: {
        "Data": "Two"
    }
}

@app.get("/")
def home():
    return {"Data":"Test"}

@app.get("/ok")
def ok():
    return {"OK":"OK"}

@app.get("/multi_params/{test_id}")
def multi_params(test_id: int = Path(None, description="Describes this endpoint, Fisrt argument is the default value given, Can be seen in docs. GT is basically grater than and all",gt=0)):
    return multiParams[test_id]


# We use Optional below because that is recommended. Just giving default value will also make it optional. 
# When setting up optional params, in the function either use optional params at last or give functions first argument as *. 
# FastAPI doesnt need to follow any sequence, it can figure by itself.
@app.get("/qParams")
def qParamsw(dataVal: Optional[str] = None):
    for i in multiParams:
        if multiParams[i]["Data"] == dataVal:
            return multiParams[i]
    return {"Data":"Null"}


#post

# create class that defines the body of post
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    
@app.post("/post-ex")
def postExample(item: Item):
    return "OK!"


# put
# used to update instances 

@app.put('updateMultiParams/{id}')
def updateMulti(id:int, data:str):
    if id not in multi_params:
        return {"Error":"Not found"}
    multi_params[id].data = data
    return multi_params[id]

# delete 
# used to delete instance

@app.delete('deleteFromMulti')
def deleteMulti(id: Optional[int]=Query(None,title="Enter Query Param")):
    if id not in multi_params:
        return {"Error":"Not found"}
    del multi_params[id]
    return {"success":"true"}


# raise status errors
@app.get('updateMultiParams/{id}')
def updateMulti(id:int):
    if id not in multi_params:
        raise HTTPException(status_code=404, detail="Id not found")
    # multi_params[id].data = data
    return multi_params[id]
    
