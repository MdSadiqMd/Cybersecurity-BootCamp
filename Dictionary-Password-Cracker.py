import bcrypt

def test_pass(crypt_pass, salt):
    dict_file = open('dictionary', 'r')
    for word in dict_file:
        hashed_word = bcrypt.hashpw(word.strip('\n').encode(), salt.encode())

        if hashed_word.decode() == crypt_pass:
            print(f'[+] Found Password: {word}\n')
            return
    print('[-] Password Not Found.\n')


if __name__ == '__main__':
    pass_file = open('passwords.txt', 'r')
    for line in pass_file:
        if ':' in line:
            user, _crypt_pass = line.split(':')
            _crypt_pass = _crypt_pass.strip()
            salt = _crypt_pass[:29]  # Extract the salt from the hash
            print(f'[*] Cracking Password For: {user}')
            test_pass(_crypt_pass, salt)
