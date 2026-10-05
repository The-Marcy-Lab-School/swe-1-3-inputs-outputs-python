def order_summary():
    item = "Coffee"
    quantity = 2
    price = 3.5
    is_gift = True

    print(f"{quantity} x {item}")
    print(f"Total: ${quantity * price:.2f}")
    if is_gift:
        print("Gift wrapped.")


def print_receipt(items, total):
    for item in items:
        print(item)
    print("-----")
    print("Total:")
    print(total)
