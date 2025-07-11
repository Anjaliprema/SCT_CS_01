def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # check if character is alphabet
            shift_amount = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_message += char  # Non-alphabetic characters are not shifted
    return encrypted_message

def decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():  # check if character is alphabet
            shift_amount = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift - shift_amount) % 26 + shift_amount)
        else:
            decrypted_message += char  # Non-alphabetic characters are not shifted
    return decrypted_message

def main():
    while True:
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1 or 2 or 3): ")
       
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
       
        elif choice == '2':
            encrypted_message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(encrypted_message, shift)
            print(f"Decrypted Message: {decrypted_message}")
       
        elif choice == '3':
            print("Exiting the program.")
            break
       
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
