class HelloSolution:
    # friend_name = unicode string
    def hello(self, friend_name: str | None) -> str:
        if friend_name is None:
            raise ValueError("friend_name cannot be None")

        if len(friend_name) > 100:
            raise ValueError("friend_name must be less than 100")

        return f"Hello, {friend_name}!"
