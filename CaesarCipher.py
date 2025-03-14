def caesar_cipher(text, shift, decrypt=False):
    
    if decrypt:
        shift = -shift

    result = []
    for char in text:
        if char.isupper():
            
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            
            result.append(char)

    return ''.join(result)

def main():
    print(" Caesar Cipher Program")

    
    while True:
        mode = input("\nChoose mode (encrypt/decrypt/exit): ").strip().lower()

        if mode == "exit":
            print("Exiting the program. Goodbye!")
            break

        if mode not in ["encrypt", "decrypt"]:
            print("Invalid mode! Use 'encrypt', 'decrypt', or 'exit'.")
            continue

        text = input("Enter the message: ")
        
        try:
            shift = int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        output = caesar_cipher(text, shift, decrypt=(mode == "decrypt"))
        print(f"\n Result ({mode}ed message): {output}")

if __name__ == "__main__":
    main()
