#q7_generate_payroll.py
#payroll generator

#input name
name = input("Enter name: ")

#input no. of hours work
hours = int(input("Enter number of hours worked weekly: "))

#input hourly pay
rate = float(input("Enter pay rate: "))

#input CPF contribution rate
cpf = int(input("Enter CPF contribution rate: "))

#print payroll statement
print("Payroll statement for",name)

#print numbr of hours worked
print("Number of hours worked in week:",hours)

#print hourly pay rate
print("Hourly pay rate: ${0:.2f}".format(rate))

#print gross pay
gross = rate * hours
print("Gross pay: ${0:.2f}".format(gross))

#print cpf contribution rate
cpf_amt = cpf / 100 * gross
print("CPF contribution at {0}% = ${1:.2f}".format(cpf,cpf_amt))

#print Net pay
net = gross - cpf_amt
print("Net pay: ${0:.2f}".format(net))
