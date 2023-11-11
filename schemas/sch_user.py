from pydantic import BaseModel


# payloads structure

class SignupAccount(BaseModel):
    username: str
    password: str
    phone: str
    email: str


class LoginAccount(BaseModel):
    username: str
    password: str


# payloads

class SignupPayload(BaseModel):
    signup_account: SignupAccount


class LoginPayload(BaseModel):
    login_account: LoginAccount
