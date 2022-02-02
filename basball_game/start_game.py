import random as ran

def generate_numbers():
    #i = 0
    #questions = []
    #while i < 3:
    #    question = ran.randint(0, 9)
    #    questions.append(question)
    #    i += 1
    ## 문제점 1 > i를 사용하지 않고 len(questions)로 list 길이 조절 가능
    ## 문제점 2 > 이렇게 작성할 경우 중복된 숫자가 나온다
    questions =[]
    while len(questions) < 3:
        number = ran.randint(0, 9)
        if number not in questions:
            questions.append(number)
        
    return questions


#print(generate_numbers())    

def take_guess():
    answers = []
    print('숫자 3개를 하나씩 차례대로 입력하세요.')
    i = 1
    while len(answers) < 3:
        answer = input(f'{i}번째 숫자를 입력하세요: ')
              
        if not answer: #input 값이 비었을때
            print('값을 입력해주세요')
            
        elif int(answer) not in range(0, 10):
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')

        elif int(answer) in answers:
            print('중복되는 숫자입니다. 다시 입력하세요.')

        else:
            answers.append(int(answer))
            i += 1
            #print(answers, i)

    return answers  

        
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    #guesses = take_guess()
    #solution = generate_numbers()
    #print(guesses, solution, strike_count, ball_count)
    i = 0
    while i < 3:
        if guesses[i] == solution[i]:
            strike_count +=1

        elif guesses[i] != solution[i] and guesses[i] in solution:
            ball_count += 1

        i += 1

    return str(strike_count) + 'S', str(ball_count) + 'B'


ANSWER = generate_numbers()
tries = 0

while True:
    tries += 1
    user_answer = take_guess()
    #print(ANSWER, user_answer)  정답출력용
    score = get_score(ANSWER, user_answer)
    print(score[0], score[1])
    #print(type(score))
    if ANSWER == user_answer:
        print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.")
        break

