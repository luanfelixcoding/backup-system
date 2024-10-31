from cryptography.fernet import Fernet

key = Fernet.generate_key()
f: object = Fernet(key=key)

token = f.encrypt(bytes(input().strip(), "utf-8", "NAO FUNCIONOU"))
print(token)
print(f.decrypt(token=token))
