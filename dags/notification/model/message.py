from dataclasses import dataclass


@dataclass
class Message:
    def __init__(
        self, title: str, content: str
    ) -> None:
        self.title = title
        self.content = content
