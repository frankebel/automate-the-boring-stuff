#!/usr/bin/env python
import random
import time

# Set parameters.
number_of_questions = 10
number_of_tries = 3
timeout = 8

correct_answers = 0

# Start quiz.
for question in range(1, number_of_questions+1):
    # Generate question.
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    answer = num1*num2

    # Ask question.
    time_start = time.time()
    for i in range(number_of_tries):
        player_answer = input(f'#{question}: {num1} x {num2} = ')
        if player_answer == str(answer):
            # Correct answer.
            if time.time() - time_start < timeout:
                # Answered within timeout.
                correct_answers += 1
            else:
                print('Out of time!')
            break
    if i == 2:
        print('Out of tries!')

print(f'Score: {correct_answers} / {number_of_questions}')
    
