answer = []
#hejalkjshd
#######################################
#    IN: Integers N1 and N2.
#    OUT: Nothing.
#    Intention is to use this function to determine if the answer should be negative or not.
def answerIsPositive(N1, N2):
    positiveAnswer = (N1 <= 0 and N2 <= 0) or (N1 >= 0 and N2 >= 0)
    if not positiveAnswer:
        answer.append('-')

########################
#   IN: Integers N1 & N2 and what action is calling the function (either "div" or "mult")
#   OUT: Abs-values of N1 and N2 as a string or as integers
#   Intention is to deliver clean numbers and raise potential errors.
def processNumbers(N1, N2, method):
    N1 = abs(N1)
    N2 = abs(N2)
    if method == 'div':
        N1 = str(abs(N1))
        N2 = str(abs(N2))
    return N1, N2

#######################
#   IN: Integers N1 and N2.
#   OUT: The product between N1 and N2.
#   Intention is to multiply N1 and N1.
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

###########################
#
#
#
def getNumber(numerator, denominator, count, rest):
    isNormalNumerator = int(numerator[0]) != 0 and int(numerator) != 0 and len(numerator) > 0
    index = 1
    if isNormalNumerator:
        number = int(numerator[0])
        newNumerator = numerator[index:]
        while number < int(denominator) and newNumerator != '':
                number = int(numerator[:index])
                newNumerator = numerator[index:]
                if count > 0 and (index > len(str(rest))+1):
                    answer.append('0')
                if index >= len(str(rest))+1 and rest == 0:
                    answer.append('0')
                index = index+1
    else:
        # # TODO: Add handler for this part.
        onlyZeroesLeft = int(numerator) == 0
        if onlyZeroesLeft:
            for value in range(0,len(numerator)):
                answer.append('0')
            number = 0
            newNumerator = ''
    return number, newNumerator

def divide(numberToDivide, numerator, denominator):
    denominator = int(denominator)
    quotient = 0
    localDenominator = denominator
    while localDenominator <= int(numberToDivide):
        localDenominator = localDenominator + denominator
        quotient = quotient + 1
    if quotient != 0:
        answer.append(str(quotient))
    rest = int(numberToDivide) - mult(quotient, denominator)
    return rest

def div(numerator, denominator):
    answerIsPositive(numerator, denominator)
    numerator, denominator = processNumbers(numerator, denominator, 'div')
    numberToDivide = int(numerator)
    originalNumerator = numerator
    rest = None
    count = 0
    while len(numerator) >= len(denominator):
        numberToDivide, numerator = getNumber(numerator, denominator, count, rest)
        rest = divide(numberToDivide, numerator, denominator)
        if rest != 0:
            numerator = str(rest) + str(numerator)
        count = count + 1
        if count >= 10^6 :
            break
    return answer

div(3498455, 4)
print(''.join(answer))
