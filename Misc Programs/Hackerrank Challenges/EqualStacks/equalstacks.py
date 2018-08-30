# File which will figure out minimum
# number of blocks, that needs to be
# removed to get the maximum height
# possible among the given three stacks

import os


# Function which calculates the
# minimum value required to
# maintain the height
def equalStacks(h1, h2, h3):
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    optimal_val = 0
    isTrue = True

    while isTrue:
        top_value = 0
        if sum_h3 == sum_h2 and sum_h3 == sum_h1:
            optimal_val = sum_h3
            break
        elif sum_h1 >= sum_h2 and sum_h1 >= sum_h3:
            top_value = h1[0]
            sum_h1 += (-top_value)
            h1.pop(0)
            isTrue = True
        elif sum_h2 >= sum_h1 and sum_h2 >= sum_h3:
            top_value = h2[0]
            sum_h2 += (-top_value)
            h2.pop(0)
        elif sum_h3 >= sum_h1 or sum_h3 >= sum_h2:
            top_value = h3[0]
            sum_h3 += (-top_value)
            h3.pop(0)
    return optimal_val


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
