LOWER_LIMIT = 33
UPPER_LIMIT = 127

num_list = ''
columns = int(input("How many columns: "))
column_size = 760 // columns  # len(num_list)
for i in range(LOWER_LIMIT, UPPER_LIMIT + 1):
    num_list += ('{:>3}{:>4}\n'.format(i, chr(i)))
for i in range(0, columns):
    print(num_list[column_size * i: column_size * (i + 1)])

# for i in range(LOWER_LIMIT, UPPER_LIMIT + 1):
#     print('{:>3}{:>4}'.format(i, chr(i)))
#     if i > UPPER_LIMIT//2:
#         print(end=" ")

