# You can also store integer values other than base 10 such as

# Binary (base 2)
# Octal (base 8)
# Hexadecimal numbers (base 16)

# decimal int 16 with base 8
# Prefix with zero + letter o
octal_num = 0o20
print(octal_num)  # 16
print(type(octal_num))  # class 'int'

# decimal int 16 with base 16
# Prefix with zero + letter x
hexadecimal_num = 0x10  # decimal equivalent of 21
print(hexadecimal_num)  # 16
print(type(hexadecimal_num))  # class 'int'

# decimal int 16 with base 2
# Prefix with zero + letter b
binary_num = 0b10000  # decimal equivalent of 6
print(binary_num)  # 16
print(type(binary_num))  # class 'int'