from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Greeting:
    message: str
    recipient: str


class GreetingRepository(ABC):
    @abstractmethod
    def get_greeting(self, recipient: str) -> Greeting:
        ...

    @abstractmethod
    def save_greeting(self, greeting: Greeting) -> None:
        ...
