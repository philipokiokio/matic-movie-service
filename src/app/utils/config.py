from src.app.utils.schema_utils import AbstractSetting


class DBSettings(AbstractSetting):
    db_name: str
    db_username: str
    db_password: str
    db_port: int
    db_host: str


class SWSettings(AbstractSetting):
    base_url: str


db_settings = DBSettings()
sw_settings = SWSettings()
