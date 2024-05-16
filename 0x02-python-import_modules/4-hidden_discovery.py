#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    x = []
    x = dir(hidden_4.pyc)
    for name in sorted(x):
        if not name.startwith('__'):
            print(name)
