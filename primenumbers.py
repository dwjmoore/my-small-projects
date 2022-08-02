"""
Prime numbers are numbers greater than 1.
They only have two factors, 1 and the number itself.
This means that these numbers cannot be divided by any
number other than 1 and the number itself without
leaving any remainder.

This program creates a list of prime numbers
you would like to find.
"""


def main():
  prime = int(input("How many prime numbers do you want? "))
  prime_list = [] 
  num = 0

  while len(prime_list) < prime:
    num += 1

    if num % 10 == 0:
      print(f'The code is still running. It has processed {num} integers.')

    pre_list = []

    for elem in range(1, num + 1):
      if num % elem == 0:
        pre_list.append(elem)
    if len(pre_list) == 1:
      prime_list.append(pre_list[0]) 
    elif len(pre_list) == 2:
      prime_list.append(pre_list[1])
  
  print()
  print(f'Here are the first {prime} prime numbers.')
  print()
  print(prime_list)

if __name__ == '__main__':
  main()