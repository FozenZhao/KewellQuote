# KewellQuote

This repository contains a minimal command-line quoting system. It uses JSON files stored in the `data/` directory to keep track of products, customers and quotes.

## Requirements

The script only uses Python standard library and does not require any external dependencies. It has been tested with Python 3.12.

## Usage

```bash
# Add a product
python quoting_system.py add-product "Widget" 9.99

# List products
python quoting_system.py list-products

# Add a customer
python quoting_system.py add-customer "Acme" customer@example.com

# Create a quote for customer 1 and product 1
python quoting_system.py create-quote 1 1 5

# Approve the quote as manager
python quoting_system.py approve-quote 1 manager

# Send the quote (simulation)
python quoting_system.py send-quote 1
```
