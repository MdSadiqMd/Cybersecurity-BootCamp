import hashlib


def read_dictionary(dictionary):
    with open(dictionary, 'r') as file:
        return [line.strip() for line in file]


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def crack_password(target_hash, dictionary):
    for word in dictionary:
        hashed_word = hash_password(word)
        if hashed_word == target_hash:
            return word
    return None


if __name__ == "__main__":
    target_hash = "f464d7d71c06e47a535ce441aa202aa717cddeab902a45b0c283aac7a9a090d7"
    dictionary_file = "dictionary"
    dictionary = read_dictionary(dictionary_file)
    print("Dictionary loaded:", dictionary)

    for word in dictionary:
        hashed_word = hash_password(word)
        print(f"Word: {word}, Hash: {hashed_word}")

        if hashed_word == target_hash:
            print("Match found!")
            cracked_password = word
            break
    else:
        cracked_password = None

    if cracked_password:
        print(f"Password Cracked! The password is: {cracked_password}")
    else:
        print("Password Not found in Dictionary")
