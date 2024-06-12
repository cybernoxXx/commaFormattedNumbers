def commaFormat(number):

    strNumber = (str(number))
    isFloating = False
    integerPart = ''
    decimalPart = ''
    commaConversion = ''
    countingComma = 0

    # Cycling the string number to split the decimal part and the integer part
    for element in strNumber:
        # Checking from left to right so if I found a point the remaining numbers are decimal part
        if element == '.':
            isFloating = True

        if isFloating:
            # I have no more integer part, I found a point
            decimalPart = decimalPart + element
        else:
            # Not found yet a point so it's integer part
            integerPart = integerPart + element

    # Adding comma to integer part, I consider the integer part from right to left
    for i in range(len(integerPart)-1, -1, -1):
        commaConversion = integerPart[i] + commaConversion
        countingComma += 1

        # If I consider three number and I'm not at the end of the integer part I add a comma
        if countingComma == 3 and i != 0:
            commaConversion = ',' + commaConversion
            # Restarting the counting to check if I have other 3 numbers after
            countingComma = 0

    return commaConversion + decimalPart


assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
