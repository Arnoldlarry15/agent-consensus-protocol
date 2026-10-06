# Agent Consensus Protocol ⚖️

[![License: MIT](https://img.shields.io/badge/License-MIT-amber.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Consensus: Quorum-Backed](https://img.shields.io/badge/Consensus-Quorum--Backed-emerald.svg)](https://labuilds.xyz)
[![Ecosystem: LA Builds](https://img.shields.io/badge/Catalog-329%20Production%20Engines-amber.svg)](https://labuilds.xyz)

> **Autonomous Multi-Agent Consensus & Deliberation Protocol Engine**

---

### 🌐 Part of the LA Builds Architecture Ecosystem
> Looking for production-grade turnkey Python engines, AI security guardrails, and enterprise blueprints?  
> **Explore all 329 self-hosted architectures on the official store: [labuilds.xyz](https://www.labuilds.xyz)**

---

## The Problem
When coordinating multi-agent systems (CrewAI, AutoGen, LangGraph, OpenAI Swarm), specialized agents often reach contradictory conclusions or recommend conflicting actions. Relying on simple majority vote or unconstrained prompt arguments frequently causes infinite deliberation loops, hallucinated compromises, and unreliable executions.

## The Solution
`agent-consensus-protocol` provides a formal mathematical framework for multi-agent quorum deliberation and confidence-weighted voting:

- ⚖️ **Confidence-Weighted Voting**: Agents submit proposals backed by numerical confidence metrics.
- 🏛️ **Configurable Quorum Thresholds**: Enforces 2/3 (67%) or supermajority rules before automated tool execution.
- 🛑 **Deadlock Detection & Escalation**: Identifies split-brain agent states and terminates deliberation gracefully.

## Quickstart

### 1. Installation
```bash
pip install -e .
```

### 2. Usage
```python
from agent_consensus_protocol import AgentConsensusProtocol

# Enforce 2/3 supermajority consensus
protocol = AgentConsensusProtocol(quorum_threshold=0.67)

votes = [
    {"agent_id": "security_agent", "proposal": "quarantine_endpoint", "confidence": 0.95},
    {"agent_id": "audit_agent", "proposal": "quarantine_endpoint", "confidence": 0.85},
    {"agent_id": "ops_agent", "proposal": "restart_container", "confidence": 0.30}
]

verdict = protocol.resolve_consensus(votes)

print("Consensus Reached:", verdict.reached) # True
print("Winning Action:", verdict.decision) # "quarantine_endpoint"
print("Agreement Ratio:", verdict.agreement_ratio) # 0.857
```

## Running Tests
```bash
pytest tests/
```

## License
MIT License. Free for commercial and open-source use.

Developed by [LA Builds](https://www.labuilds.xyz) • Autonomous AI Systems & Architecture.
