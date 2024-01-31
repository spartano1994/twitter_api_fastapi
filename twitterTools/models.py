from uuid import UUID
from typing import Optional
from datetime import datetime as dt

from pydantic import BaseModel, EmailStr, Field

class UserBase( BaseModel ):
    uder_id : UUID = Field( ... )
    email : EmailStr = Field( ... )

class UserLogin( UserBase ):
    password : str = Field( ... , min_length = 8 , max_length = 15 )
    
class User( UserBase ):
    first_name : str = Field( ... , min_length = 1 , max_length = 50 )
    last_name : str = Field( ... , min_length = 1 , max_length = 50 )
    birth_date : Optional[ dt ] = Field( default = None )




class Twitter( BaseModel ):
    tweet_id : UUID = Field( ... )
    content : str = Field( ... , min_length = 1 , max_length = 280 )
    created_at : dt = Field( default = dt.now() )
    update_at : Optional[ dt ] = Field( default = None )
    by : User = Field( ... )