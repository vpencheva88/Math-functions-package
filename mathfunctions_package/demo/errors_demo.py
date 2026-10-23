#Catching errors
from mathfunctions_package import gcd, lcm
 
 
#1. TypeError: giving gcd a decimal number
try:
    print(gcd(5.7689, 2))       #not executed: 4.5 is not a whole number
except TypeError as e:
    print('Error:', e)       #e holds the message written in gcd
finally:
    print('This is the finally block, it will always be executed.')
 
 
#2. TypeError: giving lcm text instead of a number
try:
    print(lcm('12', 8))      #'12' in quotes is text, not a number
except TypeError as e:
    print('Error:', e)
finally:
    print('This is the finally block, it will always be executed.')

#3. TypeError: lcm with a zero and a decimal
   
    try:
        print(lcm(0, 2.5))
    except TypeError as e:
        print('Error:', e)
    finally:
        print('This is the finally block, it will always be executed.')
 
#4. Correct input, so no error
try:
    print('gcd(48, 18) =', gcd(48, 18))
    print('lcm(4, 6) =', lcm(4, 6))
except TypeError as e:
    print('Error:', e)       #skipped, because nothing went wrong
finally:
    print('This is the finally block, it will always be executed.')

#ZeroDivisionError
try:
    a, b = 0, 0
    answer = abs(a * b) // gcd(a, b)    #gcd(0, 0) = 0, so this divides by zero
    print(answer)
except ZeroDivisionError:
    print('You cannot divide by zero! gcd(0, 0) = 0, so lcm(0, 0) needs the special check.')
finally:
    print('This is the finally block, it will always be executed.')

def show_errors() -> None:
    """Run all the error-handling examples."""

    #1. TypeError: giving gcd a decimal number
    try:
        print(gcd(5.7689, 2))
    except TypeError as e:
        print('Error: gcd only works with integers', e)
    finally:
        print('This is the finally block, it will always be executed.')

    #...examples 2 to 7, all indented the same way...


if __name__ == "__main__":
    show_errors()