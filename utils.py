def check_str(msg:str) -> str:
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


def check_float(msg:str) -> float:
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


def is_valid_option(option:str) -> bool:
    return True if option in VALID_OPTIONS else False


VALID_OPTIONS = ["d", "s", "e", "q", "c", "u", "l", "b"]
