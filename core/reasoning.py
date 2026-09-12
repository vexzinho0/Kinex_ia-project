class ReasoningEngine:
    """Reasoning interface reserved for the future model implementation."""

    def process(self, input_text: str, context: list[dict] | None = None) -> dict:
        return {
            "input": input_text,
            "context_items": len(context or []),
            "status": "not_implemented",
        }
