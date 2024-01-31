#bibliotecas de Python
from typing import List, Dict, Optional
from datetime import datetime as dt

#elementos de fastAPI
from fastapi import FastAPI, status, Query , Path, Form
from fastapi.responses import JSONResponse

#bibliotecas propias
from twitterTools.models import *

#creación de la API
app = FastAPI( title = "Twitter API" , 
              version = "0.1.0",
              description = "API funcional basada en Twitter" ,
              contact = {
    		    	"name" : "Gerardo González García" ,
    		    	"url" : "https://www.gerabytes.com/" ,
    		    	"email" : "spartano1994@hotmail.com"
    			}
)

#Test
@app.get( path = "/" , tags = [ "Home" ] , summary = "Home" , 
		description = "Este es un método para probar el funcionamiento inicial de la API" , 
        response_class = JSONResponse, status_code = status.HTTP_200_OK)
def home() -> JSONResponse:
    return { "Twitter API" , "Working!"}

#Users
@app.post( path = "/singup" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_201_CREATED , 
          summary = "Register a user" )
def singup(  ):
    pass

@app.post( path = "/login" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_200_OK , 
          summary = "Login a user" )
def login(  ):
    pass

@app.get( path = "/users" , tags = [ "Users" ] , response_model = List[User] , status_code = status.HTTP_200_OK , 
         summary = "Show all users" )
def show_all_users(  ):
    pass

@app.get( path = "/users/{user_id}" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_200_OK , 
         summary = "Show a user" )
def show_a_user(  ):
    pass

@app.delete( path = "/users/{user_id}" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_202_ACCEPTED , 
         summary = "Delete a user" )
def delete_a_user(  ):
    pass

@app.put( path = "/users/{user_id}" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_202_ACCEPTED , 
         summary = "Delete a user" )
def update(  ):
    pass




