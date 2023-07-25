from settings import BLUE, CYAN, GREEN, RED, RESET, YELLOW


def message_info(text: str, size: int | None = None) -> None:

    if size:
        print(f"{YELLOW} # {'-' * size} # {RESET}")
        print(f'   {GREEN}{text}{RESET}')
        print(f"{YELLOW} # {'-' * size} # {RESET}")
    else:
        size = len(text)
        print(f"{YELLOW} # {'-' * size} # {RESET}")
        print(f'   {GREEN}{text}{RESET}')
        print(f"{YELLOW} # {'-' * size} # {RESET}")


def message_error(text: str, size: int | None = None) -> None:

    if size:
        print(f"{CYAN} # {'-' * size} # {RESET}")
        print(f'   {RED}{text}{RESET}')
        print(f"{CYAN} # {'-' * size} # {RESET}")
    else:
        size = len(text)
        print(f"{CYAN} # {'-' * size} # {RESET}")
        print(f'   {RED}{text}{RESET}')
        print(f"{CYAN} # {'-' * size} # {RESET}")


def message_winner(text: str, size: int | None = None) -> None:

    if size:
        print(f'{BLUE} # {"-" * size} # {RESET}')
        print(f'   {GREEN}{text}{RESET}')
        print(f'{BLUE} # {"-" * size} # {RESET}')
    else:
        size = len(text)
        print(f'{BLUE} # {"-" * size} # {RESET}')
        print(f'   {GREEN}{text}{RESET}')
        print(f'{BLUE} # {"-" * size} # {RESET}')


def message_lose(text: str, size: int | None = None) -> None:

    if size:
        print(f'{BLUE} # {"-" * size} # {RESET}')
        print(f'   {RED}{text}{RESET}')
        print(f'{BLUE} # {"-" * size} # {RESET}')
    else:
        size = len(text)
        print(f'{BLUE} # {"-" * size} # {RESET}')
        print(f'   {RED}{text}{RESET}')
        print(f'{BLUE} # {"-" * size} # {RESET}')


def message_alert(text: str, size: int | None = None) -> None:
    if size:
        print(f'{RED} # {"-" * size} # {RESET}')
        print(f'   {YELLOW}{text}{RESET}')
        print(f'{RED} # {"-" * size} # {RESET}')
    else:
        size = len(text)
        print(f'{RED} # {"-" * size} # {RESET}')
        print(f'   {YELLOW}{text}{RESET}')
        print(f'{RED} # {"-" * size} # {RESET}')
