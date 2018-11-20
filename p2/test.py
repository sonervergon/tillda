from p2_5 import mult,div

def test(D1, D2, method):
    for index, value in enumerate(D1):
        if method == 'mult':
            tested_value = mult(D1[index], D2[index], False)
            correct_answer = D1[index] * D2[index]
        if method == 'div':
            try:
                tested_value = div(D1[index], D2[index])
                correct_answer = int(D1[index] / D2[index])
            except Exception as e:
                print('_______________')
                print('')
                print('\033[91m' + 'Zero Division Error: ' + '\033[0m')
                pass
        test = '\033[91m' + 'Failed' + '\033[0m'
        if tested_value == correct_answer:
            test = '\033[92m' + 'Success' + '\033[0m'
        print('_______________')
        print('\033[94m' + 'Test: ' + str(index+1) + '\033[0m')
        print('Value: ', tested_value, ' ..... ', 'Correct value: ', correct_answer, ' ..... ', 'Test ', test)
    print('')

def main():
    test_values_1 = [1, -2, 4, 6, 8, 9, 10, 43, 983]
    test_values_2 = [4234, -51235, 23452, -134123, 5234, 23123, 4123, 42, 87]
    test_values_3 = [420, 500032, 7000, 2000200003, 4123, -434510023, 440000234]
    test_values_4 = [4, 70, 70, 9, 10, 0, 700]
    print('')
    print('\033[4m' + '\033[95m' + 'Testing Multiplication...' + '\033[0m')
    test(test_values_1, test_values_2, 'mult')
    print('\033[4m' + '\033[95m' + 'Testing Division...' + '\033[0m')
    test(test_values_3, test_values_4, 'div')



if __name__ == '__main__':
    main()
