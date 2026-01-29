from chonkie import SemanticChunker

# Initialize with semantic similarity grouping
chunker = SemanticChunker(
    embedding_model="minishlab/potion-base-32M",
    threshold=0.7,  # Similarity threshold
    chunk_size=512
)

text = """Your document text with multiple topics and themes..."""
chunks = chunker.chunk(text)

# Process chunks
for chunk in chunks:
    print(f"Chunk: {chunk.text[:50]}...")
    print(f"Tokens: {chunk.token_count}")