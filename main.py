from infra.mock_greeting_repository import MockGreetingRepository
from usecase.greet_user import GreetUserUseCase


def main():
    # Dependency wiring: inject the mock adapter into the use case
    repo = MockGreetingRepository()
    use_case = GreetUserUseCase(repo=repo)

    result = use_case.execute("World")
    print(result.message)

    result2 = use_case.execute("Clean Architecture")
    print(result2.message)
    print("the change made at xinpu")


if __name__ == "__main__":
    main()
