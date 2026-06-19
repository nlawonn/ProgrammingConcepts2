# setA = {1, 2, 3, 4, 5}
# setB = {2, 4, 7, 8, 9}
# And
# setUnion = setA | setB
# Or
# setIntersect = setA & setB
# setXOR = setA ^ setB
# setSub = setA - setB
# print(setUnion)
# print(setIntersect)
# print(setXOR)
# print(setSub)

# print(7 / float(2))

# age = input('What is your age? ')

# print(f'Your age is {age}.')
# num_list = [3, 2, 17, 2.5]
# num_list.sort()  # Sorts into [2, 2.5, 3, 17]
# print(num_list)
# my_list = []          # Must do this before you append!
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(my_list)
# my_list.remove(1)     # List is now [2, 3]
# print(my_list)
# a_list = [1, 2, 3]

# a_list.append(4)
# a_list.extend([4])        # This has the same effect.

# a_list.extend([4, 5, 6])  # Adds 3 elements to the list.
# a_list = [10, 20, 40]  # Missing 30.
# a_list.insert(2, 30 )  # At index 2 (third), insert 30.
# print(a_list)          # Prints [10, 20, 30, 40]
# a_list.insert(100, 33)
# print(a_list)          # Prints [10, 20, 30, 40, 33]
# a_list.insert(-100, 44)
# print(a_list)          # Prints [44, 10, 20, 30, 40, 33]
# def main():
    # my_list = []      # Start with empty list
    # while True:
        # s = input('Enter next name: ')
        # if len(s) == 0:
            # break
        # my_list.append(s)
    # my_list.sort()    # Place all elems in order.
    # print('Here is the sorted list:')
    # for a_word in my_list:
        # print(a_word, end=' ')

# main()
#a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_list = [ ]
for i in range(1,101):
    b_list.append(i * i)
print(b_list)

mat = [[10, 20, 30], [11, 21, 31], [12, 22, 32]]
print(mat)