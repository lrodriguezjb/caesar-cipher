import random
from nltk.corpus import words
import nltk
nltk.download('words')

word_list = words.words()


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(words, key):
    encrypted_words = ''

    for char in words.lower():
        if char in alphabet:
            encrypted_letter = alphabet[(alphabet.index(
                char.lower()) + key) % len(alphabet)]
            encrypted_words += encrypted_letter
        else:
            encrypted_words += char
    return encrypted_words


def decrypt(words):

    def english_words(list_of_words):
        number_correct = 0
        for word in list_of_words:
            if word in word_list:
                number_correct += 1
        if number_correct/len(list_of_words) >= 0.5:
            return True
        return False

    for key in range(len(alphabet)):
        a = encrypt(words, (-1*(key)))
        b = english_words(a.split(' '))
        if b:
            return a


if __name__ == "__main__":
    topseccret_string = "“We are currently in Project Week and im excited!!.”"
    encrypted_string = encrypt(
        topseccret_string, random.randint(1, len(alphabet)))
    decrypted_string = decrypt(encrypted_string)
    print('original string: ', topseccret_string)
    print('')
    print(encrypted_string)
    print(decrypted_string)
