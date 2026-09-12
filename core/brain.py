from datetime import datetime
from core.memory import Memory

class Brain:
    """Initial orchestration layer for Kinex IA.

    The first version intentionally has no external model dependency.
    Future model inference, research and tools plug into this layer.
    """

    def __init__(self):
        self.memory = Memory()

    def chat(self, message: str) -> dict:
        self.memory.add({"role": "user", "content": message})
        reply = (
            "Recebi sua mensagem. O núcleo da Kinex IA está funcionando, "
            "mas o modelo próprio ainda será conectado nesta etapa."
        )
        self.memory.add({"role": "assistant", "content": reply})
        return {
            "reply": reply,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "memory_items": self.memory.count(),
        }
