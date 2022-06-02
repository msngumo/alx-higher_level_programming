#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    for x in sorted(dir(hidden)):
        if x[:3] != '__':
            print(x)
