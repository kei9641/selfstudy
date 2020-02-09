A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

def dogAttack(attack, rest, visit):
    time = 0
    cntAttack = 0
    while visit >= (attack+rest) * time:
        if (attack+rest) * time < visit <= (attack+rest) * time + attack:
            cntAttack += 1
        time += 1
    return cntAttack

print(dogAttack(A, B, P) + dogAttack(C, D, P))
print(dogAttack(A, B, M) + dogAttack(C, D, M))
print(dogAttack(A, B, N) + dogAttack(C, D, N))