num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")


# # isnumeric isdigit isdecimal

# if num1.isnumeric() and num2.isnumeric():
#     soma = num1 + num2
# else:
#     print("Os valores digitados não são númericos")

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1+num2)
except:
    print("Error")