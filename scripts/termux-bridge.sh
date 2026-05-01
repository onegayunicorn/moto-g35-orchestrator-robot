#!/bin/bash
# OGUF Termux Bridge - Moto G35 Optimizer

echo "Initializing OGUF Bridge for Moto G35..."
# Check for python
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install it."
    exit 1
fi

# Launch the bridge component from the monorepo if available
if [ -f "../../onegayunicorn-monorepo/src/termux-bridge/termux_bridge.py" ]; then
    python3 ../../onegayunicorn-monorepo/src/termux-bridge/termux_bridge.py
else
    echo "Stand-alone bridge mode active."
    while true; do
        echo "Monitoring Moto G35..."
        sleep 10
    done
fi
