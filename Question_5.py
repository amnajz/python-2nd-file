def caesar_cipher(text: str, shift: int = 3, mode: str = "encrypt")-> str:
    """
        Encrypts or decrypts text.

        Args:
            text (str): The text to be encrypted or decrypted
            shift (int, optional): The number of positions to shift each letter (Default: 3)
            mode (str, optional): Mode of operation "encrypt" or "decrypt" (Default: "encrypt")

        Returns:
            str: The encrypted or decrypted text.
    """
    result = ""
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result
