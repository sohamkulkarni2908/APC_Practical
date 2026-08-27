def fact():
   n = int(input("Enter a number: "))
   if n < 0:
      print("Factorial cannot be calculated for -ve numbers.")
   elif n == 0:
      print("Factorial of zero is 1.")
   else:
      f = 1
      for i in range(1, n+1):
         f = f * i
      print("Factorial of",n,"is",f)

fact()