from domain import Greeting, GreetingRepository


class GreetUserUseCase:
    """Application logic — depends only on the domain port, never on infra."""

    def __init__(self, repo: GreetingRepository):
        self._repo = repo

    def execute(self, recipient: str) -> Greeting:
        greeting = self._repo.get_greeting(recipient)
        self._repo.save_greeting(greeting)
        return greeting
