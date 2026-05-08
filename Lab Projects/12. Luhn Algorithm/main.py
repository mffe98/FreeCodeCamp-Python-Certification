def verify_card_number(id_string):
    id_string = ''.join(id_string.replace('-','').split())
    account_num = [int(num) for num in id_string[:-1]]
    check_digit = int(id_string[-1])

    processed_num = []
    for index, digit in enumerate(account_num[::-1]):
        if index % 2 == 0:
            digit *= 2
        if digit > 9:
            digit -= 9
        processed_num.append(digit)

    is_valid = (sum(processed_num) + check_digit) % 10 == 0
 
    return 'VALID!' if is_valid else 'INVALID!'

