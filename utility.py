def convert_price(price):
    if price.text.strip() == 'توافقی':
        return price.text.strip()
    else:
        return float(price.text.replace(',', ''))


def convert_description(description):
    if description:
        return description.text
    else:
        return ''
