#!/usr/bin/env python

import os
import pickle
import Crypto.Random
from Crypto.Cipher import AES
import hashlib

SECRETSDB_FILE = os.environ['FREE_OFFERING_WORKSPACE']+'/config'
# salt size in bytes
SALT_SIZE = 16
# number of iterations in the key generation
NUMBER_OF_ITERATIONS = 20
# the size multiple required for AES
AES_MULTIPLE = 16
PASSWORD = 'somepassword'  # change to the actual password, this will be used to store and retrive keys from config file


def generate_key(password, salt, iterations):
    assert iterations > 0
    key = ('%s%s' % (salt, password)).encode('utf-8')
    for i in range(iterations):
        key = hashlib.sha256(key).digest()
    return key


def pad_text(text, multiple):
    extra_bytes = len(text) % multiple
    padding_size = multiple - extra_bytes
    padding = chr(padding_size) * padding_size
    padded_text = text + padding
    return padded_text


def unpad_text(padded_text):
    padding_size = padded_text[-1]
    text = padded_text[:-padding_size]
    return text


def encrypt(plaintext, password):
    salt = Crypto.Random.get_random_bytes(SALT_SIZE)
    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad_text(plaintext, AES_MULTIPLE)
    ciphertext = cipher.encrypt(padded_plaintext.encode("utf-8"))
    ciphertext_with_salt = salt + ciphertext
    return ciphertext_with_salt


def decrypt(ciphertext, password):
    salt = ciphertext[0:SALT_SIZE]
    ciphertext_sans_salt = ciphertext[SALT_SIZE:]
    key = generate_key(password, salt, NUMBER_OF_ITERATIONS)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext_sans_salt)
    plaintext = unpad_text(padded_plaintext)
    return plaintext.decode("utf-8")

# User Functions #


def store(key, value):
    ''' Sore key-value pair safely and save to disk.'''
    db[key] = encrypt(value, PASSWORD)
    with open(SECRETSDB_FILE, 'wb') as f:
        pickle.dump(db, f)


def retrieve(key):
    ''' Fetch key-value pair.'''
    return decrypt(db[key], PASSWORD)


def load():
    # Load or create secrets database:
    global db
    try:
        with open(SECRETSDB_FILE, 'rb') as f:
            db = pickle.load(f)
        if db == {}:
            raise IOError
    except (IOError, EOFError):
        db = {}
        with open(SECRETSDB_FILE, 'wb') as f:
            pickle.dump(db, f)
