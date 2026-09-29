
import secrets
import string

def generate_password(length=16):
    if length < 8:
        raise ValueError("Пароль должен быть не короче 8 символов")

    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password


if __name__ == "__main__":
    try:
        length = int(input("Длина пароля: "))
        password = generate_password(length)
        print(f"\nТвой пароль: {password}")
    except ValueError as error:
        print(f"Ошибка: {error}")