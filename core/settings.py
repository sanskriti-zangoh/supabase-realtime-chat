# ---INFO-----------------------------------------------------------------------
"""
Settings Module.
"""

# ---DEPENDENCIES---------------------------------------------------------------
from functools import lru_cache
from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError, AnyHttpUrl


# ---CODE-----------------------------------------------------------------------
class DatabaseSettings(BaseSettings):
    """
    Database settings class.

    Attributes:
        url (str): Database URL.
        pool_size (int): Connection pool size.
        max_overflow (int): Max overflow.
        echo (bool): If True, print SQL statements. For debugging.
        pool_pre_ping (bool): If True, ping the database before each query.
        pool_recycle (int): Connection pool recycle time in seconds.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="DB_", case_sensitive=False
    )
    url: str = "sqlite+aiosqlite:///:memory:"
    pool_size: int = 8
    max_overflow: int = 16
    echo: bool = False
    pool_pre_ping: bool = False
    pool_recycle: int = 3600

class SupabaseSettings(BaseSettings):
    """
    Firebase settings class.

    Attributes:
        api_key (str): Firebase API key.
        project_id (str): Firebase project ID.
        storage_bucket (str): Firebase storage bucket.
        messaging_sender_id (str): Firebase messaging sender ID.
        app_id (str): Firebase app ID.
        measurement_id (str): Firebase measurement ID.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="SUPA_", case_sensitive=False
    )
    url : str
    api : str


@lru_cache
def load_settings(settings_cls_name: str) -> BaseSettings:
    """
    Load settings.

    Args:
        settings_cls_name (str): Settings class name.

    Returns:
        BaseSettings: Settings class.
    """
    load_dotenv(find_dotenv())
    settings_cls = globals()[settings_cls_name]
    return settings_cls()
