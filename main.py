import string

# Extended character set including letters, digits, and special symbols
alphabet = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " ")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            # If character is not in the alphabet, add it unchanged
            end_text += char
    return end_text

# Logo for fun (optional)
logo = """
   Brute Forcing Caesar Cipher Encryption   
"""
print(logo)

# Main program loop for brute-force decryption
should_end = False
while not should_end:
    encoded_message = input("Type the encoded message you want to brute-force:\n")
    print("Brute-force decryption in progress... This might take a while.")

    shift_key = 0
    while shift_key < len(alphabet):
        decoded_message = caesar(start_text=encoded_message, shift_amount=shift_key, cipher_direction="decode")
        print(f"Trying shift key {shift_key}: {decoded_message}")
        shift_key += 1

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye!")
