# Memory System Design

A three-tier architecture for persistent AI context.

## Memory Tiers
1. **Short-Term Working Memory**: Real-time inputs and active tasks (hours to days).
2. **Long-Term Episodic Memory**: Specific events (e.g., "Dropped at 2:15pm").
3. **Long-Term Semantic Memory**: General knowledge (e.g., "Dropping causes damage").

## Implementation
Uses a combination of SQLite for structured data and vector embeddings for semantic search.\n