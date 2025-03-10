class Challenge:
    def __init__(self):
        self.data = (
            "The solution to this challenge is a list containing the string `o7`."
        )
        """The `data` property contains the data you need to complete the challenge.
        (In this instance, these are just instructions.)"""

    def check_solution(self, solution) -> bool:
        """The `check_solution` method is used to make sure your solution is correct.
        (You can often check the type-hinting if you are getting any type errors.)"""
        return True if solution == ["o7"] and len(solution) == 1 else False
