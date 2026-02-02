# Getting Started with Chonkie

## Contents

This repository provides **hands-on examples and practical code** accompanying the Medium article:

**[Why Most RAG Pipelines Fail at Chunking — and How Chonkie Fixes It](https://medium.com/@lekhashree2012/why-most-rag-pipelines-fail-at-chunking-and-how-chonkie-fixes-it-5fcbf675c33a)**

- Demonstrations of **core chunking strategies** using `FastChunker` and `RecursiveChunker`
- Example implementations of **TokenChunker**, **SentenceChunker**, **NeuralChunker**, **CodeChunker**, **SlumberChunker**, and other available chunkers

The blog dives into the underlying concepts, explains why chunking is critical in RAG pipelines, and shows how Chonkie approaches it in practice

---

## What is Chonkie

Chonkie is a lightweight Python library for **deterministic, strategy-driven text chunking** in RAG and LLM pipelines. It focuses purely on how text is split — preserving semantic boundaries, respecting token limits, and improving retrieval relevance — without locking you into any embedding model or vector store.

---

## Chunker Types

Chonkie provides multiple strategies to handle different text types and use cases:

- **TokenChunker** – splits text by token count  
- **FastChunker** – high-speed chunking using SIMD acceleration  
- **SentenceChunker** – preserves complete sentences  
- **RecursiveChunker** – recursively splits long structured documents  
- **TableChunker** – handles markdown tables  
- **CodeChunker** – chunks code based on AST structure  
- **SemanticChunker** – groups semantically related content  
- **LateChunker** – semantically rich chunks using embeddings  
- **NeuralChunker** – uses a fine-tuned model to detect topic shifts  
- **SlumberChunker** – agentic chunker leveraging LLM reasoning  

Each chunker is designed for specific scenarios in RAG pipelines, ensuring more accurate and context-aware retrieval.

---

## Installation

Basic installation (TokenChunker, SentenceChunker, RecursiveChunker)

```bash
pip install chonkie
```

For all features

```bash
pip install chonkie[all]
```
