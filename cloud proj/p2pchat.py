from fastapi import FastAPI, Body #, get, post
from requests import Request
import logging


'''
Nicholas Mooney
2/8/2022
In class lab for p2p chat program
'''
app = FastAPI()

@app.get("/")
async def root():
 return {"message": "Hello World"}

@app.get("/help")
async def root():
 return {"message": "idk man"}

@app.post("/send/")
async def update_item(
 payload: dict = Body(...)
):
 return payload

#@app.post("/receive")
#async def root(request):
# return {"message": "idk man"}


#class Item(BaseModel):
# name: str
# description: Optional[str] = None

#@app.post("/items/")
#async def create_item(item: Item):
# return item

















