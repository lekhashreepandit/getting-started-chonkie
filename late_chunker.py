from chonkie import LateChunker, RecursiveRules

chunker = LateChunker(
    embedding_model="nomic-ai/modernbert-embed-base",
    chunk_size=2048,
    rules=RecursiveRules(),
    min_characters_per_chunk=24,
)

# single text chunking
text = """First paragraph about a specific topic.
Second paragraph continuing the same topic.
Third paragraph switching to a different topic.
Fourth paragraph expanding on the new topic."""

chunks = chunker(text)

for chunk in chunks:
    print(f"Chunk text: {chunk.text}")
    print(f"Token count: {chunk.token_count}")
    print(f"Embedding shape: {chunk.embedding.shape}")