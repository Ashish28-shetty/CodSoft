import random
import string
def generate_password(length: int) -> str:
    if length <= 0:
        raise ValueError("Password length must be greater than 0")
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )
    return "".join(random.choice(characters) for _ in range(length))
def main() -> None:
    print("Password Generator")
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as error:
        print(f"Error: {error}")
if __name__ == "__main__":
    main()
