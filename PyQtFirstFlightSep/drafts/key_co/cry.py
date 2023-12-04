from cryptography.fernet import Fernet

# generate a new encryption key
key = Fernet.generate_key()

# create a Fernet object with the key
fernet = Fernet(key)

# encrypt the password
password = "my_password".encode()
encrypted_password = fernet.encrypt(password)

# decrypt the password
decrypted_password = fernet.decrypt(encrypted_password).decode()

print(f"Original password: {password.decode()}")
print(f"Encrypted password: {encrypted_password}")
print(f"Decrypted password: {decrypted_password}")
print(password)