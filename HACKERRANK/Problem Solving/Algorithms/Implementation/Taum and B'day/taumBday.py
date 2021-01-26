def taumBday(b: int, w: int, bc: int, wc: int, z: int) -> int:
    if abs(bc-wc)<=z:
        return b*bc+w*wc
    elif bc < wc:
        return b * bc + w * (bc + z)
    else:
        return w*wc+b*(wc+z)

if __name__ == "__main__":
    for _ in range(int(input())):
        b,w = (int(x) for x in input().split())
        bc,wc,z = (int(x) for x in input().split())
        print(taumBday(b, w, bc, wc, z))