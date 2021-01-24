from typing import List


def jumpingOnClouds(n: int, cloud_arr: List[int]) -> int:
    current_pos, num_jumps = 0, 0
    
    while current_pos < n:

        if current_pos == n - 1:
            break;

        if current_pos == n - 2:
            if cloud_arr[current_pos + 1] == 0:
                num_jumps += 1
                break;
            else:
                break;

        if cloud_arr[current_pos + 2] == 0:
            current_pos += 2
            num_jumps += 1
        else:
            current_pos += 1
            num_jumps += 1
    
    return num_jumps

if __name__ == "__main__":
    print(jumpingOnClouds(7, [0, 1, 0, 0, 0, 1, 0]))
    print(jumpingOnClouds(6, [0, 0, 0, 1, 0, 0]))
