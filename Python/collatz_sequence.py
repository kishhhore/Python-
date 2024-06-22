def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    number = int(input("Enter a positive integer: "))
    sequence = collatz_sequence(number)
    print("Collatz sequence:", sequence)

if __name__ == "__main__":
    main()
