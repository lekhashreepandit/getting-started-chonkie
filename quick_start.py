# First import the chunker you want from Chonkie
from chonkie import TokenChunker

# Initialize the chunker
chunker = TokenChunker() # defaults to using GPT2 tokenizer

# Here's some text to chunk
text = """Woah! Chonkie, the chunking library is so cool!"""

# Chunk some text
chunks = chunker(text)

# Access chunks
for chunk in chunks:
  print(f"Chunk: {chunk.text}")
  print(f"Tokens: {chunk.token_count}")