VALID_OPTIONS = ['d', 's', 'e', 'q']

def check_str(msg):
    while True:
        try:
            value = str(input(msg))
        except(ValueError, TypeError):
            print('value must be valid')
        except KeyboardInterrupt:
            print('User Interrupt')
            return 0
        else:
            return value
        

def is_valid_option(option):
    if option in VALID_OPTIONS:
        return True
    else:
        print('Invalid option, please try again.')
        return False

