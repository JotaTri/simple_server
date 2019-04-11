# Simple Server

This repository was created for anyone who needs a simple to run server on a machine that outputs:

- Client IP and HTTP Method
- Client Designated endpoint
- HTTP Headers
- HTTP Body

It was designed for debugging applications that make HTTP requests of any kind, printing all important information in the transaction.

The debug mode is *on* by default, making it easier to edit the code and adapt it to any users needs.

## Running it

The file *requirements.txt* contains the Flask version in which this project was developed. Simply run the following command to have the correct Flask version on your environment

> pip install -r requirements.txt

After that, just run the *server.py* code

> python server.py