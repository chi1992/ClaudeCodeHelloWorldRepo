from domain import Greeting, GreetingRepository


class MockGreetingRepository(GreetingRepository):
    """In-memory adapter — stands in for a real DB or external service."""

    def __init__(self):
        self._store: dict[str, Greeting] = {}

    def get_greeting(self, recipient: str) -> Greeting:
        if recipient not in self._store:
            return Greeting(message=f"Hello, {recipient}!", recipient=recipient)
        return self._store[recipient]

    def save_greeting(self, greeting: Greeting) -> None:
        self._store[greeting.recipient] = greeting
