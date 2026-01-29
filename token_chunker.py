from chonkie import TokenChunker

# Initialize the chunker
chunker = TokenChunker(
    tokenizer="gpt2",
    chunk_size=512,
    chunk_overlap=50
)

# Chunk your text
text = "Your long document text here..."
chunks = chunker.chunk(text)

# Access chunk information
for chunk in chunks:
    print(f"Chunk: {chunk.text[:50]}...")
    print(f"Tokens: {chunk.token_count}")