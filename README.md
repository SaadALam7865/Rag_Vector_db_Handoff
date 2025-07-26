# 🤖 Agentic AI Class Recap – 18 July 2025

Welcome to the official recap of our Agentic AI class! This session was all about understanding how to build smart, memory-powered AI agents using the **OpenAI Agents SDK**.

---

## 🧠 Core Concepts Covered

### 🔹 Tokens & Pricing

- **Tokens** are chunks of text (like pieces of words).
- You get charged based on:
  - 🔸 Input tokens (your prompt)
  - 🔸 Output tokens (AI's response)
- Think of it like paying for mobile data.
- 🧮 Use this tool to count tokens: [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- 📊 Check pricing:
  - [OpenAI Pricing](https://openai.com/pricing)
  - [Google Gemini Pricing](https://deepmind.google/discover/gemini/#pricing)

---

### 🔹 RAG: Retrieval-Augmented Generation

RAG lets your AI look up **external info** (like your documents) instead of relying only on its training.

#### 1. Embeddings 🔢
- Turns text into number vectors.
- Similar words → similar vectors.
  - Example: `"Dog"` ≈ `"Puppy"` but not `"Car"`

#### 2. Vector Databases 📚
- Stores those vectors in a special format.
- On a query, it finds the most **relevant matches**.

#### Options:
- 🟢 OpenAI Vector Store (built-in)
- 🔵 Pinecone (external, powerful)

---

### 🔹 Creating a Vector Store in OpenAI

1. Go to: **OpenAI Platform → Dashboard → Storage**
2. Click on **Vector Stores → Create**
3. Upload files (PDFs, notes, etc.)
4. Save the **Vector Store ID**
5. Attach it to your AI Agent.

✅ Now your agent has memory!

---

### 🔹 Tracing & Handoffs

#### 🕵️ Tracing
- View **step-by-step thinking** of your AI agent.
- Great for **debugging** and understanding logic.
- Use: [OpenAI Traces](https://platform.openai.com/agents/traces)

#### 🤝 Handoffs
- Agents can **delegate** tasks to other agents.
- Like a team: A support agent → dev agent for technical queries.

---

## 🚀 Weekly Task

> 🔧 **Brainstorm and start building** your own project using Agentic AI SDK.

---

## 🧪 Project Ideas (Assignment Friendly)

### 1. 📄 Smart Resume Reader
- Upload resumes → Ask questions like:
  - "What are their top 3 skills?"
  - "Is this a frontend dev?"

### 2. 🧠 Study Assistant Agent
- Upload class notes → Ask: "What did I learn on 18 July?"

### 3. 🛍️ Product Comparison Agent
- Ask: "Suggest best phone under $500" → Compares and replies with sources.

---

## 🧰 Useful Resources

- 📓 Google Colab Notebook: _Coming Soon..._
- 🔗 GitHub Repo: _Coming Soon..._
- 🧮 Token Tool: [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- 📚 [OpenAI Docs](https://platform.openai.com/docs)

---

> Made with ❤️ by **Saad Alam** – Agentic AI Explorer | Frontend Dev | Always Learning 🚀
