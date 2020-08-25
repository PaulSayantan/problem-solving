from cmath import phase

def polarcord(comp: complex):
    print(abs(comp))
    print(phase(comp))

if __name__ == "__main__":
    polarcord(complex(input()))



    