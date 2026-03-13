def get_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def get_operation() -> str:
    while True:
        op = input("Choose operation (+ or -): ").strip()
        if op in {"+", "-"}:
            return op
        print("Please enter + or -.")


def main() -> None:
    print("Simple Add/Subtract App")
    number_a = get_number("Number A: ")
    number_b = get_number("Number B: ")
    op = get_operation()

    if op == "+":
        result = number_a + number_b
    else:
        result = number_a - number_b

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
