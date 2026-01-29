from chonkie import SentenceChunker

# Basic initialization with default parameters
chunker = SentenceChunker(
    tokenizer="character",     # Default tokenizer (or use "gpt2", etc.)
    chunk_size=2048,           # Maximum tokens per chunk
    chunk_overlap=128,         # Overlap between chunks
    min_sentences_per_chunk=1  # Minimum sentences in each chunk
)

# single text chunking
text = """This is the first sentence. This is the second sentence.
And here's a third one with some additional context."""
chunks = chunker.chunk(text)

for chunk in chunks:
    print(f"Chunk text: {chunk.text}")
    print(f"Token count: {chunk.token_count}")

    