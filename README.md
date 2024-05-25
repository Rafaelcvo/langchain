# LangChain Quick Start Guide

## Introduction

LangChain offers a variety of components designed to help build question-answering (QA) applications and RAG (Retrieval-Augmented Generation) applications in general. In this guide, we will build a simple QA application using a text data source. Along the way, we will cover a typical QA architecture, discuss the relevant components of LangChain, and highlight additional features for more advanced QA techniques. We will also explore how LangSmith can help us track and understand our application, becoming increasingly useful as our application grows in complexity.

We will create a typical RAG application, as described in the QA introduction, which has two main components:

1. **Indexing**: A pipeline to ingest data from a source and index it. This usually happens offline.
2. **Retrieval and Generation**: The actual RAG chain, which takes the user's query at runtime, retrieves the relevant data from the index, and then passes it to the model.

The complete sequence from raw data to response will look like this:

### Indexing Process
1. **Load**: First, we need to load our data. We will use `DocumentLoaders` for this.
2. **Split**: Text splitters break documents into smaller chunks. This is useful for both indexing data and passing it to a model, as large chunks are harder to search and do not fit in a model's finite context window.
3. **Store**: We need a place to store and index our splits so they can be searched later. This is usually done using a `VectorStore` and `Embeddings`.

### Retrieval and Generation Process
4. **Retrieve**: Given a user input, the relevant splits are retrieved from storage using a `Retriever`.
5. **Generate**: A `ChatModel` or `LLM` produces a response using a prompt that includes the question and the retrieved data.

In this guide, we will use an OpenAI chat model and embeddings, and a Chroma vector store, but everything shown here works with any `ChatModel` or `LLM`, `Embeddings`, and `VectorStore` or `Retriever`.

## Quick Start

### Installation

We will use the following packages:

```bash
pip install --upgrade --quiet langchain langchain-community langchainhub langchain-openai langchain-chroma bs4
```

## Referências

[RAG](https://python.langchain.com/v0.1/docs/use_cases/question_answering/)