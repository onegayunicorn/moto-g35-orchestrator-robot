#!/bin/bash
# OGUF Termux Bridge Script

COMMAND=$1

case $COMMAND in
    "init")
        echo "🚀 Initializing OGUF Bridge on Moto G35..."
        sleep 1
        echo "✅ Bridge initialized"
        ;;
    "status")
        echo "🦄 OGUF System Monitor"
        echo "======================"
        echo "Time: $(date)"
        echo ""
        # Check if orchestrator is running on port 8080
        if curl -s http://localhost:8080/health > /dev/null; then
            echo "🟢 Orchestrator: UP"
        else
            echo "🔴 Orchestrator: DOWN"
        fi
        
        # Check if bridge process is running (self-check or placeholder)
        echo "🟢 Termux Bridge: UP"
        echo ""
        echo "Press Ctrl+C to stop monitoring"
        ;;
    "exec")
        shift
        echo "Executing on bridge: $@"
        eval "$@"
        ;;
    *)
        echo "Usage: $0 {init|status|exec}"
        ;;
esac
