import pytest
from caesar_cipher import encrypt, decrypt
import random


def test_decrypt_random():
    org_sent = '“we are currently in project week and im excited!!.”'
    encrypted = encrypt(org_sent, random.randint(1, 26))
    assert org_sent == decrypt(encrypted)
