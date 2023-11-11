from fastapi import APIRouter
import db_car as db
from schemas import sch_car as schemas

# define new route for included to main route
router = APIRouter(
    prefix="/car"
)


@router.post("/add")
async def add_car(request: schemas.AddCar):
    # converted to dictionary
    dt_car = {
        "name": request.name,
        "plate": request.plate,
        "vin": request.vin,
        "distance": request.distance,
        "cid": request.cid,
        "data": request.data
    }
    # make request to database
    operation = db.add_car(ncar=dt_car)

    if operation['is_success']:
        res = {
            "is_success": True,
            "info": f"New car has been added succesfully",
            "detail": f"{operation['info']}",
        }
        return res
    else:
        res = {
            "is_success": False,
            "info": f"Account login operation failed",
            "detail": f"{operation['info']}"
        }
        return res


@router.get("/list_all_car")
async def list_all_car():
    return db.list_all_car()


@router.get("/load")
async def load_car(automotive_id: str):
    # make request to database
    operation = db.load_car(automotive_id)

    if operation['is_success']:
        res = {
            "is_success": True,
            "info": f"Selected car is successfully loaded",
            "detail": f"{operation['info']}",
            "data": operation['data']
        }
        return res
    else:
        res = {
            "is_success": False,
            "info": f"Selected car failed to load",
            "detail": f"{operation['info']}"
        }
        return res


@router.post("/save_edited_car")
async def edit_car():
    pass


@router.post("/delete")
async def delete_car():
    pass
