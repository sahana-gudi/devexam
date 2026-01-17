def multiplication(num: float) -> float:
    return num * 5

if __name__ == "__main__":
    try:
        args = __builtins__.__dict__.get('argv', [])
        if len(args) < 2:
            raise ValueError("No number provided")
        num = float(args[1])
        result = multiplication(num)
        print(f"{num} multiplied by 5 is {result}")
    except ValueError:
        print("Invalid input")
