def vector_size_check(*vector_variables):
    size = [len(vector_variables[i]) for i in range(len(vector_variables)) ]

    false_token = 0

    for j in range(len(size)):
        for k in range(len(size)):
            if(size[j] != size[k]):
                false_token += 1

    if(false_token == 0):
        check_code = "True"
    else:
        check_code = "False"
    return check_code

print("=================Problem 1 ==================")
print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
print(vector_size_check([1, 3], [2,4], [6,7])) # Expected value: True
print(vector_size_check([1, 3, 4], [4], [6,7])) # Expected value: False




# ====================================================== #
def vector_addition(*vector_variables):
    answer = ""
    if(vector_size_check(*vector_variables) == "True"):
        size = len(vector_variables)
        data = [vector_variables[i] for i in range(size)]

        result = [0 for i in range(len(data[0])) ]

        for i in range(size):
            for j in range(len(data[i])):
                result[j] += data[i][j]
        answer = result

    elif(vector_size_check(*vector_variables) == "False"):
       answer = "ArithmeticError"

    return answer

print("=================Problem 2==================")
print(vector_addition([1, 3], [2, 4], [6, 7])) # Expected value: [9, 14]
print(vector_addition([1, 5], [10, 4], [4, 7])) # Expected value: [15, 16]
print(vector_addition([1, 3, 4], [4], [6,7])) # Expected value: ArithmeticError


# ====================================================== #



def vector_subtraction(*vector_variables):
    answer = ""
    if vector_size_check(*vector_variables) == "False":
        answer = "ArithmeticError"
        raise ArithmeticError

    elif(vector_size_check(*vector_variables) == "True"):
        size = len(vector_variables)
        data = [vector_variables[i] for i in range(size)]

        result = data[0]

        for i in range(1,size):
            for j in range(len(data[i])):
                result[j] -= data[i][j]
        answer = result

    return answer

print("=================Problem 3==================")
print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]





# ====================================================== #






def scalar_vector_product(alpha, vector_variable):
    result = [alpha * i for i in vector_variable]
    return result


print("=================Problem 4==================")
print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
print (scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
print (scalar_vector_product(4,[1])) # Expected value: [4]



# ====================================================== #


def matrix_size_check(*matrix_variables):
    data = [[i for i in matrix_variables[j]] for j in range(len(matrix_variables))]
    size_data = []
    for i in range(len(matrix_variables)):
        size_data.append(len(data[i]))

    false_token = 0

    for i in range(len(size_data)):
        for j in range(len(size_data)):
            if(size_data[i] != size_data[j]):
                false_token += 1

    if (false_token == 0):
        answer = "True"
    else:
        answer = "False"

    return answer


print("=================Problem 5==================")
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True

# ====================================================== #

def is_matrix_equal(*matrix_variables):
    answer = ""
    if(matrix_size_check(*matrix_variables) == "True"):
        data = [i for i in matrix_variables]

        false_token = 0

        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] != data[j] :
                    false_token += 1
        if(false_token == 0):
            answer = "True"
        else :
            answer = "False"
    else:
        answer = "False"

    return answer


print("=================Problem 6==================")
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]

print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
print (is_matrix_equal(matrix_x, matrix_x)) # Expected value: True


# ====================================================== #


def matrix_addition(*matrix_variables):
    answer = []
    if matrix_size_check(*matrix_variables) == "False":
        answer = "ArithmeticError"

    else :
        turn = len(matrix_variables)
        size = len(matrix_variables[0])

        answer = [[0 for i in range(size)] for j in range(size)]

        for i in range(turn):
            for j in range(size):
                for k in range(size):
                    answer[j][k] += matrix_variables[i][j][k]
    return answer

print("=================Problem 7==================")

matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]


# ====================================================== #

def matrix_subtraction(*matrix_variables):
    answer = []
    if matrix_size_check(*matrix_variables) == "False":
        answer = "ArithmeticError"
    else:
        turn = len(matrix_variables)
        size = len(matrix_variables[0])

        answer = matrix_variables[0]

        for i in range(1, turn):
            for j in range(size):
                for k in range(size):
                    answer[j][k] -= matrix_variables[i][j][k]

    return answer

print("=================Problem 8==================")
matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
print (matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]


# ====================================================== #

def matrix_transpose(matrix_variable):
    rows_1 = len(matrix_variable)
    colunms_1 = len(matrix_variable[0])

    answer = [[0 for i in range(rows_1)] for j in range(colunms_1)]

    for i in range (colunms_1):
        for j in range(rows_1):
            answer[i][j] = matrix_variable[j][i]

    print(answer)

    return 0

print("=================Problem 9==================")

matrix_w = [[2, 5], [1, 1], [2, 2]]
matrix_transpose(matrix_w)

# ====================================================== #
def scalar_matrix_product(alpha, matrix_variable):

    answer = matrix_variable

    rows = len(matrix_variable)
    colunms = len(matrix_variable[0])

    for i in range(rows):
        for j in range(colunms):
            answer[i][j] *= alpha

    return answer

print("================Problem 10==================")

matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print(scalar_matrix_product(3, matrix_x)) #Expected value: [[6, 6], [6, 6], [6, 6]]
print(scalar_matrix_product(2, matrix_y)) #Expected value: [[4, 10], [4, 2]]
print(scalar_matrix_product(4, matrix_z)) #Expected value: [[8, 16], [20, 12]]
print(scalar_matrix_product(3, matrix_w)) #Expected value: [[6, 15], [3, 3], [6, 6]]

# ====================================================== #

def is_product_availability_matrix(matrix_a, matrix_b):

    colunms_a = len(matrix_a[0])
    rows_b = len(matrix_b)

    if (colunms_a == rows_b):
        answer = 'True'
    else :
        answer = 'False'

    return answer

print("================Problem 11==================")

matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True

# ====================================================== #
def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == 'False':
        answer = 'False'

    elif is_product_availability_matrix(matrix_a, matrix_b) == 'True':
        rows_a = len(matrix_a)
        colunms_a = len(matrix_a[0])

        rows_b = len(matrix_b)
        colunms_b = len(matrix_b[0])

        answer = [[0 for i in range(colunms_b)]for j in range(rows_a)]

        for i in range(rows_a):
            for j in range(colunms_b):
                for k in range(colunms_a):
                    answer[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return answer


print("================Problem 12==================")
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
print(matrix_product(matrix_z, matrix_w)) # Expected value: False

