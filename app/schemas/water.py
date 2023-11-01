from typing import Optional

from pydantic import BaseModel

from pydantic import UUID4

from .general import Response

import datetime

class Create_wEntry(BaseModel):  
    amt: int

class Edit_wEntry(BaseModel):  
    amt: int

class wEntryResponse(Response):
    email : str
    amt : int
    date: datetime.date
    time: datetime.datetime
