# Your task is to sort the string S in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

x= input()

lower= sorted(i for i in x if i.islower())
upper = sorted(i for i in x if i.isupper())
number= sorted(int(i)for i in x if i.isdigit())
odd= [str(i) for i in number if i%2 != 0]
even= [str(i) for i in number if i%2 == 0]

print(''.join(lower + upper + odd + even))