# 📁 Project Structure - Predictive Maintenance Bike Sharing System

## Overview
This document explains the complete project structure and what each component does.

## 🏗️ Root Directory

```
COMPLETE_Predictive_Maintenance_Bike_Sharing_System/
├── README.md                          # Main documentation (start here!)
├── .env.template                      # Environment configuration template
├── .gitignore                        # Git ignore rules
├── docker-compose.yml                # Multi-service Docker setup
├── setup.sh                         # Automated setup script
├── PROJECT_STRUCTURE.md              # This file
└── LIVE_DEMO/                        # Working demo you can try
    └── demo_launcher.html            # Opens the live demo
```

## 🔧 Backend Directory (`backend/`)

### Core Application (`backend/app/`)
```
backend/app/
├── main.py                           # FastAPI application entry point
├── __init__.py                       # Package initialization
├── core/                            # Core configuration and database
│   ├── config.py                    # Application settings
│   ├── database.py                  # Database connections (PostgreSQL + InfluxDB)
│   └── __init__.py
├── api/                             # REST API endpoints
│   ├── routes/                      # API route definitions
│   │   ├── bikes.py                 # Bike management endpoints
│   │   ├── rides.py                 # Ride tracking endpoints
│   │   ├── maintenance.py           # Maintenance record endpoints
│   │   ├── predictions.py           # ML prediction endpoints
│   │   ├── telemetry.py             # Real-time telemetry endpoints
│   │   ├── routes.py                # Route optimization endpoints
│   │   └── __init__.py
│   └── __init__.py
├── models/                          # Database models (SQLAlchemy)
│   ├── bike.py                      # Bike entity model
│   ├── ride.py                      # Ride tracking model
│   ├── maintenance.py               # Maintenance record model
│   ├── prediction.py                # ML prediction storage model
│   ├── bike_features.py             # Engineered features model
│   └── __init__.py
├── schemas/                         # API request/response schemas (Pydantic)
│   ├── bike.py                      # Bike API schemas
│   ├── ride.py                      # Ride API schemas
│   ├── maintenance.py               # Maintenance API schemas
│   ├── prediction.py                # Prediction API schemas
│   ├── route.py                     # Route optimization schemas
│   └── __init__.py
├── services/                        # Business logic layer
│   ├── bike_service.py              # Bike management logic
│   ├── ride_service.py              # Ride processing logic
│   ├── maintenance_service.py       # Maintenance workflow logic
│   ├── prediction_service.py        # ML prediction service
│   ├── telemetry_service.py         # Telemetry data processing
│   ├── route_optimization_service.py # Route planning logic
│   ├── feature_service.py           # Feature engineering service
│   ├── synthetic_data_service.py    # Demo data generation
│   └── __init__.py
└── utils/                           # Utility functions
    └── __init__.py
```

### Machine Learning Pipeline (`backend/ml_models/`)
```
backend/ml_models/
├── feature_engineering/              # Feature calculation and processing
│   ├── feature_engineer.py          # Core feature engineering logic
│   └── __init__.py
├── training/                        # Model training pipeline
│   ├── xgboost_model.py             # XGBoost model training and evaluation
│   └── __init__.py
├── inference/                       # Real-time prediction service
│   ├── model_inference.py           # Live prediction generation
│   └── __init__.py
└── trained/                         # Trained model storage (created at runtime)
    ├── brake_model.joblib           # Brake failure prediction model
    ├── chain_model.joblib           # Chain failure prediction model
    ├── tire_model.joblib            # Tire failure prediction model
    ├── scaler.joblib                # Feature scaling model
    └── model_metadata.json          # Model version and performance info
```

### Data Storage (`backend/data/`)
```
backend/data/
├── synthetic/                       # Generated demo data
├── processed/                       # Processed feature datasets
└── raw/                            # Raw data inputs (if any)
```

### Scripts and Configuration
```
backend/
├── scripts/                        # Utility scripts
│   ├── generate_demo_data.py       # Demo data generation script
│   └── __init__.py
├── requirements.txt                # Python package dependencies
├── Dockerfile                     # Backend container configuration
├── .env.example                   # Backend environment template
├── alembic.ini                    # Database migration configuration
├── alembic/                       # Database migration files
│   ├── env.py                     # Alembic environment setup
│   ├── script.py.mako             # Migration script template
│   └── versions/                  # Migration version files
└── tests/                         # Unit and integration tests
    └── __init__.py
```

## 🎨 Frontend Directory (`frontend/`)

### React Application (`frontend/src/`)
```
frontend/src/
├── main.jsx                        # React application entry point
├── App.jsx                         # Main application component
├── index.css                       # Global styles and Tailwind imports
├── components/                     # React components
│   ├── Navbar.jsx                  # Navigation component
│   ├── Dashboard/                  # Dashboard page components
│   │   ├── Dashboard.jsx           # Main dashboard view
│   │   ├── StatsCards.jsx          # Fleet statistics cards
│   │   ├── PriorityBikesList.jsx   # Maintenance priority list
│   │   └── BikeMap.jsx             # Interactive map component
│   ├── BikeDetails/                # Individual bike detail components
│   │   └── BikeDetails.jsx         # Detailed bike information view
│   ├── MaintenanceList/            # Maintenance management components
│   │   └── MaintenanceList.jsx     # Maintenance records table
│   └── RouteOptimizer/             # Route planning components
│       └── RouteOptimizer.jsx      # Route optimization interface
├── services/                       # API integration services
│   └── api.js                      # Axios-based API client
├── contexts/                       # React context for state management
│   └── BikeContext.jsx             # Global bike fleet state
├── utils/                          # Utility functions
├── hooks/                          # Custom React hooks
└── assets/                         # Static assets (images, icons)
```

### Frontend Configuration
```
frontend/
├── package.json                    # Node.js dependencies and scripts
├── vite.config.js                  # Vite build configuration
├── tailwind.config.js              # Tailwind CSS configuration
├── postcss.config.js               # PostCSS configuration
├── index.html                      # HTML entry point
├── Dockerfile                     # Frontend container configuration
├── .env.example                   # Frontend environment template
└── public/                        # Static public assets
    └── favicon.ico                # Application favicon
```

## 🐳 Infrastructure Configuration

### Docker Setup
- **docker-compose.yml**: Multi-service orchestration
  - PostgreSQL database service
  - InfluxDB time-series database
  - Redis caching service  
  - FastAPI backend service
  - React frontend service
  - Volume mounting for development
  - Network configuration

### Database Services
- **PostgreSQL**: Primary database for bikes, rides, maintenance records
- **InfluxDB**: Time-series database for telemetry data
- **Redis**: Caching layer for improved performance

## 🚀 Key Features by Directory

### Backend API (`backend/app/api/`)
- **30+ REST endpoints** for complete fleet management
- **OpenAPI documentation** auto-generated at `/docs`
- **Authentication ready** with JWT token support
- **CORS configuration** for frontend integration

### Machine Learning (`backend/ml_models/`)
- **Feature Engineering**: 24 calculated features from ride data
- **XGBoost Training**: Separate models for brake, chain, tire predictions
- **Real-time Inference**: Live prediction generation
- **Model Versioning**: Performance tracking and model updates

### Interactive Frontend (`frontend/src/components/`)
- **Responsive Dashboard**: Fleet overview with real-time updates
- **Interactive Maps**: Mapbox integration for bike locations
- **Mobile Optimized**: Touch-friendly interface for field crews
- **Real-time Updates**: Live data refresh capabilities

## 📊 Data Flow Architecture

```
Bike Sensors → Telemetry API → InfluxDB → Feature Engineering → 
XGBoost Models → Predictions → PostgreSQL → REST API → React Dashboard
```

## 🔧 Development vs Production

### Development Mode
- Hot-reload for both backend and frontend
- Debug logging enabled
- Local file mounting
- Development database credentials

### Production Ready
- Optimized Docker images
- Environment-based configuration
- Database connection pooling
- Security configurations

## 📈 Scalability Considerations

- **Horizontal Scaling**: Load balancer ready
- **Database Optimization**: Indexed queries and connection pooling
- **Caching Strategy**: Redis for frequently accessed data
- **Microservices Ready**: Service-based architecture

## 🔒 Security Features

- Environment-based secrets management
- Database connection security
- API authentication framework
- CORS configuration
- Input validation with Pydantic

---

This structure supports a production-ready bike sharing predictive maintenance system that can scale from hundreds to thousands of bikes while maintaining performance and reliability.
