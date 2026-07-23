class ConversationMemory:
    def __init__(self, max_messages: int = 6):
        self.max_messages = max_messages
        self.messages = []

    def add_user_message(self, text: str):
        self.messages.append({
            "role": "user",
            "content": text
        })
        self._trim()

    def add_yaara_message(self, text: str):
        self.messages.append({
            "role": "assistant",
            "content": text
        })
        self._trim()

    def get_context(self) -> str:
        lines = []

        for msg in self.messages:
            speaker = "User" if msg["role"] == "user" else "YAARA"
            lines.append(f"{speaker}: {msg['content']}")

        return "\n".join(lines)

    def _trim(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]