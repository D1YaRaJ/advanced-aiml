import random

def toss():
    return random.choice(["Heads", "Tails"])

def prob(event, S):
    return len(event) / len(S)

S = {"Heads", "Tails"}
A, B = {"Heads"}, {"Tails"}

print("Sample Space:", S)
print("Event A:", A, "| Event B:", B)

print("\nTheoretical Probabilities:")
print("P(A) =", prob(A, S), "| P(B) =", prob(B, S))
print("P(A ∩ B) =", prob(A & B, S))
print("P(A ∪ B) =", prob(A | B, S))

trials = 10000
countA = sum(toss() in A for _ in range(trials))
countB = trials - countA

print("\nExperimental Probabilities (from", trials, "trials):")
print("P(A) ≈", countA / trials, "| P(B) ≈", countB / trials)
