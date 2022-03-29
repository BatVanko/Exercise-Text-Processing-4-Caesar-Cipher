text = input()
encrypted_text = "".join([chr(ord(x)+3) for x in text])
print(encrypted_text)