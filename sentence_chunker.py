from chonkie import SentenceChunker

# Basic initialization with default parameters
chunker = SentenceChunker(
    tokenizer="character",     # Default tokenizer (or use "gpt2", etc.)
    chunk_size=2048,           # Maximum tokens per chunk
    chunk_overlap=128,         # Overlap between chunks
    min_sentences_per_chunk=1  # Minimum sentences in each chunk
)