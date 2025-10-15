from util import is_direction_valid, validate_text, validate_shift, encrypt, decrypt

encode = "encode"
decode = "decode"

possible_directions = (encode, decode)

using_the_program = True

while using_the_program:

    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    direction_successful = is_direction_valid(direction, possible_directions)

    while not direction_successful:
        direction = input("Wrong input! Type correctly 'encode' to encrypt, 'decode' to decrypt:\n").lower()
        direction_successful = is_direction_valid(direction, possible_directions)

    text = input("Type your message:\n").lower()
    is_text_valid = validate_text(text)
    while not is_text_valid:
        text = input("Wrong input! Type a valid message please:\n").lower()
        is_text_valid = validate_text(text)

    shift = int(input("Type the shift number:\n"))
    is_shift_valid = validate_shift(shift)
    while not is_shift_valid:
        shift = int(input("Type a valid shift number:\n"))
        is_shift_valid = validate_shift(shift)

    cipher_func = encrypt if direction == encode else decrypt
    print(cipher_func(text, shift))

    keep_using_the_cipher = input("Do you want to encode / decode more ? Y or N").lower()

    if keep_using_the_cipher == 'n':
        using_the_program = False
