"""
Mamdouh Zayed
"""

def convert_to_words(num):
    # list of numbers as words
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if 1 <= num < 10:
        return units[num]
    elif 11 <= num < 20:
        return teens[num-10]
    elif 20 <= num < 100:
        return tens[num//10] + ('' if num%10 == 0 else ' ' + units[num%10])
    elif 100 <= num < 1000:
        return units[num//100] + ' hundred' + ('' if num%100 == 0 else ' ' + convert_to_words(num%100))
    elif 1000 <= num < 1000000:
        return convert_to_words(num//1000) + ' thousand' + ('' if num%1000 == 0 else ' ' + convert_to_words(num%1000))

def check_writer(dollars, cents):
    # convert dollars and cents into words
    dollars_in_words = convert_to_words(dollars) + ' dollars'
    cents_in_words = convert_to_words(cents) + ' cents'
    # combine the words for dollars and cents
    amount_in_words = dollars_in_words + ' and ' + cents_in_words
    return amount_in_words

print(check_writer(123, 45))