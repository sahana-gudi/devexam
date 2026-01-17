def multiplication(num: float) -> float:
    return num * 5

if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        result = multiplication(num)
        print(f"{num} multiplied by 5 is {result}")
    except ValueError:
        print("Invalid given")