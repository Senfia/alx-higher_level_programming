#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for x, n in enumerate(dir(hidden_4)):
        if n[:2] != "__":
            print("{:s}".format(n))
