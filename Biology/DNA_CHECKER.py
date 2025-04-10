from functools import lru_cache
from colorama import Fore

creator = "Orestis Gatos"

dna_bases = {
    0: "A", 1: "T", 2: "C", 3: "G", 4: "A", 5: "T", 6: "G", 7: "C", 8: "A", 9: "T",
    10: "C", 11: "G", 12: "A", 13: "T", 14: "G", 15: "C", 16: "A", 17: "T", 18: "C", 19: "G",
    20: "A", 21: "T", 22: "G", 23: "C", 24: "A", 25: "T", 26: "C", 27: "G", 28: "A", 29: "T",
    30: "G", 31: "C", 32: "A", 33: "T", 34: "C", 35: "G", 36: "A", 37: "T", 38: "G", 39: "C",
    40: "A", 41: "T", 42: "C", 43: "G", 44: "A", 45: "T", 46: "G", 47: "C", 48: "A", 49: "T",
    50: "C", 51: "G", 52: "A", 53: "T", 54: "G", 55: "C", 56: "A", 57: "T", 58: "C", 59: "G",
    60: "A", 61: "T", 62: "G", 63: "C", 64: "A", 65: "T", 66: "C", 67: "G", 68: "A", 69: "T",
    70: "G", 71: "C", 72: "A", 73: "T", 74: "C", 75: "G", 76: "A", 77: "T", 78: "G", 79: "C",
    80: "A", 81: "T", 82: "C", 83: "G", 84: "A", 85: "T", 86: "G", 87: "C", 88: "A", 89: "T",
    90: "C", 91: "G", 92: "A", 93: "T", 94: "G", 95: "C", 96: "A", 97: "T", 98: "C", 99: "G"
}

@lru_cache
def deco(func):
    def wrapper(*args, **kwargs):
        print(Fore.LIGHTRED_EX + f"\nProgram made by {creator}!")
        print(f"\n", Fore.YELLOW + f"Starting function {func.__name__} ...\n")
        func(*args, **kwargs)
        print("\n", Fore.GREEN + ''.join(["-" for _ in range(30)]))
        print(Fore.YELLOW + f"\nExiting function {func.__name__} ...")
        exit()
    return wrapper

@deco
def check_dna(bases: dict):
    results = []
    for base in range(0, len(bases), 2):
        if (bases[base] == "A") and (bases[base+1] == "T"):
            results.append(True)
        elif (bases[base] == "T") and (bases[base+1] == "A"):
            results.append(True)
        elif (bases[base] == "C") and (bases[base+1] == "G"):
            results.append(True)
        elif (bases[base] == "G") and (bases[base+1] == "C"):
            results.append(True)
        else:
            results.append(False)
    for idx, value in enumerate(results):
        print(Fore.LIGHTCYAN_EX + f"|Sequence {idx+1}: {value}") if idx < 9 else print(Fore.LIGHTCYAN_EX + f"Sequence {idx+1}: {value}")
    for b in results:
        if not b:
            print("\n", Fore.GREEN + ''.join(["-" for _ in range(30)]))
            print(Fore.RED + "\n       Problematic DNA")
            return False
    print("\n", Fore.GREEN + ''.join(["-" for _ in range(30)]))
    print(Fore.BLUE + "\n       Functional DNA")
    return True

if __name__ == "__main__":
    print(check_dna(dna_bases))