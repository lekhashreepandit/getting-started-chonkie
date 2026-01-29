from chonkie import NeuralChunker

# Basic initialization with default parameters
chunker = NeuralChunker(
    model="mirth/chonky_modernbert_base_1",  # Default model
    device_map="cpu",                        # Device to run the model on ('cpu', 'cuda', etc.)
    min_characters_per_chunk=10,             # Minimum characters for a chunk
)

# single text chunking
text = """Topic one starts here and continues for a bit.
Suddenly, the context shifts to topic two, which is quite different.
Topic two carries on, discussing various aspects. Then topic one briefly returns.
Finally, we conclude with topic three."""

chunks = chunker.chunk(text)

for chunk in chunks:
    print(f"Chunk text: {chunk.text}")
    print(f"Token count: {chunk.token_count}") # Note: token_count might be added post-hoc or not available depending on implementation
    print(f"Start index: {chunk.start_index}")
    print(f"End index: {chunk.end_index}")