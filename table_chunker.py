from chonkie import TableChunker

table = """
| Name   | Age | City     |
|--------|-----|----------|
| Alice  | 30  | New York |
| Bob    | 25  | London   |
| Carol  | 28  | Paris    |
| Dave   | 35  | Berlin   |
"""

chunker = TableChunker(tokenizer="row", chunk_size=3)
chunks = chunker.chunk(table)
for chunk in chunks:
	print(chunk.text)