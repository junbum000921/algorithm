import sys

def min_swaps_to_transform(A, B):
    if A.count('a') != B.count('a'):  
        return -1
    
    a_pos_A = [i for i in range(len(A)) if A[i] == 'a']
    a_pos_B = [i for i in range(len(B)) if B[i] == 'a']

    return sum(abs(a_pos_A[i] - a_pos_B[i]) for i in range(len(a_pos_A)))

T = int(sys.stdin.readline().strip())
for _ in range(T):
    A, B = sys.stdin.readline().split()
    print(min_swaps_to_transform(A, B))
