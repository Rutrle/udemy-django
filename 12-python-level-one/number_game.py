from random import sample

nums = sample(range(1, 10), 3)

print('Welcome to the guessing game!')
print('You will be guessing three non repeating numbers')

game_running = True


def is_close(guess, real):
    answer = []
    for i in range(len(real)):
        if int(guess[i]) in real:
            answer.append(True)
        else:
            answer.append(False)

    return answer


def is_match(guess, real):
    answer = []
    for i in range(len(real)):
        if int(guess[i]) == real[i]:
            answer.append(True)
        else:
            answer.append(False)

    return answer


while game_running:
    guess = input('Guess a number! ')

    if int(guess[0]) == int(guess[1]) or int(guess[0]) == int(guess[2]) or int(guess[1]) == int(guess[2]) or len(guess) > 3456:
        print('wrong input, try it again!')
        continue

    close = is_close(guess, nums)
    match = is_match(guess, nums)
    matches = 0
    closes = 0

    for i in range(3):
        if match[i] == True:
            matches = matches+1
        elif close[i] == True:
            closes = closes+1

    if matches == 3:
        # game_running=False
        print('Congratulations! That was correct!')
        break

    if matches > 0:
        print(f"{matches} * Match ")

    if closes > 0:
        print(f"{closes} * Close ")
