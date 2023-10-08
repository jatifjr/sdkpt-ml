import os
import dotenv
from pydantic import BaseConfig, AnyHttpUrl, HttpUrl, MySQLDsn, validator
from typing import Any, Dict, List, Optional, Union

dotenv.load_dotenv()


class Settings(BaseConfig):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    API_V1_STR: str = "/api/v1"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.getenv("BACKEND_CORS_ORIGINS")

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB: str = os.getenv("MYSQL_DB")
    SQLALCHEMY_DATABASE_URI: Optional[MySQLDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return MySQLDsn.build(
            scheme="mysql",
            user=values.get("MYSQL_USER"),
            password=values.get("MYSQL_PASSWORD"),
            host=values.get("MYSQL_SERVER"),
            path=f"/{values.get('MYSQL_DB') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
