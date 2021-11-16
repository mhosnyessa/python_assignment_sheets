input_list = [-1, -2, 3, 15, -10, - 5, 124, -
              20, 19, 11, -12, -13,  50, -100]

# name := Muhammed Hosny
# section := 3
# this code was inspired by a YouTube video I watched.
# my initial thought was 3-nested-for loops, but didn't take me much time to figure out that this wasn't that good of a solution.
# all rights reserved.


def find_sub_lists(l):
    l.sort()
    current, left, right, sol, triplets, targetNum = 0, 1, len(
        l) - 1, [], [], 0
    while current <= len(l) - 2:
        print('hi', current)
        if l[current] + l[left] + l[right] == targetNum and not (l[current] == l[left] or l[right] == l[left] or l[current] == l[right]):
            triplet = [l[current], l[left], l[right]]
            sol.append([l[current], l[left], l[right]])
            left += 1
            right -= 1
        elif l[current] + l[left] + l[right] < targetNum:
            left += 1
        else:
            right -= 1

        if left > right:
            current += 1
            left = current + 1
            right = len(l) - 1
    print(sol)


find_sub_lists(input_list)
