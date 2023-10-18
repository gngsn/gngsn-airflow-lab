from dataclasses import dataclass

@dataclass
class Message:
    def __init__(
        self, id: int, schedule: list[str], condition: list[str], message: str, target: list[str], argument: list[dict]
    ) -> None:
        self.id = id
        self.schedule = schedule
        self.condition = condition
        self.message = message
        self.target = target
        self.argument = argument

