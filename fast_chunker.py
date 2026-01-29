from chonkie import FastChunker

# Initialize the chunker
chunker = FastChunker(
    chunk_size=1024,
    delimiters=". \n",
)

# Chunk your text
text = "Your long document text here..."
chunks = chunker.chunk(text)

# Access chunk information
for chunk in chunks:
    print(f"Chunk: {chunk.text[:50]}...")
    print(f"Bytes: {len(chunk.text)}")
    print(f"Position: {chunk.start_index}-{chunk.end_index}")