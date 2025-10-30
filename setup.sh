#!/bin/bash
# 🚴 Automated Setup Script for Predictive Maintenance Bike Sharing System

echo "🚴 Setting up Predictive Maintenance for Bike Sharing System..."
echo "==============================================================="

# Check dependencies
echo "🔍 Checking system dependencies..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    echo "   Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose not found. Please install Docker Compose first."
    echo "   Visit: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Environment setup
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.template .env
    echo "⚠️  IMPORTANT: Please edit .env file and add your MAPBOX_ACCESS_TOKEN"
    echo "   Get one free at: https://account.mapbox.com/access-tokens/"
    echo "   This is required for map functionality!"
    echo ""
    read -p "Press Enter to continue once you've added your Mapbox token..."
else
    echo "✅ .env file already exists"
fi

# Start services
echo "🐳 Building and starting Docker services..."
echo "This may take a few minutes on first run..."

# Use docker compose (new syntax) or docker-compose (legacy)
if docker compose version &> /dev/null; then
    docker compose up -d --build
else
    docker-compose up -d --build
fi

# Wait for services
echo "⏳ Waiting for services to start..."
sleep 15

# Health check
echo "🔍 Checking service health..."

if curl -s http://localhost:8000/health > /dev/null; then
    echo "✅ Backend API is healthy"
else
    echo "⚠️  Backend API not responding yet (may need more time)"
fi

if curl -s http://localhost:5173 > /dev/null; then
    echo "✅ Frontend is healthy"  
else
    echo "⚠️  Frontend not responding yet (may need more time)"
fi

echo ""
echo "🎉 Setup completed!"
echo "================="
echo ""
echo "🌐 Access your applications:"
echo "   📊 Frontend Dashboard:  http://localhost:5173"
echo "   🔧 Backend API:         http://localhost:8000"
echo "   📚 API Documentation:   http://localhost:8000/docs"
echo ""
echo "📊 To generate demo data with 100 bikes:"
echo "   docker exec -it bike_maintenance_backend python scripts/generate_demo_data.py"
echo ""
echo "🔧 Useful commands:"
echo "   View logs:     docker compose logs -f"
echo "   Stop services: docker compose down"
echo "   Restart:       docker compose restart"
echo ""
echo "🚴‍♂️ Your bike sharing predictive maintenance system is ready!"
echo "Try the live demo first: check LIVE_DEMO/demo_launcher.html"
