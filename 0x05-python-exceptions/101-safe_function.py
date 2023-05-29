#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    val = None
    try:
        val = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return (val)
