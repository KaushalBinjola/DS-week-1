from fastapi import FastAPI, Path
from typing import Optional

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

