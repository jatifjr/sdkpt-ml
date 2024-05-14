from typing import Any, Optional, List

from pydantic import BaseModel


class CasesResponse(BaseModel):
    jumlah_kasus: int
