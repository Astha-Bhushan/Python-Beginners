def checkArmstrong(num):
  # initialize sum
  sum = 0
  # find the sum of the cube of each digit
  temp = num
  while temp > 0:
     digit = temp % 10
     sum += digit ** 3
     temp //= 10

  # display the result
  if num == sum:
     print(num,"is an Armstrong number")
  else:
     print(num,"is not an Armstrong number")
     
def checkPrime(num):
  # prime numbers are greater than 1
  if num > 1:
     # check for factors
     for i in range(2,num):
         if (num % i) == 0:
             print(num,"is not a prime number")
             print(i,"times",num//i,"is",num)
             break
     else:
         print(num,"is a prime number")

  # if input number is less than
  # or equal to 1, it is not prime
  else:
     print(num,"is not a prime number")

# take input from the user
number = int(input("Enter a number: "))

checkArmstrong(number)

checkPrime(number)


