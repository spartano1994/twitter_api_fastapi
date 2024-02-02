#bibliotecas de Python
from typing import List, Dict, Optional
from datetime import datetime as dt
from datetime import date as d
import json

#elementos de fastAPI
from fastapi import FastAPI, status, Query , Path, Form, Body
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
def singup( user : CompleteUser = Body( ... ) ) -> User :
    with open( "./users.json" , "r+" , encoding = "utf-8" ) as f:
        results = json.load( f ) #json.load( ) convierte un string o un archivo a un json
        user_dict = user.model_dump() #.model_dump convierte un modelo a un diccionario
        user_dict[ "user_id" ] = str( user_dict[ "user_id" ]  )
        user_dict[ "birth_date" ] = str( user_dict[ "birth_date" ]  )
        results.append( user_dict )
        f.seek( 0 ) #El método anterior agrega un elemento al final, pero .seek nos permite movernos a cualquier byte del archivo
                    #Nos movemos al primer byte para reescribir toda la lista y no crear una nueva enfrente de la primera
        f.write( json.dumps( results , indent = 2 ) )  #El parámetro indent= sirve para dar formato al json con dos espacios de identación
        return user

@app.post( path = "/login" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_200_OK , 
          summary = "Login a user" )
def login( ):
    pass

@app.get( path = "/users" , tags = [ "Users" ] , response_model = List[ User ] , status_code = status.HTTP_200_OK , 
         summary = "Show all users" )
def show_all_users(  ) -> List[ User ]:
    with open( "./users.json" , "r" , encoding = "utf-8" ) as f:
        users_list = json.load( f )
        return users_list

@app.get( path = "/users/{user_id}" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_200_OK , 
         summary = "Show a user" )
def show_a_user(  ) -> User:
    pass

@app.delete( path = "/users/{user_id}/delete" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_200_OK , 
         summary = "Delete a user" )
def delete_a_user(  ) -> JSONResponse:
    return { "User state" : "removed" }

@app.put( path = "/users/{user_id}/update" , tags = [ "Users" ] , response_model = User , status_code = status.HTTP_202_ACCEPTED , 
         summary = "Update a user" )
def update_a_user(  ) -> User :
    pass



#Tweets
@app.post( path = "/tweets/create" , tags = [ "Tweets" ] , response_model = Tweet , status_code = status.HTTP_201_CREATED , 
          summary = "Post a user" )
def create_a_tweet( tweet : Tweet = Body( ... ) ) -> Tweet :
    with open( "./tweets.json" , "r+" , encoding = "utf-8" ) as f:
        results = json.load( f )
        tweet_dict = tweet.model_dump()
        tweet_dict[ "tweet_id" ] = str( tweet_dict[ "tweet_id" ]  )
        tweet_dict[ "created_at" ] = str( tweet_dict[ "created_at" ]  )
        if tweet_dict[ "update_at" ]:
            tweet_dict[ "update_at" ] = str( tweet_dict[ "update_at" ] )

        tweet_dict[ "by" ][ "user_id" ] = str( tweet_dict[ "by" ][ "user_id" ] )
        tweet_dict[ "by" ][ "birth_date" ] = str( tweet_dict[ "by" ][ "birth_date" ] )

        results.append( tweet_dict )
        f.seek( 0 )
        f.write( json.dumps( results , indent = 2 ) )
        return tweet

@app.get( path = "/tweets" , tags = [ "Tweets" ] , response_model = List[ Tweet ] , status_code = status.HTTP_200_OK , 
         summary = "Show all tweets" )
def show_all_tweets() -> List[ Tweet ]:
    pass

@app.get( path = "/tweets/{tweet_id}" , tags = [ "Tweets" ] , response_model = Tweet , status_code = status.HTTP_200_OK , 
         summary = "Show a tweet" )
def show_a_tweet() -> Tweet:
    pass

@app.delete( path = "/tweets/{tweet_id}/delete" , tags = [ "Tweets" ] , response_model = Tweet , status_code = status.HTTP_200_OK , 
         summary = "Delete a tweet" )
def delete_a_tweet() -> JSONResponse:
    return { "Tweet_state" : "removed" }

@app.put( path = "/tweets/{tweet_id}/update" , tags = [ "Tweets" ] , response_model = Tweet , status_code = status.HTTP_202_ACCEPTED , 
         summary = "Update a tweet" )
def update_a_tweet() -> Tweet :
    pass



