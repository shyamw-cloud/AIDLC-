from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Ticket:
    key: str
    summary: str
    description: str = ""
    acceptance_criteria: List[str] = field(default_factory=list)
    priority: str = "medium"
    labels: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, payload: Dict[str, Any]) -> "Ticket":
        return cls(
            key=payload.get("key", "UNKNOWN"),
            summary=payload.get("summary", "No summary provided"),
            description=payload.get("description", ""),
            acceptance_criteria=payload.get("acceptance_criteria", []),
            priority=payload.get("priority", "medium"),
            labels=payload.get("labels", []),
        )
