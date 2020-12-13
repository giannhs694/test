import sys

print(sys.version)
print(sys.executable)


def greet(who_to_target):
    greeting = 'Hello, {}'.format(who_to_target)
    return greeting


print(greet("World"))
print(greet('Corey'))

print
