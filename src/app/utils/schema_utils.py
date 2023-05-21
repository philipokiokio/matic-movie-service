from pydantic import BaseModel, BaseSettings


class AbstractModel(BaseModel):
    class Config:
        orm_mode = True


class ResponseModel(AbstractModel):
    message: str
    status: int


class AbstractSetting(BaseSettings):
    class Config:
        env_file = ".env"
