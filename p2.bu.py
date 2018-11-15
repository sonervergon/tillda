answer = []

def answerIsPositive(N1, N2):
    positiveAnswer = (N1 <= 0 and N2 <= 0) or (N1 >= 0 and N2 >= 0)
    if not positiveAnswer:
        answer.append('-')

def processNumbers(N1, N2, method):
    N1 = abs(N1)
    N2 = abs(N2)
    if method == 'div':
        N1 = str(abs(N1))
        N2 = str(abs(N2))
    return N1, N2

def mult(N1, N2):
    answerIsPositive(N1, N2)
    N1, N2 = processNumbers(N1, N2, 'mult')
    if N1 > N2:
        temp = N1
        N1 = N2
        N2 = temp
    localAnswer = 0
    for value, index in enumerate(range(0, N1)):
        localAnswer = localAnswer + N2
    return localAnswer

def getNumber(numerator, denominator, rest, count):
    number, newNumerator, denominator = int(numerator[0]), '', int(denominator)
    if len(numerator) > 1:
        newNumerator = numerator[1:]
    index = 1
    while int(number) < denominator or (int(number) == 0 and len(numerator) > index):
        index = index + 1
        print('Number: ',int(number))
        print('Numerator: ', numerator)
        print('Rest: ',rest)
        if  len(numerator) <= index:
            newNumerator = ''
        if count != 0 and (int(numerator) < denominator) and int(number) != int(numerator):
            print('Append 1')
            answer.append('0')
        if rest != 0 and rest < int(number) and len(numerator) > 0:
            print('Append 2')
            answer.append('0')
        string = numerator[0:index]
        stringRest = numerator[index:]
        number = string
        if len(numerator) > 1:
            newNumerator = stringRest
        if newNumerator == '':
            break
        print('Numerator: ',numerator)
        print('_______NEW_LAP_______')
    print('Laps: ', index-1)
    return number, newNumerator

def divide(numberToDivide, numerator, denominator):
    denominator = int(denominator)
    quotient = 0
    localDenominator = denominator
    while localDenominator <= int(numberToDivide):
        localDenominator = localDenominator + denominator
        quotient = quotient + 1
    if int(numberToDivide) != 0:
        answer.append(str(quotient))
    rest = int(numberToDivide) - mult(quotient, denominator)
    return rest

def div(numerator, denominator):
    answerIsPositive(numerator, denominator)
    numerator, denominator = processNumbers(numerator, denominator, 'div')
    rest = 0
    count = 0
    while len(numerator) != 0:
        numberToDivide, newNumerator = getNumber(numerator, denominator, rest, count)
        rest = divide(numberToDivide, newNumerator, denominator)
        print('Number to Divide: ', numberToDivide)
        print('Numerator: ', newNumerator)
        print('Rest: ', rest)
        numerator = str(rest) + str(newNumerator)
        if len(str(newNumerator)) == 0:
            break
        count = count + 1
        print('##########################')

def main():
    global answer
    div(420, 4)
    print(''.join(answer))

if __name__ == "__main__":
    main()
