def check_str(msg):
    while True:
        try:
            value = str(input(msg))
        except (ValueError, TypeError):
            print("value must be valid")
        except KeyboardInterrupt:
            print("User Interrupt")
            return 0
        else:
            return value


def check_float(msg):
    while True:
        try:
            value = float(input(msg))
            if value < 0:
                raise ValueError("Value must be non-negative")
        except (ValueError, TypeError):
            print("value must be valid")
        except KeyboardInterrupt:
            print("User Interrupt")
            return 0
        else:
            return value


def is_valid_option(option):
    if option in VALID_OPTIONS:
        return True
    else:
        print("Invalid option, please try again.")
        return False


VALID_OPTIONS = ["d", "s", "e", "q"]
