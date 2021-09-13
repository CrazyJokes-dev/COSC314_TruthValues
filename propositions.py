
# inputs
p = [True, True, False, False]

q = [True, False, True, False]

# Nice job! I do like how you thought of doing implication
# I find it kind of cool that python has these in-built functions

print("Conjunction:")
for i in range(0, len(p)):
    print(p[i] and q[i])

print() # for separation
print("Disjunction: ")
for i in range(0,len(p)):
    print(p[i] or q[i])

print() # for separation
print("Exclusive Or: ")
for i in range(0,len(p)):
    print(p[i] ^ q[i])

print() # for separation
print("Implication: ")
for i in range(0,len(p)):
    if (p[i]):
        print(q[i])
    else:
        print(True)

print() # for separation
print("Biconditional: ")
for i in range(0,len(p)):
    if (p[i] == q[i]):
        print(True)
    else:
        print(False)



