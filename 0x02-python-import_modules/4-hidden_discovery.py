#!/usr/bin/python3.8
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    varfunct = [
        name
        for name in names
        if callable(getattr(hidden_4, name)) or not name.startswith('__')
    ]
    for sortname in varfunct:
        print ("{}".format(sortname)) 

