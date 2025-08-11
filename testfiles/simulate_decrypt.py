from cryptography.fernet import Fernet
import os

def decrypt_files(folder, key):
    cipher = Fernet(key)
    for filename in os.listdir(folder):
        if filename.endswith(".locked"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            original_filename = filepath.replace(".locked", "")
            with open(original_filename, "wb") as file:
                file.write(decrypted_data)
            os.remove(filepath)
    print("Files decrypted successfully.")

def main():
    folder = r"C:\Users\USER 1\testfiles"
    key = input("Enter the decryption key: ").encode()
    decrypt_files(folder, key)
    print("Your files have been decrypted.")

if __name__ == "__main__":
    main()
