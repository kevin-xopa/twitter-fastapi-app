from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id : UUID = Field(...)
    email : EmailStr = Field(...)


class User(UserBase):
    first_name : str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name : str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional( date) = Field(
        default=None,
    )

class UserLogin(UserBase):
    password : str = Field(
        ...,
        min_length=8,
        max_length=64
    )
class Tweet(BaseModel):
    tweet_id : UUID = Field(...),
    content : str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    created_at : datetime = Field(
        default=datetime.now(),
    )
    updated_at : Optional[datetime] = Field(default=None)
    by: User= Field(...)



@app.get(
    path='/'
)
def home():
    return {
        "Twitter API" : "Working!"
    }

## Users
@app.post(
    path='/register',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register User',
    tags=["User"]
)
def signup():
    pass


@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=["User"]
)
def login():
    pass

@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=["User"]
)
def show_all_users():
    pass


@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a user',
    tags=["User"]
)
def show_a_user():
    pass


@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a user',
    tags=["User"]
)
def delete_user():
    pass

@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=["User"]
)
def update_user():
    pass

## Tweets
