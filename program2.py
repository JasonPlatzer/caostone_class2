import requests

question = input('Enter your question for 8 ball: ')
magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

try:
    # gets data from website
    response = requests.get(magic_8_ball_url).json()
    # gets the specific data from json
    answer = response['magic']['answer']
    print(f'The magic 8 ball says {answer}')
except Exception as e:
    print(e)
    print('Sorry cant connect')