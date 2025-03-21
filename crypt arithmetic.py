from itertools import permutations
letters = 'SENDMORY'
digits = permutations('0123456789', len(letters))
def to_number(s, mapping):
    return int(''.join(mapping[c] for c in s))
for mapping in digits:
    letter_to_digit = dict(zip(letters, mapping))
    if letter_to_digit['S'] == '0' or letter_to_digit['M'] == '0':
        continue
    send = to_number('SEND', letter_to_digit)
    more = to_number('MORE', letter_to_digit)
    money = to_number('MONEY', letter_to_digit)
    if send + more == money:
        print(f"SEND + MORE = MONEY")
        print(f"{send} + {more} = {money}")
        break
