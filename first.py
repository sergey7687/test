
def decorator(func):
    def wrapper():
        g = []
        for i in range(10):
            g.append(func())
        return g
    return wrapper

@decorator
def mu():
    return 'helllo'

print(mu())