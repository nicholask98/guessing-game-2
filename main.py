import random
from os import system, name 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def binary_search(ai_guess, response, applicable_range):
    if response == 'higher':
        applicable_range[0] = ai_guess
        ai_guess = (applicable_range[0] + applicable_range[1]) // 2
    elif response == 'lower':
        applicable_range[1] = ai_guess
        ai_guess = (applicable_range[0] + applicable_range[1]) // 2
    return ai_guess, applicable_range

def prompt(ai_guess): # prompts for user response
    response = input('Is your number: {}?\nType "yes", "higher", or "lower"\n'.format(ai_guess))
    while response != 'higher' and response != 'lower' and response != 'yes': # Checks valid input
        print('Invalid input:')
        response = input('Type "yes", "higher", or "lower"\n')
    return response

def main():
    clear()
    applicable_range = [random.randint(-1000, -50), random.randint(0, 1000)]
    ai_guess = (applicable_range[0] + applicable_range[1]) // 2
    print('Pick a number between {} and {} and remember it. I will try to guess it.'.format(applicable_range[0], applicable_range[1]))
    response = prompt(ai_guess) # retrieves user response
    count = 1
    while response != 'yes':
        count += 1
        ai_guess, applicable_range = binary_search(ai_guess, response, applicable_range)
        response = prompt(ai_guess)
    print('Got it! Your number is {}. I got it in {} guess(es).'.format(ai_guess, count))

if __name__ == '__main__':
    main()