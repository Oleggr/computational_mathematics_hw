'''
Couple of functions work easy handle with matrix

My own realisation
'''

def matrix_print(a, matrix_name = 'default_name'):
    '''
    Func for printing matrix
    '''

    print('\n{} is:'.format(matrix_name))

    for line in a:

        print('|', end=' ')

        for elem in line:
            print(round(elem, 4), end=' ')

        print('|')