org_message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 3

# make all characters upper case
org_message = org_message.upper()
encrypt_message = ''
# print all character
for org_character in org_message:

    if org_character in alphabet:
        org_position = alphabet.find(org_character)
        new_position = org_position + key

        if new_position > (len(alphabet) - 1):
            new_position = new_position - len(alphabet)
        new_character = alphabet[new_position]

    else:
        new_character = org_character

    encrypt_message = encrypt_message + new_character

print(encrypt_message)
