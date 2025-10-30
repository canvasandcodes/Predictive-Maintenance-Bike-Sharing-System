"""
Main FastAPI application for Predictive Maintenance Bike Sharing System
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .core.config import settings
from .core.database import Base, engine
from .api.routes import bikes, rides, maintenance, predictions, telemetry, routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚴 Starting Predictive Maintenance System...")
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    print("🔧 Shutting down gracefully...")


app = FastAPI(
    title="Predictive Maintenance for Bike Sharing",
    description="ML-powered predictive maintenance system for bike sharing fleets",
    version="1.0.0",
    lifespan=lifespan
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(bikes.router, prefix=f"{settings.API_V1_STR}/bikes", tags=["bikes"])
app.include_router(rides.router, prefix=f"{settings.API_V1_STR}/rides", tags=["rides"])
app.include_router(maintenance.router, prefix=f"{settings.API_V1_STR}/maintenance", tags=["maintenance"])
app.include_router(predictions.router, prefix=f"{settings.API_V1_STR}/predictions", tags=["predictions"])
app.include_router(telemetry.router, prefix=f"{settings.API_V1_STR}/telemetry", tags=["telemetry"])
app.include_router(routes.router, prefix=f"{settings.API_V1_STR}/routes", tags=["route-optimization"])


@app.get("/")
async def root():
    return {
        "message": "🚴 Predictive Maintenance for Bike Sharing Systems API",
        "version": "1.0.0", 
        "status": "running",
        "features": [
            "ML-powered failure prediction",
            "Route optimization",
            "Real-time telemetry",
            "Fleet management"
        ]
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "bike-maintenance-api"}
