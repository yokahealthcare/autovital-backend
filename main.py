from fastapi import FastAPI

import db_user as db
from schemas import sch_user as schemas
import car

app = FastAPI()
app.include_router(car.router)


@app.post("/signup_account")
async def create_account(request: schemas.SignupPayload):
    data = [
        request.signup_account.username,
        request.signup_account.password,
        request.signup_account.phone,
        request.signup_account.email
    ]

    operation = db.signup(data=data)
    if operation['is_success']:
        # 'res' will be sent to android studio
        res = {
            "is_success": True,
            "info": f"Account '{request.signup_account.username}' added to database.",
            "detail": f"{operation['info']}"
        }
        return res
    else:
        # 'res' will be sent to android studio
        res = {
            "is_success": False,
            "info": f"Account '{request.signup_account.username}' failed to be added database.",
            "detail": f"{operation['info']}"
        }
        return res


@app.get("/account/verified")
async def verified_account(uid: str):
    operation = db.verified_account(uid)
    if operation['is_success']:
        res = {
            "is_success": True,
            "info": f"Account verification process successful. Login to your account",
            "detail": f"{operation['info']}"
        }
        return res['info']
    else:
        res = {
            "is_success": False,
            "info": f"Account verification process failed",
            "detail": f"{operation['info']}"
        }
        return res['info']


@app.post("/login_account")
async def login_account(request: schemas.LoginPayload):
    data = [
        request.login_account.username,
        request.login_account.password,
    ]

    operation = db.login(data=data)
    if operation['is_success']:
        res = {
            "is_success": True,
            "info": f"Account login operation successful",
            "detail": f"{operation['info']}",
            "data": operation['data']
        }
        return res
    else:
        res = {
            "is_success": False,
            "info": f"Account login operation failed",
            "detail": f"{operation['info']}"
        }
        return res

