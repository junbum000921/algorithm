

def process_contest(M, N, P, submissions):
    participants = {i: {'solved': 0, 'score': 0, 'problems': {}} for i in range(1, P+1)}
    
    for p, m, t, j in submissions:
        if m not in participants[p]['problems']:
            participants[p]['problems'][m] = {'wrong_attempts': 0, 'solved_time': None}
        
        problem_data = participants[p]['problems'][m]
        
        if j == 1 and problem_data['solved_time'] is None:
            problem_data['solved_time'] = t
            participants[p]['solved'] += 1
            participants[p]['score'] += t + problem_data['wrong_attempts'] * 20
        elif j == 0 and problem_data['solved_time'] is None:
            problem_data['wrong_attempts'] += 1
    
    ranking = sorted(
        [(pid, data['solved'], data['score']) for pid, data in participants.items()],
        key=lambda x: (-x[1], x[2])
    )
    
    return ranking


data = input().strip().split("\n")
index = 0
K = int(data[index])
index += 1
    
results = []
for case_num in range(1, K+1):
    M, N, P = map(int, data[index].split())
    index += 1
        
    submissions = []
    for _ in range(N):
        parts = data[index].split()
        p, m, t, j = int(parts[0]), parts[1], int(parts[2]), int(parts[3])
        submissions.append((p, m, t, j))
        index += 1
        
    ranking = process_contest(M, N, P, submissions)
        
    results.append(f"Data Set {case_num}:")
    for pid, solved, score in ranking:
        results.append(f"{pid} {solved} {score}")
        
    if case_num < K:
        results.append("")
    
print("\n".join(results))

