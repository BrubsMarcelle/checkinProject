from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from bson import ObjectId
from pydantic import BaseModel, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema, core_schema

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls.validate, handler(str))

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return handler(core_schema)

class User(BaseModel):
    id: Optional[PyObjectId] = None
    username: str
    email: EmailStr
    password: str

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}

class CheckIn(BaseModel):
    user_id: PyObjectId
    timestamp: datetime
    date: str  # Format: DD/MM/YY

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}

class Ranking(BaseModel):
    user_id: PyObjectId
    score: int

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}