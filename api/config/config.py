from pydantic import BaseSettings
from enum import Enum

class Profile(str, Enum):
    STAGING = "staging"

class ProfileSetting(BaseSettings):
    profile: Profile

    def get_settings(self):
        return Settings(_env_file="api/environments/.env" + "." + self.profile.lower())

    class Config:
        # env_file = "../.env"
        env_file = "app/environments/.env"
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    APP_NAME: str
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"


def get_settings():
    profile = ProfileSetting()
    return profile.get_settings()