from fastapi import APIRouter, HTTPException, Security
from app.models.water import WaterEntries
from app.schemas.water import Create_wEntry, Edit_wEntry, wEntryResponse
from app.models.user import UserAccount
from app.services.auth.utils import get_current_user
from datetime import date,datetime

from app.utils.response import responses
from app.utils.exception import ShapeShyftException

router = APIRouter(
    tags=["Health profile"],
)

@router.post("/createWater", response_model=wEntryResponse,responses=responses)
async def create_water(data: Create_wEntry, current_user: UserAccount = Security(get_current_user)):
    data = data.dict()
    water = await WaterEntries.create(
        **data,
        email=current_user.email,
        date=date.today()
    )
    return water
    

@router.get("/getWater", response_model=wEntryResponse, responses=responses)
async def get_water(current_user: UserAccount = Security(get_current_user)):
    waterLog = await WaterEntries.get(email=current_user.email)
    return waterLog 

@router.put("/updateWater", response_model=wEntryResponse, responses=responses)
async def update_water_amt(data : int, current_user: UserAccount = Security(get_current_user)):
    hydration_log = await WaterEntries.get(email=current_user.email)
    hydration_log.amt = data
    await hydration_log.save()

    return hydration_log