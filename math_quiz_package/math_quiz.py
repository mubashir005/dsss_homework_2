import random


def random_integer(min_val, max_val):
    """Generate a random integer within the specified range."""
    return random.randint(min_val, max_val)


def random_operator():
    """Generate a random arithmetic operator (+, -, *)."""
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer():
    """Generate a random math problem and its correct answer."""
    n1, n2 = random_integer(1, 10), random_integer(1, 5)
    operator = random_operator()

    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2

    problem = f"{n1} {operator} {n2}"
    return problem, answer


def math_quiz(total_questions):
    """Conduct a math quiz game with a specified number of questions."""
    score = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        problem, answer = generate_problem_and_answer()
        print(f"\nQuestion: {problem}")

        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz(3)  # Specify the number of questions as an argument
