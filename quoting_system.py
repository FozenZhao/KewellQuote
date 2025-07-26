"""Simple quoting system using JSON files for storage."""
import argparse
from datetime import datetime
from typing import Optional

from storage import load_json, save_json


def add_product(name: str, price: float) -> None:
    products = load_json('products')
    pid = len(products) + 1
    products.append({'id': pid, 'name': name, 'price': price})
    save_json('products', products)
    print(f'Product added with id {pid}')


def list_products() -> None:
    products = load_json('products')
    for p in products:
        print(f"{p['id']}: {p['name']} - {p['price']}")


def add_customer(name: str, email: str) -> None:
    customers = load_json('customers')
    cid = len(customers) + 1
    customers.append({'id': cid, 'name': name, 'email': email})
    save_json('customers', customers)
    print(f'Customer added with id {cid}')


def list_customers() -> None:
    customers = load_json('customers')
    for c in customers:
        print(f"{c['id']}: {c['name']} <{c['email']}>")


def create_quote(customer_id: int, product_id: int, quantity: int) -> None:
    quotes = load_json('quotes')
    qid = len(quotes) + 1
    quote = {
        'id': qid,
        'customer_id': customer_id,
        'product_id': product_id,
        'quantity': quantity,
        'approved': False,
        'approved_by': None,
        'approved_at': None,
        'sent': False,
        'sent_at': None,
    }
    quotes.append(quote)
    save_json('quotes', quotes)
    print(f'Quote created with id {qid}')


def list_quotes() -> None:
    quotes = load_json('quotes')
    for q in quotes:
        print(f"Quote {q['id']} -> customer {q['customer_id']} product {q['product_id']} qty {q['quantity']} approved {q['approved']} sent {q['sent']}")


def approve_quote(qid: int, user: str) -> None:
    quotes = load_json('quotes')
    for q in quotes:
        if q['id'] == qid:
            if q['approved']:
                print('Quote already approved')
                return
            q['approved'] = True
            q['approved_by'] = user
            q['approved_at'] = datetime.utcnow().isoformat()
            save_json('quotes', quotes)
            print('Quote approved')
            return
    print('Quote not found')


def send_quote(qid: int) -> None:
    quotes = load_json('quotes')
    for q in quotes:
        if q['id'] == qid:
            if not q['approved']:
                print('Quote not approved yet')
                return
            if q['sent']:
                print('Quote already sent')
                return
            q['sent'] = True
            q['sent_at'] = datetime.utcnow().isoformat()
            save_json('quotes', quotes)
            print(f"Quote {qid} sent (simulated)")
            return
    print('Quote not found')


def main(argv: Optional[list] = None) -> None:
    parser = argparse.ArgumentParser(description='Simple quoting system')
    sub = parser.add_subparsers(dest='command', required=True)

    p_add_product = sub.add_parser('add-product')
    p_add_product.add_argument('name')
    p_add_product.add_argument('price', type=float)

    p_list_products = sub.add_parser('list-products')

    p_add_customer = sub.add_parser('add-customer')
    p_add_customer.add_argument('name')
    p_add_customer.add_argument('email')

    p_list_customers = sub.add_parser('list-customers')

    p_create_quote = sub.add_parser('create-quote')
    p_create_quote.add_argument('customer_id', type=int)
    p_create_quote.add_argument('product_id', type=int)
    p_create_quote.add_argument('quantity', type=int)

    p_list_quotes = sub.add_parser('list-quotes')

    p_approve_quote = sub.add_parser('approve-quote')
    p_approve_quote.add_argument('quote_id', type=int)
    p_approve_quote.add_argument('user')

    p_send_quote = sub.add_parser('send-quote')
    p_send_quote.add_argument('quote_id', type=int)

    args = parser.parse_args(argv)

    if args.command == 'add-product':
        add_product(args.name, args.price)
    elif args.command == 'list-products':
        list_products()
    elif args.command == 'add-customer':
        add_customer(args.name, args.email)
    elif args.command == 'list-customers':
        list_customers()
    elif args.command == 'create-quote':
        create_quote(args.customer_id, args.product_id, args.quantity)
    elif args.command == 'list-quotes':
        list_quotes()
    elif args.command == 'approve-quote':
        approve_quote(args.quote_id, args.user)
    elif args.command == 'send-quote':
        send_quote(args.quote_id)


if __name__ == '__main__':
    main()
