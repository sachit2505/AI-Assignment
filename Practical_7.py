def implies(p, q):
    return (not p) or q 

# Given facts
S = True  # It is sunny today

D = implies(S, True)  # If sunny, plants are dry -> D is True
W = implies(D, True)  # If dry, water is needed -> W is True

# Print results
print(f"It is sunny: {S}")
print(f"Plants are dry: {D}")
print(f"Water is needed: {W}")