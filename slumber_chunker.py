from chonkie import SlumberChunker
from chonkie.genie import GeminiGenie

# Optional: Initialize Genie
genie = GeminiGenie(
    model="gemini-3-pro-preview",
    api_key="YOUR_GEMINI_API_KEY"
)

# Basic initialization
chunker = SlumberChunker(
    genie=genie,                        # Genie interface to use
    tokenizer="character",              # Default tokenizer
    chunk_size=1024,                    # Maximum chunk size
    candidate_size=128,                 # How many tokens Genie looks at for potential splits
    min_characters_per_chunk=24,        # Minimum number of characters per chunk
    verbose=True                        # See the progress bar for the chunking process
)

# single text chunking
text = """Complex document with interwoven ideas. Section 1 introduces concept A.
Section 2 discusses concept B, but references A frequently.
Section 3 concludes by merging A and B. Traditional chunkers might struggle here."""

# Assuming 'chunker' is initialized as shown above
chunks = chunker.chunk(text)

for chunk in chunks:
    print(f"Chunk text: {chunk.text}")
    print(f"Token count: {chunk.token_count}")
    print(f"Start index: {chunk.start_index}")
    print(f"End index: {chunk.end_index}")
