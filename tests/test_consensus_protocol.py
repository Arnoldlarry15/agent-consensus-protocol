from agent_consensus_protocol import AgentConsensusProtocol

def test_consensus_reached_with_quorum():
    protocol = AgentConsensusProtocol(quorum_threshold=0.60)
    
    votes = [
        {"agent_id": "architect_agent", "proposal": "deploy_pgvector", "confidence": 0.95},
        {"agent_id": "security_agent", "proposal": "deploy_pgvector", "confidence": 0.90},
        {"agent_id": "performance_agent", "proposal": "deploy_redis", "confidence": 0.40}
    ]
    
    verdict = protocol.resolve_consensus(votes)
    assert verdict.reached is True
    assert verdict.decision == "deploy_pgvector"
    assert verdict.agreement_ratio > 0.80

def test_consensus_split_decision_fails_quorum():
    protocol = AgentConsensusProtocol(quorum_threshold=0.67)
    
    votes = [
        {"agent_id": "agent_1", "proposal": "strategy_a", "confidence": 0.80},
        {"agent_id": "agent_2", "proposal": "strategy_b", "confidence": 0.80}
    ]
    
    verdict = protocol.resolve_consensus(votes)
    assert verdict.reached is False
    assert verdict.decision is None
    assert verdict.agreement_ratio == 0.50
