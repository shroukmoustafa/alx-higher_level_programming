#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    x = []
    x = dir(hidden_4)
    for name in sorted(x):
        if not name.startswith('__'):
            print(name)
