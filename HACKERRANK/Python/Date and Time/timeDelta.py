#!/bin/python3

from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    time_fmt = '%a %d %b %Y %H:%M:%S %z'
    return str(int(abs((dt.strptime(t1, time_fmt) - 
                    dt.strptime(t2, time_fmt)).total_seconds())))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
