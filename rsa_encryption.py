import rsa
import base64

def generate_keys():
    (public_key, private_key) = rsa.newkeys(512)
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1("PEM"))
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1("PEM"))
    return public_key

def encrypt_words(words, public_key):
    with open("encrypted_message.txt", "w", encoding="utf-8") as file:
        for word in words:
            encrypted = rsa.encrypt(word.encode("utf-8"), public_key)
            encoded = base64.b64encode(encrypted).decode("utf-8")
            file.write(encoded + "\n")
    print("Οι λέξεις κρυπτογραφήθηκαν και αποθηκεύτηκαν στο 'encrypted_message.txt'.")

def main():
    message = input("Δώσε λέξεις χωρισμένες με κενό για κρυπτογράφηση: ")
    words = message.strip().split()
    public_key = generate_keys()
    encrypt_words(words, public_key)

if __name__ == "__main__":
    main()
