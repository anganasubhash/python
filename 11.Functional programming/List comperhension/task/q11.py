#Given a list of numbers, create a list where each number is replaced by "FizzBuzz" if divisible
#by 15, "Fizz" if divisible by 3, "Buzz" if divisible by 5, and the number itself otherwise (for
#numbers 1 to 30)
lst1=["fizzbuzz" if i%15==0 else "fizz" if i%3==0 else "buzz" if i%5==0 else i for i in range(1,31)]
print(lst1)