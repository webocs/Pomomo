import config

NO_ACTIVE_SESSION_ERR = 'No active session.\n' \
                        f'Use command \'{config.CMD_PREFIX}start [pomodoro] [short_break] [long_break] [intervals]\'.'

ACTIVE_SESSION_EXISTS_ERR = 'There is already an active session on the server.\n'

NUM_LT_ONE_ERR = 'Must use numbers greater than 0.'

NUM_OUTSIDE_ONE_AND_SIXTY_ERR = 'Duration must be between 1 and 60 minutes.'

MISSING_ARG_ERR = 'Pass in at least one number.'

GREETINGS = ['Howdy howdy! Let\'s do this thang.',
             'Hey there! Let\'s get started!',
             'It\'s productivity o\'clock!']

ENCOURAGEMENTS = ['Let\'s keep it going!',
                  'Keep up the good work!',
                  'That\'s some good stuff!']

STILL_THERE = ['Phew...I was getting nervous 😅',
               'Gotcha! Just checking 😊',
               'Cool beans!']
