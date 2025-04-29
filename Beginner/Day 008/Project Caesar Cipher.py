alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, encode_or_decode):
    new_text = ""
    if encode_or_decode == "decode":
        shift *= -1
    for char in text:
        if char not in alphabet:
            new_text += char
        else:
            new_index_number = (alphabet.index(char) + shift) % len(alphabet)
            new_text += alphabet[new_index_number]
    print(f"here is the {encode_or_decode}d result: {new_text}")

program_over = False
while not program_over:
    direction = input("type 'encode' to encrypt,\ntype 'decode' to decrypt: ").lower()
    if direction != "encode" and direction != "decode":
        print("wrong input")
    else:
        text = input("type your message: ").lower()
        shift = int(input("type the shift number: "))
        caesar(text, shift, direction)
        ask_flag = False
        while not ask_flag:
            ask_again = input("do you want to try it again? (Y/N)").lower()
            if ask_again == "n":
                print("thank you for using our program")
                program_over = True
                ask_flag = True
            elif ask_again == "y":
                ask_flag = True
                print("Goodbye")
            else:
                print("wrong input")