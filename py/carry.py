import sys

def count_carry_operations(a, b):
    carry = 0
    carry_count = 0
    
    while a > 0 or b > 0:
        digit_a = a % 10
        digit_b = b % 10
        
        if digit_a + digit_b + carry >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
        
        a //= 10
        b //= 10
    
    return carry_count

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    for line in data:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        result = count_carry_operations(a, b)
        print(result)

if __name__ == "__main__":
    main()
