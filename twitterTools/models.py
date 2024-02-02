from uuid import UUID, uuid4  #uuid4 genera un id aleatorio de la clase UUID
from typing import Optional
from datetime import datetime as dt
from datetime import date as d

from pydantic import BaseModel, EmailStr, Field

#User model
class UserBase( BaseModel ):
    user_id : UUID = Field( ... , default_factory = uuid4 )
    email : EmailStr = Field( ... )

class UserLogin( UserBase ):
    password : str = Field( ... , min_length = 8 , max_length = 15 )
    
class User( UserBase ):
    first_name : str = Field( ... , min_length = 1 , max_length = 50 )
    last_name : str = Field( ... , min_length = 1 , max_length = 50 )
    birth_date : Optional[ d ] = Field( default = d.today )

class CompleteUser( User , UserLogin ):
    pass



#Tweet model
class Tweet( BaseModel ):
    tweet_id : UUID = Field( ... , default_factory = uuid4 )
    content : str = Field( ... , min_length = 1 , max_length = 280 )
    created_at : dt = Field( default = dt.now() )
    update_at : Optional[ dt ] = Field( default = None )
    by : User = Field( ... )