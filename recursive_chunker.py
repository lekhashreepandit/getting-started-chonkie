from chonkie import RecursiveChunker, RecursiveRules

chunker = RecursiveChunker(
    tokenizer="character",
    chunk_size=2048,
    rules=RecursiveRules(),
    min_characters_per_chunk=24,
)

text = """This is the first sentence. This is the second sentence.
And here's a third one with some additional context."""

chunks = chunker.chunk(text)

for chunk in chunks:
    print(f"Chunk text: {chunk.text}")
    print(f"Token count: {chunk.token_count}")
