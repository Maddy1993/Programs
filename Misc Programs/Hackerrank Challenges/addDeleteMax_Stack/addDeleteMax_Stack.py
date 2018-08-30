# This file consists of a program
# which adds, deletes and prints the max
# element of the stack efficiently.


# global
stack = []
max_stack = []


# Function which reads the input and
# forwards the parsed input to be processed
def read_input():
    # read input lines
    input_lines = int(input())

    # store the input values as list
    # where each member is also a list
    values = []
    for i in range(0, input_lines):
        values.append(input().split(" "))

    process(values)


# Function which process the read input
def process(values):
    # process each member of list
    # perform the operations specified
    # on the global list (stack) variable
    global stack
    global max_stack

    file = open("test", 'a')

    for item in values:
        # if it is add operation,
        # add the value to the beginning
        # of the list.
        if item[0] == '1':
            stack.insert(0, int(item[1]))
            if not max_stack:
                max_stack.insert(0, int(item[1]))
            elif max_stack[0] < int(item[1]):
                max_stack.insert(0, int(item[1]))

        # when the operation requested is
        # a delete operation, pop the element
        # at index 0
        elif item[0] == '2':
            top_val = stack[0]
            if stack:
                stack.pop(0)
                if max_stack and top_val == max_stack[0]:
                    max_stack.pop(0)

        # when the find maximum operation is requested
        # process it along with the delete operations.
        elif item[0] == '3':
            # find_max()
            if max_stack:
                max_val = max_stack[0]
                # max_stack.pop(0)
                # print(max_val)
                file.write(str(max_val)+"\n")


# Function which performs deletes and finds
# maximum value among the values stored until
# now
def find_max():
    global stack

    # iterate through the stack
    # to find the maximum element
    max_val = -1

    for value in stack:
        if int(value) > max_val:
            max_val = value

    print(str(max_val))


if __name__ == '__main__':
    read_input()
