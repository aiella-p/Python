# # indexing - accessing the elements of a sequence using [] (indexing operator[start : end : step])
# # note the starting index inclusive and ending index not inclusive
# credit_card = "1234-5678-9876-6734"

# print(credit_card[0:4]) # 1234 OR print(credit_card[:4])
# print(credit_card[:4])
# print(credit_card[5:9]) # 5678
# print(credit_card[10:14]) #9876
# print(credit_card[15:19]) # 6734

# print(credit_card[5:]) # 5678-9876-6734

# print(credit_card[5:-1]) #5678-9876-673

# print(credit_card[-4:-1]) # 673

# print(credit_card[::2]) # every thing from begining from the string till end of the string with step 2
# # "1234-5678-9876-6734"(13-6897-7)

# print(credit_card[::3]) # every thing from begining from the string till end of the string with step 3
# # "1234-5678-9876-6734" (146-764)

# print(credit_card[::]) # "1234-5678-9876-6734"


# last 4 digits of credit card number...only visible...!!
# "1234-5678-9876-6734"

credit_card = "1234-5678-9876-6734"
#credit_card1 = 1234567898766734

# last_digits = credit_card[-4:]
# print(f" XXXX-XXXX-XXXX-{last_digits}")

# Reverse all credit_card numbers...
credit_card = "1234-5678-9876-6734"

last_digits = credit_card[::-1]
print(last_digits)



