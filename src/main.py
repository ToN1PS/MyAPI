from fastapi import FastAPI
from src.auth.router import router as auth_router
from src.post.router import router as post_router 

app = FastAPI(title="My App")

app.include_router(auth_router)
app.include_router(post_router)


# sqlalchemy.url = postgresql+asyncpg://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s?async_fallback=True
# from alembic import context

# import sys
# import os

# sys.path.append(os.path.join(sys.path[0], 'src'))

# from src.config import DB_HOST, DB_USER, DB_NAME, DB_PASS, DB_PORT
# from src.auth.models import metadata as metadata_auth
# from src.post.models import metadata as metadata_post
# from src.likesreaction.models import metadata as metadata_likesreaction


# # this is the Alembic Config object, which provides
# # access to the values within the .ini file in use.
# config = context.config

# section = config.config_ini_section
# config.set_section_option(section, "DB_HOST", DB_HOST)
# config.set_section_option(section, "DB_PORT", DB_PORT)
# config.set_section_option(section, "DB_USER", DB_USER)
# config.set_section_option(section, "DB_PASS", DB_PASS)
# config.set_section_option(section, "DB_NAME", DB_NAME)


# target_metadata = [metadata_auth, metadata_post, metadata_likesreaction]

# script_location = migrations