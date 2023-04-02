# Import necessary libraries
from eth_account import Account
from mnemonic import Mnemonic
import os
import sys
import secrets
import string
import csv
import json
from eth_keys import keys
from eth_utils import to_checksum_address
from bip32 import BIP32

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits

    # Generate the password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    # Format the password as XXXXX-XXXXX-XXXXX
    formatted_password = '-'.join([password[i:i + 5] for i in range(0, len(password), 5)])

    return formatted_password

def create_ethereum_account(mnemonic_phrase):
    seed = Mnemonic.to_seed(mnemonic_phrase)
    bip32_node = BIP32.from_seed(seed)
    eth_derivation_path = "m/44'/60'/0'/0/0"
    private_key = bip32_node.get_privkey_from_path(eth_derivation_path)
    private_key = keys.PrivateKey(private_key)
    address = private_key.public_key.to_checksum_address()
    return private_key.to_hex(), address

def create_multiple_accounts(n):
    accounts = []
    for _ in range(n):
        # Generate a new mnemonic phrase
        mnemonic = Mnemonic("english")
        mnemonic_phrase = mnemonic.generate()

        # Generate a strong password
        password = generate_password(15)

        private_key, address = create_ethereum_account(mnemonic_phrase)
        accounts.append({'address': address, 'private_key': private_key, 'mnemonic_phrase': mnemonic_phrase, 'password': password})
    return accounts

def save_accounts_to_csv(accounts, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['address', 'private_key', 'mnemonic_phrase', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for account in accounts:
            writer.writerow(account)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python account_generator.py <number_of_accounts> <output_file>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: The number of accounts must be an integer.")
        sys.exit(1)

    output_file = sys.argv[2]

    accounts = create_multiple_accounts(n)
    save_accounts_to_csv(accounts, output_file)

    print(f"{n} Ethereum accounts saved to {output_file}.")
