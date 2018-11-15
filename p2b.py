answer = []

def answerIsPositive(N1, N2):
    positiveAnswer = (N1 <= 0 and N2 <= 0) or (N1 >= 0 and N2 >= 0)
    if not positiveAnswer:
        answer.append('-')

def processNumbers(N1, N2, method):
    N1 = abs(N1)
    N2 = abs(N2)
    if method == 'div':
        if N1 < N2:
            answer.append('0.')
        N1 = list(str(abs(N1)))
        N2 = list(str(abs(N2)))
    return N1, N2

def mult(N1, N2):
    answerIsPositive(N1, N2)
    N1, N2 = processNumbers(N1, N2, 'mult')
    if N1 > N2:
        N1, N2 = N2, N1
    localAnswer = 0
    for value, index in enumerate(range(0, N1)):
        localAnswer = localAnswer + N2
    answer.append(str(localAnswer))

def getNumber(numerator, denominator):
    number = numerator[0]
    _, denominator = getInts(numerator, denominator)
    index = 1
    index2 = 0
    newNumerator = numerator[index: -1]
    while int(number) < int(denominator) and len(newNumerator) > 0:
        number = ''.join(numerator[0:index])
        newNumerator = numerator[index: -1]
        if index > len(numerator):
            answer.append('0')
            numerator.append('0')
        if number == 0:
            index2 = index2 + 1
            answer.append('0')
        index = index + 1
    return number, newNumerator

def calculateRestAndIterations(numerator, denominator):
    numerator, denominator = getInts(numerator, denominator)
    localDenominator = denominator
    iterations = 0
    while numerator >= localDenominator:
        iterations = iterations + 1
        localDenominator = localDenominator + denominator
    if localDenominator - denominator - numerator == 0:
        localDenominator = numerator
    rest = localDenominator - numerator
    return iterations, rest

def getInts(numerator, denominator):
    return int(''.join(numerator)), int(''.join(denominator))

def div(numerator, denominator):
    answerIsPositive(numerator, denominator)
    numerator, denominator = processNumbers(numerator, denominator, 'div')
    while len(numerator) != 0:
        numberToDivide, newNumerator = getNumber(numerator, denominator)
        iterations, rest = calculateRestAndIterations(numberToDivide,denominator)
        print(iterations, len(newNumerator))
        if len(newNumerator) > 0 and iterations != 0:
            answer.append(str(iterations))
        numerator = newNumerator
    print(''.join(answer))

def main():
    global answer
    div(700, 70)


if __name__ == "__main__":
    main()
