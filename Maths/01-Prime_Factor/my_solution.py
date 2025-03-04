from challenge import Challenge  # Importing the Challenge class


def my_solver(challenge: Challenge):  # Defining your solver
    data = challenge.data  # Storing our challenge data
    factors = []

    while data % 2 == 0:
        factors.append(2)
        data //= 2

    for i in range(3, int(data**0.5) + 1, 2):
        while data % i == 0:
            factors.append(i)
            data //= i

    if data > 2:
        factors.append(data)

    return factors  # Don't forget to return your solution!


if __name__ == "__main__":
    my_challenge = Challenge()  # Creating an instance of the Challenge class
    raw_data = my_challenge.data  # Storing our challenge data
    solution = my_solver(my_challenge)  # Running your solver and store what returns
    result = my_challenge.check_solution(solution)  # Checking the solution
    print(f"{raw_data} | {solution} | {result}")  # Print the final outcome

# need to fix so that it does not repeat numbers in the solution
