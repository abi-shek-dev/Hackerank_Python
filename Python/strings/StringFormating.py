def print_formatted(number):
    width = len(bin(number)[2:])  
    
    for i in range(1, number + 1):
        deci = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(deci.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)