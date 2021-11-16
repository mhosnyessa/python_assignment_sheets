# input_list = [-1, -2, 3, 15, -10, - 5, 124, -
#               20, 19, 11, -12, -13, -1, 50, -2, -100]

input_list = [-1, -2, 3, 15, -10, - 5, 124, -
              20, 19, 11, -12, -13,  50, -100]
input_list = [-25, -10, -7, -3, 2, 4, 8, 10]


class TripletsFinder:

    @staticmethod
    def triplets_finder(input):
        input.sort()
        target = 0
        result = []
        # for n in input
        for i in input[:]:
            for j in input[1:]:
                for k in input[2:]:
                    if not (i == j or i == k or j == k) and (i + j + k == target):
                        # i == j ? i =
                        triplet = [i, j, k]
                        triplet.sort()
                        if triplet not in result:
                            result.append(triplet)

        print(result)


TripletsFinder.triplets_finder(input_list)
