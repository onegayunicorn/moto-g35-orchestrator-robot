import time

class ShortTermMemory:
    def __init__(self):
        self.buffer = []
        self.retention_period = 86400 # 24 hours

    def add_event(self, event_type, description):
        event = {
            'timestamp': time.time(),
            'type': event_type,
            'description': description
        }
        self.buffer.append(event)
        self.prune()

    def prune(self):
        now = time.time()
        self.buffer = [e for e in self.buffer if now - e['timestamp'] < self.retention_period]

    def get_recent_events(self):
        return self.buffer\n