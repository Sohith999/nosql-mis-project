#!/bin/bash

echo "================================"
echo "Starting NoSQL MIS Application"
echo "================================"
echo ""

echo "Checking MongoDB..."
if mongosh --eval "db.version()" > /dev/null 2>&1; then
    echo "✅ MongoDB is running"
else
    echo "❌ MongoDB is not running!"
    echo "Start it with: brew services start mongodb-community (macOS)"
    echo "Or: sudo systemctl start mongod (Linux)"
    exit 1
fi

echo ""
echo "Checking Redis..."
if redis-cli ping > /dev/null 2>&1; then
    echo "✅ Redis is running"
else
    echo "❌ Redis is not running!"
    echo "Start it with: brew services start redis (macOS)"
    echo "Or: sudo systemctl start redis (Linux)"
    exit 1
fi

echo ""
echo "Starting Flask server..."
python3 app.py