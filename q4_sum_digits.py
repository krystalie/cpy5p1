# q4_sum_digits.py
# Find sum of digits

# input integer
num = int(input("Enter integer from (0-1000): "))
          
# compute sum of digits
total = 0

total = total + (num % 10) # add remainder 
num = num // 10            # remove last digit
total = total + (num % 10) # add remainder 
num = num // 10            # remove last digit 
total = total + (num % 10) # add remainder 
num = num // 10            # remove last digit
total = total + (num % 10) # add remainder 



# output sum of digits
print (" Sum of digits =", total)
