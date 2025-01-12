from pydantic import BaseModel, Field, validator


class ConnectionParameters(BaseModel):
    host: str = Field(..., min_length=1, max_length=255)
    port: int = Field(..., ge=1, le=65535)
    database_name: str = Field(..., min_length=1, max_length=255)
    username: str = Field(min_length=1, max_length=255, default="username")
    password: str = Field(min_length=1, max_length=255, default="password")

    @classmethod
    @validator('host')
    def validate_host(cls, v):
        if not v:
            raise ValueError('Host cannot be empty')
        return v

    @classmethod
    @validator('database_name')
    def validate_database_name(cls, v):
        if not v:
            raise ValueError('Database name cannot be empty')
        return v
