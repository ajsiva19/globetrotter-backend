from fastapi import FastAPI
from utils.database.default_data_db  import default_data
from modals.globetrotter import Destination
from utils.config_env import ConfigEnv
from fastapi.middleware.cors import CORSMiddleware
from utils.logger_util import logger
from routes.globetrotter import globetrotter_router
from utils.database.db_connection import engine, Base, SessionLocal
app = FastAPI(
    title="globetrotter backend development",
    description="globetrotter backend development",
    root_path="/api/v1",
)

# Initialize the settings
configEnv = ConfigEnv()

# Print the settings to verify
logger.info(f"Settings Loaded: {configEnv.dict()}")

#Create tables
Base.metadata.create_all(bind=engine)
with SessionLocal() as session:
    if not session.query(Destination).first():  # Check if there are any roles in the database
        default_data(session, Destination)



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers

app.include_router(
    globetrotter_router,
    prefix="/globetrotter",
    tags=["Globetrotter"],
)

