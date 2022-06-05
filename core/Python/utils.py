class bcolors:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def TakeInput(items: list = [], Type: list = []):
    """Util function to quickly take input from user"""
    inputs = {}
    for idx, item in enumerate(items):
        val = input(
            bcolors.GREEN
            + "Please enter "
            + item
            + " (Type: "
            + Type[idx]
            + "): "
            + bcolors.RESET
        )
        inputs[item] = val
    return inputs

def printError():
    print(bcolors.RED + "Error: Operation failed." + bcolors.RESET)
