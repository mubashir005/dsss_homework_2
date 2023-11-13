import random

MIN_VALUE = 1
MAX_VALUE_N1 = 10
MAX_VALUE_N2 = 5


def random_integer(min_val, max_val):
    return random.randint(min_val, max_val)


def random_operator():
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer():
    n1 = random_integer(MIN_VALUE, MAX_VALUE_N1)
    n2 = random_integer(MIN_VALUE, MAX_VALUE_N2)
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
    math_quiz(3)
