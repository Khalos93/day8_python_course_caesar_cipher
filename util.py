alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_direction_valid(user_direction: str, valid_directions) -> bool:
    return user_direction in valid_directions


def validate_text(message: str) -> bool:
    validation_outcome = True
    for char in message:
        if char not in alphabet and char != " ":
            validation_outcome = False

    if len(message) < 1:
        validation_outcome = False

    return validation_outcome


def validate_shift(steps: int) -> bool:
    if - 25 > steps > 25:
        return False
    else:
        return True


def encrypt(message: str, steps_variance: int) -> str:
    encrypted_message = ""

    for char in message:
        new_index = steps_variance
        if char in alphabet:

            new_index = new_index + alphabet.index(char)
            new_index %= 26
            encrypted_message += alphabet[new_index]
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(message: str, steps_variance: int) -> str:
    decrypted_message = ""

    for char in message:
        new_index = steps_variance * -1
        if char in alphabet:

            new_index = new_index + (alphabet.index(char) % 26)
            decrypted_message += alphabet[new_index]
        else:

            decrypted_message += char
    return decrypted_message
