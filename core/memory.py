class Memory:
    """Simple in-process memory for the prototype.

    This will later be replaced/extended with persistent storage and
    validated knowledge retrieval.
    """

    def __init__(self):
        self.items = []

    def add(self, item: dict) -> None:
        self.items.append(item)

    def count(self) -> int:
        return len(self.items)

    def recent(self, limit: int = 10) -> list[dict]:
        return self.items[-limit:]
