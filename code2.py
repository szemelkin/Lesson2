import sys

for line in sys.stdin:
    for token in line.strip().split():
        print(token + "\t1")
print("Test record")
print("Hello")
