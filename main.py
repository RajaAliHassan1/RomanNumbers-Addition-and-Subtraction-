def ConvertToNumericChar (char):
    if char == "I" or char == "i":
        return 1
    elif char == "V" or char == "v":
        return 5
    elif char == "X" or char == "x":
        return 10
    elif char == "L" or char == "l":
        return 50
    elif char == "C" or char == "c":
        return 100
    elif char == "D" or char == "d":
        return 500
    elif char == "M" or char == "m":
        return 1000

def ConvertToRoman(Numeric):
    RomanExpression = ""
    while Numeric > 0:
        if Numeric >= 1000:
            RomanExpression = RomanExpression + "M"
            Numeric = Numeric - 1000
        elif Numeric >= 500:
            RomanExpression = RomanExpression + "D"
            Numeric = Numeric - 500
        elif Numeric >= 100:
            RomanExpression = RomanExpression + "C"
            Numeric = Numeric - 100
        elif Numeric >= 50:
            RomanExpression = RomanExpression + "L"
            Numeric = Numeric - 50
        elif Numeric >= 10:
            RomanExpression = RomanExpression + "X"
            Numeric = Numeric - 10
        elif Numeric >= 5:
            RomanExpression = RomanExpression + "V"
            Numeric = Numeric - 5
        elif Numeric >= 1:
            RomanExpression = RomanExpression + "I"
            Numeric = Numeric - 1

    return RomanExpression
def ConvertToNumeric(RomanNumber):
    i = 1
    NumericValue = ConvertToNumericChar(RomanNumber[0])
    while i < len(RomanNumber):
        if (i != len(RomanNumber)-1) and (ConvertToNumericChar(RomanNumber[i]) < ConvertToNumericChar(RomanNumber[i+1])):
             NumericValue = NumericValue + (ConvertToNumericChar(RomanNumber[i+1]) - ConvertToNumericChar(RomanNumber[i]))
             i = i+1

        elif NumericValue >= ConvertToNumericChar(RomanNumber[i]):
            NumericValue = ConvertToNumericChar(RomanNumber[i]) + NumericValue

        elif NumericValue < ConvertToNumericChar(RomanNumber[i]):
            if ConvertToNumericChar(RomanNumber[i]) == ConvertToNumericChar(RomanNumber[i-1]):
                NumericValue = NumericValue + ConvertToNumericChar(RomanNumber[i])
            else:
                NumericValue = ConvertToNumericChar(RomanNumber[i]) - NumericValue
        i = i + 1
    print(NumericValue)

    return NumericValue



input1 = (input("Input 1 Roman"))
input2 = (input("Input 2 Roman"))
input3 = (input("Input Operation + or -"))


number1 = int (ConvertToNumeric(input1))
number2 = int(ConvertToNumeric(input2))

result = 0
if input3 == '+':
    result = number1 + number2
else:
    result = number1 - number2

print("Result is ")
print(ConvertToRoman(result))
