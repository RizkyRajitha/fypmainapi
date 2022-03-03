import os
from fastapi.exceptions import HTTPException
from fastapi import FastAPI

from imagepro.findimage import find_image


from models import models

app = FastAPI()



@app.get("/")
async def root():

    return  {"message":"hello world"}

@app.post('/query')
async def query(img_name:models.ImageQuery):

    img_name_query = img_name.url
    print(img_name_query)

    # letimg = findimage.getDominentColor('/home/dealwithit/Documents/nemisis/favicons/zoom_us.ico')
    if img_name_query[:8] != "https://":
        raise HTTPException(status_code=400, detail="invalid format only support https")

    if img_name_query[-1:]== '/':
        img_name_query = img_name_query[:-1]

    img_query_res = find_image(img_name_query)

    print(img_query_res)


    if(img_query_res):
        # img_url = "https://"+str(img_query_res).replace('_',".")
        querydomain =  img_name_query[8:].replace('.',"_")
        print("querydomain" , querydomain)
        print("img_query_res",img_query_res)
        if(querydomain==img_query_res):
            return {"result": False}
        else:
            return {"result": True}

    else:
        raise HTTPException(status_code=404, detail="not found")



@app.on_event("startup")
async def startup_event():
    print(f"\nfavicons comparer started on port 8000\n")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    unknown_favicons_path = dir_path+'/unknownFavicons'
    # print(unknown_favicons_path)
    if not os.path.exists(unknown_favicons_path):
        os.mkdir(unknown_favicons_path)
