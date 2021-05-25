from pydantic import BaseSettings, RedisDsn, PostgresDsn  # type: ignore

# by reading from the environment(Default values used if the matching environment variable is not set.)
class Settings(BaseSettings):

    redis_dsn: RedisDsn = "redis://default:pass@localhost:6379/0"
    pg_dsn: PostgresDsn = "postgres://user:pass@localhost:5432/dev"

    pg_pool_size: int = 10
    pg_max_overflow: int = 10
    pg_pool_recycle: int = 1200
    pg_pool_pre_ping: bool = True


settings: Settings = Settings()
