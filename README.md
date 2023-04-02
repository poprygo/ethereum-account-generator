# Ethereum Account Generator

This script generates Ethereum accounts with addresses, private keys, seed phrases, and strong passwords.

## Prerequisites

- Python 3.6 or later

## Setup

1. Clone this repository or download the files.
2. Open Terminal on macOS and navigate to the project directory.
3. Create a virtual environment and activate it:

        python3 -m venv venv
        source venv/bin/activate 
        

4. Install the required libraries:

        pip install -r requirements.txt


## Usage

To generate a specified number of Ethereum accounts and save them to a CSV file, run the following command:

        python account_generator.py <number_of_accounts> <output_file>


Replace `<number_of_accounts>` with the desired number of accounts to generate and `<output_file>` with the name of the output CSV file.

For example:

        python account_generator.py 10 accounts.csv


This will generate 10 Ethereum accounts and save the data to a file named `accounts.csv`.


## Important Note

The generated account data contains sensitive information. Handle it with care and avoid storing it on publicly accessible platforms without proper access control and encryption.

## Warning
Keep the private keys safe and secret, as anyone with access to a private key can control the associated Ethereum account and its assets. Do not share your private keys with anyone.

## License
This project is available under the MIT License.

This `README.md` file provides a brief introduction to the Ethereum Account Generator script, instructions for installing the required library, usage information, and a warning about keeping private keys safe. You can customize the content as needed for your specific project.
