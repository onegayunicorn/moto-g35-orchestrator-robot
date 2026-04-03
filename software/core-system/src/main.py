from sensor_translation.translation_engine import TranslationEngine
from memory_system.short_term_memory import ShortTermMemory

def main():
    print("Moto G35 Orchestrator Robot Starting...")
    engine = TranslationEngine()
    memory = ShortTermMemory()
    
    # Example Loop
    event = engine.translate_temperature(12)
    print(f"Sensor: {event}")
    memory.add_event("sensor_alert", event)
    
    print("Current Memory:", memory.get_recent_events())

if __name__ == "__main__":
    main()\n