def convert_price(price):
    if price.text.strip() == 'توافقی':
        price = price.text.strip()
    else:
        price = float(price.text.replace(',', ''))


def convert_description(description):
    if description:
        description = description.text
    else:
        description = ''
