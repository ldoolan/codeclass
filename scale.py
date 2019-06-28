def scale(n):
    return lambda x: n * x

# Imagine that we now do this:
f = scale(42)

print(f(4))