num1 = int(input("Enter your 1st number"))
num2 = int(input("Enter your 2nd number"))
op = input("Enter your operator\n[1]Add\n[2]Sub\n[3]Multiply\n[4]Divide")

if op == "1":
  print("----------")
  print(num1+num2)
  print("----------")

elif op == "2":
  print("----------")
  print(num1-num2)
  print("----------")

elif op == "3":
  print("----------")
  print(num1*num2)
  print("----------")

elif op == "4":
  print("----------")
  print(num1/num2)
  print("----------")