# Software-Only Installation Guide

Transform your Moto G35 without any hardware modifications.

## Prerequisites
- Moto G35 (Android 13+)
- Developer Options enabled
- ADB installed on your computer

## Steps
1. Clone this repository.
2. Run `scripts/setup-dev-environment.sh`.
3. Deploy the core system using `scripts/deploy-to-device.sh`.
4. Configure virtual sensors in `software/core-system/src/sensor-translation/virtual-sensors/`.\n