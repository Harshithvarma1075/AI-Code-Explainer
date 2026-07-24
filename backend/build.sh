#!/usr/bin/env bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Building ChromaDB..."
python -m app.rag.ingest

echo "Build completed successfully!"