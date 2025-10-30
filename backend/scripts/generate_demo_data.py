#!/usr/bin/env python3
"""
🚴 Demo Data Generation for Predictive Maintenance Bike Sharing System

This script generates realistic synthetic data for the bike sharing system including:
- 100 bikes with realistic locations and specifications
- Historical ride data with telemetry patterns
- Maintenance records with component-specific history
- ML features for predictive modeling

Usage: python scripts/generate_demo_data.py
"""

import asyncio
import sys
import os
from datetime import datetime

# Add the app directory to the Python path
sys.path.append('/app')

from app.core.database import AsyncSessionLocal
from app.services.synthetic_data_service import SyntheticDataService
from ml_models.feature_engineering.feature_engineer import FeatureEngineer
from ml_models.training.xgboost_model import PredictiveMaintenanceModel

async def main():
    print("🚴 Generating Demo Data for Bike Sharing System...")
    print("=" * 60)

    async with AsyncSessionLocal() as db:
        # Generate synthetic fleet and rides
        print("📊 Creating synthetic fleet and ride data...")
        service = SyntheticDataService(db)
        result = await service.populate_complete_dataset(num_bikes=100)

        print(f"✅ Generated:")
        print(f"   🚲 Bikes: {result['bikes']}")
        print(f"   🚴 Rides: {result['rides']}")
        print(f"   🔧 Maintenance Records: {result['maintenance_records']}")

        # Generate ML features
        print("\n🧠 Engineering features for ML model...")
        feature_engineer = FeatureEngineer(db)
        feature_result = await feature_engineer.bulk_update_features()
        print(f"✅ Updated features for {feature_result['updated_bikes']} bikes")

        # Train initial ML model
        print("\n🤖 Training predictive maintenance models...")
        training_data = await feature_engineer.get_training_dataset()

        if len(training_data) > 20:  # Ensure sufficient data
            model = PredictiveMaintenanceModel()
            training_results = model.train_models(training_data)

            print("✅ Model training completed!")
            print("📈 Model Performance:")
            for component, metrics in training_results.items():
                roc_auc = metrics.get('roc_auc', 0)
                print(f"   {component.title()} Model ROC-AUC: {roc_auc:.3f}")
        else:
            print("⚠️  Insufficient data for model training. Generated data first.")

    print("\n" + "=" * 60)
    print("🎉 Demo Data Generation Completed Successfully!")
    print("\n🌐 Next Steps:")
    print("   1. Visit http://localhost:5173 for the dashboard")
    print("   2. Check API docs at http://localhost:8000/docs")
    print("   3. Monitor logs: docker compose logs -f")
    print("\n🚴‍♂️ Your bike sharing predictive maintenance system is ready!")

if __name__ == "__main__":
    asyncio.run(main())
