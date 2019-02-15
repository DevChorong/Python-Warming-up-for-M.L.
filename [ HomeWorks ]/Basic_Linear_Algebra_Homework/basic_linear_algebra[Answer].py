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

        result = [i for i in data[0]]

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
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError

    return None

print("=================Problem 7==================")

matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]

print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]
# ====================================================== #

def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return None

