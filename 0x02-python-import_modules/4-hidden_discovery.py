#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    for x in dir(hidden):
        if not x.startswith('__'):
            print(x)
