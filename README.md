# TrustRAG-Agent 🛡️🤖

### A Trustworthy and Adaptive Agent for Evidence-Based Question Answering

> A lightweight research prototype exploring how an AI agent can **plan, retrieve evidence, validate information, adapt when evidence is insufficient, and generate grounded answers**.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![AI Agent](https://img.shields.io/badge/AI-Agent-8A2BE2)](https://github.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Ready-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

---

## 🎯 Project Overview

Large Language Models can generate fluent answers, but fluency does not necessarily mean that an answer is **correct, grounded, or trustworthy**.

An AI agent should be able to ask:

> **"Do I have enough reliable evidence to answer this question?"**

If the answer is **yes**, the agent generates an evidence-based response.

If the answer is **no**, the agent should not simply guess.

Instead, it should:

1. Re-plan its search strategy.
2. Retrieve additional evidence.
3. Validate the new evidence.
4. Decide whether the evidence is now sufficient.
5. Answer only when sufficient evidence is available.
6. Otherwise, refuse to provide an unsupported answer.

This project implements a small prototype of this idea.

---

# 🧠 Core Idea

The agent follows the following workflow:

```text
                    ┌─────────────────┐
                    │  User Question  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Planner     │
                    │ Planning &      │
                    │ Reasoning       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Evidence        │
                    │ Retrieval       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Evidence        │
                    │ Validation      │
                    └────────┬────────┘
                             │
                       Enough Evidence?
                       /             \
                     YES              NO
                      │                │
                      ▼                ▼
               ┌─────────────┐  ┌─────────────────┐
               │  Generate   │  │ Adaptive        │
               │   Answer    │  │ Re-planning     │
               └──────┬──────┘  └────────┬────────┘
                      │                  │
                      │                  ▼
                      │          Search Again
                      │                  │
                      │                  ▼
                      │          Validate Again
                      │                  │
                      │             Enough?
                      │              /    \
                      │            YES      NO
                      │             │        │
                      ▼             ▼        ▼
               ┌────────────────────────┐  Refuse
               │      Safety Check      │
               └────────────┬───────────┘
                            │
                            ▼
                    ┌─────────────────┐
                    │ Trusted Answer  │
                    └─────────────────┘
```

---

# 🔬 Research Motivation

This project is inspired by several important research directions in modern Agentic AI.

### 1. Planning & Reasoning

The agent decomposes a user question into a sequence of tasks instead of immediately generating an answer.

Example:

```text
1. Understand the user question
2. Retrieve relevant evidence
3. Validate the evidence
4. Generate an evidence-based answer
```

---

### 2. Trustworthy AI

The system does not blindly trust retrieved information.

Evidence is explicitly validated against the original question.

The goal is to reduce unsupported or irrelevant information entering the generation process.

---

### 3. Adaptive Agentic AI

When evidence is insufficient, the agent does not immediately answer.

Instead, it changes its strategy:

```text
Insufficient Evidence
        ↓
Adaptive Re-planning
        ↓
Refine Search Query
        ↓
Retrieve Additional Evidence
        ↓
Validate Again
```

This introduces a simple feedback loop into the agent.

---

### 4. Safety & Hallucination Awareness

The agent follows a conservative principle:

> **No sufficient evidence → No trustworthy answer**

The final answer also passes through a simple grounding/safety check.

---

# ✨ Key Features

- 🧠 Task-based planning
- 🔎 Evidence retrieval
- ✅ Evidence validation
- 🔄 Adaptive re-planning
- 🛡️ Basic answer grounding check
- 🚫 Refusal when evidence is insufficient
- 🤖 LLM-based planning and generation
- 📚 Local knowledge base
- 🌐 FastAPI REST API
- 📖 Automatic Swagger and ReDoc documentation
- 🐍 Python-based implementation
- ⚡ Lightweight architecture
- 🧪 Unit testing

---

# 🏗️ Architecture

The project is intentionally lightweight.

```text
TrustRAG-Agent
│
├── Planner
│     └── Creates reasoning tasks
│
├── Evidence Retriever
│     └── Searches local knowledge sources
│
├── Evidence Validator
│     └── Checks relevance and sufficiency
│
├── Adaptive Replanner
│     └── Creates a new search strategy
│
├── Answer Generator
│     └── Generates an evidence-grounded answer
│
└── Safety Checker
      └── Performs a basic grounding check
```

---

# 📁 Project Structure

```text
trust-rag-agent/
│
├── src/
│   └── trust_rag_agent/
│       │
│       ├── __init__.py
│       ├── agent.py
│       ├── planner.py
│       ├── evidence.py
│       ├── validator.py
│       ├── replanner.py
│       ├── safety.py
│       ├── llm_planner.py
│       └── answer_generator.py
│
├── tests/
│   └── test_planner.py
│
├── knowledge/
│   ├── continual_learning.txt
│   └── quantum_ai.txt
│
├── api.py
├── main.py
│
├── test_llm_planner.py
├── test_evidence.py
├── test_validator.py
├── test_replanner.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# ⚙️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| Pydantic | Data validation |
| uv | Dependency & environment management |
| Pytest | Testing |
| LLM API | Planning & answer generation |
| FastAPI | REST API |
| Uvicorn | API server |
| Docker | Planned containerization |

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/trust-rag-agent.git
cd trust-rag-agent
```

---

## 2. Create the environment

This project uses `uv`.

```bash
uv sync
```

---

## 3. Configure the API key

Create a `.env` file:

```env
API_KEY=your_api_key_here
```

**Never commit `.env` to GitHub.**

Make sure `.gitignore` contains:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## 4. Run the CLI agent

```bash
uv run python main.py
```

---

# 🚀 FastAPI API

TrustRAG-Agent can be accessed through a REST API built with FastAPI.

The API provides a simple interface for sending questions to the agent and receiving evidence-based answers.

## API Architecture

```text
Client
   │
   │ POST /ask
   ▼
┌─────────────────┐
│    FastAPI      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ TrustRAG-Agent  │
└────────┬────────┘
         │
         ├── Planning
         ├── Evidence Retrieval
         ├── Evidence Validation
         ├── Adaptive Re-planning
         ├── Answer Generation
         └── Safety Check
         │
         ▼
┌─────────────────┐
│  JSON Response  │
└─────────────────┘
```

---

## Start the API

Run:

```bash
uv run uvicorn api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoints

## GET `/`

Returns basic information about the API.

Example response:

```json
{
  "name": "TrustRAG-Agent API",
  "version": "0.1.0",
  "status": "running"
}
```

---

## GET `/health`

Health check endpoint.

Example response:

```json
{
  "status": "healthy"
}
```

---

## POST `/ask`

Send a question to the TrustRAG-Agent.

### Request

```json
{
  "question": "What are the challenges of quantum computing for AI agents?"
}
```

### Example response

```json
{
  "question": "What are the challenges of quantum computing for AI agents?",
  "answer": "The challenges include computational complexity, limited quantum hardware, noise and errors, and difficulty integrating quantum algorithms with existing classical AI systems."
}
```

---

# 🧪 Testing the API

You can test the API using Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Or using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"What are the challenges of quantum computing for AI agents?\"}"
```

---

# 🔄 API Request Flow

A request to `/ask` follows the complete agent pipeline:

```text
POST /ask
   │
   ▼
Validate Question
   │
   ▼
Planning
   │
   ▼
Evidence Retrieval
   │
   ▼
Evidence Validation
   │
   ├───────────────┐
   │               │
Enough?           No
   │               │
  Yes              ▼
   │        Adaptive Re-planning
   │               │
   │               ▼
   │        Retrieve Again
   │               │
   │               ▼
   │        Validate Again
   │               │
   └───────┬───────┘
           ▼
    Answer Generation
           │
           ▼
      Safety Check
           │
           ▼
      JSON Response
```

---

# 🧠 Example

Input:

```text
What are the challenges of quantum computing for AI agents?
```

The agent first creates a plan:

```text
[1] Planning...

1. Understand the user question
2. Retrieve relevant evidence
3. Validate the evidence
4. Generate an evidence-based answer
```

Then:

```text
[2] Retrieving evidence...

Retrieved evidence items.
```

Then:

```text
[3] Validating evidence...

Valid evidence is identified.
```

If enough evidence exists:

```text
[4] Evidence is sufficient.

[5] Generating answer...
```

The answer is then checked:

```text
[6] Safety check...

Safety check: PASSED
```

---

# 🔄 Adaptive Re-planning Example

The interesting part of the project happens when the agent does **not** have enough evidence.

For example:

```text
Question:
What are the challenges of quantum computing for AI agents?
```

If the available knowledge is insufficient:

```text
[4] Evidence is insufficient.

[5] Adaptive re-planning...

1. Refine the search query
2. Retrieve additional evidence
3. Validate the new evidence
```

The agent then creates a new search query:

```text
quantum computing challenges agents
```

and performs retrieval again.

If the new evidence is still insufficient:

```text
Evidence is still insufficient.

Agent cannot provide a trustworthy answer.
```

This behavior is intentional.

The agent prefers:

> **"I don't have enough evidence."**

over:

> **A confident but unsupported answer.**

---

# 🛡️ Trustworthiness Strategy

The project follows a simple trust-oriented pipeline:

```text
Retrieve
   ↓
Validate
   ↓
Is evidence sufficient?
   ↓
 ┌───────────────┐
 │               │
YES              NO
 │               │
 ▼               ▼
Generate       Re-plan
 │               │
 ▼               ▼
Safety         Retrieve
Check          Again
 │               │
 ▼               ▼
Answer        Validate
                 │
                 ▼
              Answer
              or Refuse
```

The current implementation is a **research prototype**, not a complete safety framework.

---

# 🧩 Design Principles

### Evidence First

The LLM should not be the only source of truth.

```text
Evidence → Validation → Generation
```

rather than:

```text
Question → LLM → Answer
```

---

### Fail Safely

If evidence is insufficient:

```text
No Evidence
     ↓
No Answer
```

instead of:

```text
No Evidence
     ↓
Guess
```

---

### Adapt Instead of Stopping

The agent can change its retrieval strategy when its first attempt fails.

```text
Initial Plan
     ↓
Failure
     ↓
Re-plan
     ↓
New Retrieval
```

---

# 🧪 Testing

Run the test suite:

```bash
uv run pytest
```

Example:

```text
collected 1 item

tests/test_planner.py .                                      [100%]

1 passed
```

Additional tests cover:

- Planner
- Evidence retrieval
- Evidence validation
- Adaptive re-planning

---

# 📊 Current Limitations

This project is intentionally small and should be considered a **prototype**.

Current limitations include:

- Local keyword-based retrieval
- Simple relevance scoring
- Basic evidence validation
- Basic grounding check
- No vector database
- No sophisticated semantic retrieval
- No reinforcement learning
- No persistent agent memory
- No formal safety benchmark
- No large-scale evaluation
- No true continual-learning algorithm

These limitations also provide clear directions for future research.

---

# 🔮 Future Work

## Semantic Retrieval

Replace keyword matching with:

```text
Embedding
    ↓
Vector Database
    ↓
Semantic Retrieval
```

Possible technologies:

- FAISS
- Qdrant
- Chroma

---

## Better Evidence Validation

Introduce:

- NLI-based verification
- Cross-source consistency checking
- LLM-as-a-judge
- Citation verification
- Contradiction detection

---

## Advanced Planning

Replace the simple planner with more advanced agent reasoning:

```text
Goal
 ↓
Sub-goals
 ↓
Tool Selection
 ↓
Execution
 ↓
Observation
 ↓
Re-planning
```

---

## Continual Learning

A future version could allow the agent to learn from new interactions while controlling:

```text
New Knowledge
      ↓
Knowledge Validation
      ↓
Memory Update
      ↓
Old Knowledge Retention
```

This would move the project closer to genuine **continual learning for agentic systems**.

---

## Advanced Safety

Future versions could include:

- Hallucination detection
- Prompt injection detection
- Unsafe instruction detection
- Source reliability scoring
- Confidence estimation
- Answer abstention
- Adversarial evaluation

---

## Production Deployment

Future work includes containerizing the API:

```text
FastAPI
   ↓
Docker
   ↓
Production Deployment
```

Additional production features may include:

- Authentication
- Rate limiting
- Structured logging
- Monitoring
- Request tracing
- API versioning

---

# 🎓 Research Relevance

This project explores several concepts directly relevant to research in **Trustworthy and Adaptive Agentic AI**:

| Research Area | Project Component |
|---|---|
| Planning & Reasoning | `Planner` |
| Trustworthy AI | `EvidenceValidator` |
| Adaptive Agents | `AdaptiveReplanner` |
| Hallucination Awareness | `SafetyChecker` |
| Evidence-Based Generation | `AnswerGenerator` |
| Retrieval-Augmented Generation | `EvidenceRetriever` |
| Continual Learning | Future extension |
| Agentic AI | Overall architecture |

---

# 📌 Research Question

The project is motivated by a simple research question:

> **How can an AI agent dynamically evaluate the sufficiency of its evidence and adapt its reasoning process before generating an answer?**

The current implementation provides a small experimental environment for exploring this question.

---

# 👨‍💻 Author

**Saeid Akbari**

AI Engineer & Educator

Python • Machine Learning • Deep Learning • MLOps • Generative AI • Agentic AI

GitHub:

https://github.com/saeidakbari3364

---

# 📄 Project Status

🚧 **Research Prototype**

The project is under active development.

Current focus:

```text
Planning
   ↓
Evidence Retrieval
   ↓
Evidence Validation
   ↓
Adaptive Re-planning
   ↓
Grounded Answer Generation
   ↓
Safety Check
   ↓
FastAPI REST API
```

Future versions will investigate more advanced retrieval, reasoning, memory, continual learning, and safety mechanisms.

---

# ⭐ Why This Project?

Trustworthy Agentic AI should not only be able to **generate answers**.

It should also be able to:

> **Plan → Search → Verify → Adapt → Decide → Answer**

And when the evidence is not enough:

> **Know when not to answer.**

That is the central idea behind **TrustRAG-Agent**.
