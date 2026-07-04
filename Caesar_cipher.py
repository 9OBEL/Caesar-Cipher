def caesar(text, shift, encrypt=True):
    """
    Performs Caesar cipher encryption or decryption on a given string.
    """
    # Validate that the shift value is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Ensure the shift is within the standard alphabet range
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse the shift direction
    if not encrypt:
        shift = - shift

    # Create the shifted alphabet mapping
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create translation table for both lowercase and uppercase letters
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    # Apply the translation
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    """Wrapper function to encrypt text."""
    return caesar(text, shift)


def decrypt(text, shift):
    """Wrapper function to decrypt text."""
    return caesar(text, shift, encrypt=False)


# Example Usage
encrypted_text = caesar("Nobel Paul Gill", 4)
print(f"Encrypted: {encrypted_text}")

decrypted_text = decrypt('Rsfip Teyp Kmpp', 4)
print(f"Decrypted: {decrypted_text}")