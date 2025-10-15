from util import is_direction_valid, validate_text, validate_shift, encrypt, decrypt

encode = "encode"
decode = "decode"

possible_directions = (encode, decode)

using_the_program = True

while using_the_program:

    direction = input("Type 'encode' to encrypt, 'decode to decrypt:\n").lower()
    direction_successful = is_direction_valid(direction, possible_directions)

    while not direction_successful:
        direction = input("Wrong input! Type correctly 'encode' to encrypt, 'decode' to decrypt:\n").lower()
        direction_successful = is_direction_valid(direction, possible_directions)

    text = input("Type your message:\n").lower()
    next_step = validate_text(text)
    while not next_step:
        text = input("Wrong input! Type a valid message please:\n").lower()
        next_step = validate_text(text)

    shift = int(input("Type the shift number:\n"))
    further_step = validate_shift(shift)
    while not further_step:
        shift = int(input("Type a valid shift number:\n"))
        further_step = validate_shift(shift)

    if direction == encode:
        print(encrypt(text, shift))

    else:
        print(decrypt(text, shift))



