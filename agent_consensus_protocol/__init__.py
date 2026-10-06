import math
from typing import List, Dict, Any, Optional

class ConsensusVerdict:
    def __init__(self, reached: bool, decision: Any, agreement_ratio: float, round_count: int, votes: Dict[str, Any]):
        self.reached = reached
        self.decision = decision
        self.agreement_ratio = round(agreement_ratio, 3)
        self.round_count = round_count
        self.votes = votes

    def to_dict(self) -> Dict[str, Any]:
        return {
            "consensus_reached": self.reached,
            "decision": self.decision,
            "agreement_ratio": self.agreement_ratio,
            "deliberation_rounds": self.round_count,
            "agent_votes": self.votes
        }

class AgentConsensusProtocol:
    """
    Autonomous Multi-Agent Consensus & Deliberation Protocol Engine.
    Resolves conflicting multi-agent votes using confidence weighting and quorum thresholds.
    """
    def __init__(self, quorum_threshold: float = 0.67, max_deliberation_rounds: int = 3):
        self.quorum_threshold = quorum_threshold
        self.max_deliberation_rounds = max_deliberation_rounds

    def resolve_consensus(self, agent_votes: List[Dict[str, Any]]) -> ConsensusVerdict:
        """
        Calculates confidence-weighted consensus across an ensemble of agent proposals.
        Each agent proposal is formatted as:
          {"agent_id": str, "proposal": str, "confidence": float (0.0 to 1.0)}
        """
        if not agent_votes:
            return ConsensusVerdict(False, None, 0.0, 1, {})

        # Accumulate weighted votes per proposal
        proposal_weights: Dict[str, float] = {}
        total_weight = 0.0
        vote_audit: Dict[str, Any] = {}

        for vote in agent_votes:
            agent = vote.get("agent_id", "anonymous")
            prop = str(vote.get("proposal", "")).strip()
            conf = float(vote.get("confidence", 1.0))
            conf = max(0.01, min(1.0, conf)) # Clamp between 0.01 and 1.0

            proposal_weights[prop] = proposal_weights.get(prop, 0.0) + conf
            total_weight += conf
            vote_audit[agent] = {"proposal": prop, "weight": round(conf, 3)}

        if total_weight == 0:
            return ConsensusVerdict(False, None, 0.0, 1, vote_audit)

        # Find winning proposal
        winning_proposal = max(proposal_weights, key=proposal_weights.get)
        winning_weight = proposal_weights[winning_proposal]
        ratio = winning_weight / total_weight

        reached = ratio >= self.quorum_threshold

        return ConsensusVerdict(
            reached=reached,
            decision=winning_proposal if reached else None,
            agreement_ratio=ratio,
            round_count=1,
            votes=vote_audit
        )
