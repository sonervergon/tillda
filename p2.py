numerator = 3472
denominator = 2
answer = []
answerIsNegative = False

def mult(number, number):


def calculate(numerator):
    numerator = list(str(numerator))
    index = 0
    rest = 1
    while len(numerator) != 0 or ():
        number = grabNextNumber(numerator)
        rest = getRestAndIterations(number)['rest']
        iterations = getRestAndIterations(number)['iterations']
        answer.append(str(iterations))
        numerator = getNewNumerator(rest, number, numerator)
        index = index+1
    print(''.join(answer))

def grabNextNumber(numerator):
    number = int(numerator[0])
    index = 1
    while number < denominator:
        number = numerator[0:index]
        number = ''.join(number)
        number = int(number)
        if len(numerator) < index:
            answer.append(',')
            number = int(str(number) + '0')
        index = index+1
    return number

def getRestAndIterations(numerator):
    localDenominator = denominator
    iterations = 0
    while numerator>=localDenominator:
        iterations = iterations + 1
        localDenominator = localDenominator+denominator

    if localDenominator-denominator-numerator == 0:
        localDenominator = numerator
    rest = localDenominator-numerator
    print(rest, iterations)
    return {'rest': rest, 'iterations': iterations}

def getNewNumerator(rest,number,numerator):
    numberString = ''.join(numerator)
    if rest != 0:
        numberString = [str(rest)] + list(numberString.split(str(number))[1])
    else:
        if len(numberString.split(str(number))) > 1:
            numberString = list(numberString.split(str(number))[1])
        else:
            numberString = str(number)
    return numberString

def answerIsNegative(number, number):


def main():
    global denominator,answer,answerIsNegative
    answerIsNegative(number, number)
    calculate(numerator)

if __name__ == "__main__":
    main()
