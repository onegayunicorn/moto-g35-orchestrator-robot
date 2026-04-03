# Sensor System Design

The sensor system translates raw data into human-like descriptions for the AI.

## Sensor Mapping
| Sensor | Detection | Human-Like Output |
|--------|-----------|-------------------|
| Accelerometer | Impacts, Movement | "Ouch!", "Moving left slowly" |
| Temp/Humidity | Environment | "Cold", "Getting hot" |
| Camera | Objects, People | "Red cup on desk", "Person smiling" |
| Microphone | Sounds, Words | "Someone said 'hello'", "Loud noise" |

## Translation Engine
The engine uses a rule-based and ML-based approach to convert numerical values into descriptive strings.\n