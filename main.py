vector_1 = [1, 2, 3, 4]
vector_2 = [5, 6, 7, 8]


def add(vec_1, vec_2):
    result = []
    for index, num in enumerate(vec_1):
        result.append(num + vec_2[index])
    return result


def sub(vec_1, vec_2):
    result = []
    for index, num in enumerate(vec_1):
        result.append(num - vec_2[index])
    return result


def scalar_mult(vector, scalar):
    result = []
    for num in vector:
        result.append(scalar * num)
    return result


print(add(vector_1, vector_2))
print(sub(vector_1, vector_2))
print(scalar_mult(vector_1, 3))
