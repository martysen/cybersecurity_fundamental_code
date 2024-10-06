'''
encryption and decryption using vigenere cipher
plaintext: ATTACKATDAWN (total characters: 12 )
KEY: LEMON (total characters: 5)
A-Z: 65-90
a-z: 97-122
ATTACKATDAWN
LEMONLEMONLE
plaintext[1] =
if we have a list of length/size n=12,
first index of list is 0
and last index is n-1 (11)
traverse the list-- travel from the first to last index one index at time
repeating / loop over lets say list; implement using FOR LOOPS 
for (start-end):
  specify logic to execute on each loop iteration

coding: decision making if length of key is equal to length of message 
if age is x then do something else if age is > x do something else, otherwise some other case
==, >, <, >=, <=, != 
condition --> true or false
if - else statements
if - elese if statemetns 
if(condition1):
  logic for true part
elif(condition2):
  logic for 2nd true part
else:
  logic for false part

0. generate the key
1. encryption function 
2. decryption function 
'''
def generate_vigenere_key(plaintext, secret_key):
  secret_key = list(secret_key)
  if len(plaintext) == len(secret_key):
    return secret_key
  else:
    for i in range(len(plaintext) - len(secret_key)):
      secret_key.append(secret_key[i % len(secret_key)])
  return "".join(secret_key)

def encrypt_vigenere(plaintext, secret_key):
  encrypted_text = []
  secret_key = generate_vigenere_key(plaintext, secret_key)
  print(f"modified secret key for encryption is: {secret_key}")
  for i in range(len(plaintext)):
    char = plaintext[i]
    if char.isupper() and secret_key[i].isupper():
      encrypted_char = chr((ord(char) + ord(secret_key[i]) - 2 * ord('A')) % 26 + ord('A'))
    elif char.islower():
      encrypted_char = chr((ord(char) + ord(secret_key[i]) - 2 * ord('a')) % 26 + ord('a'))
    else:
      encrypted_char = char
    encrypted_text.append(encrypted_char)
  return "".join(encrypted_text)

def decrypt_vigenere(ciphertext, secret_key):
  decrypted_text = []
  secret_key = generate_vigenere_key(ciphertext, secret_key)
  print(f"modified secret key for decryption is: {secret_key}")
  print(f"ciphertext for decryption is: {ciphertext}")
  for i in range(len(ciphertext)):
    char = ciphertext[i]
    if char.isupper():
      decrypted_char = chr((ord(char) - ord(secret_key[i]) + 26) % 26 + ord('A'))
    elif char.islower():
      decrypted_char = chr((ord(char) - ord(secret_key[i]) + 26) % 26 + ord('a'))
    else:
      decrypted_char = char
    decrypted_text.append(decrypted_char)
  return "".join(decrypted_text)

# implement or call the functions above.
user_input = "attackatdawn"
user_key = "lemon"

print(f"input plaintext is: {user_input}")
print(f"secret key is: {user_key}")

user_output_encryption = encrypt_vigenere(user_input, user_key)
print(f"Encrypted Text is: {user_output_encryption}")

user_output_decryption = decrypt_vigenere(user_output_encryption, user_key)
print(f"Decrypted Text is: {user_output_decryption}")