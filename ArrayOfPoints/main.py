def findClosestsPoints(k: int = 0, points: list[list[int]] = [[0, 0]], origin: list[int] = [0, 0]):
    res = []

    for i in points:
        res += [
            [pow(
                    (i[0] - origin[0])**2 + (i[1] - origin[1]**2), 0.5
                ), 
                i[0], i[1]]]

    res = sorted(res, key=lambda x: x[0])
        
    return [[x[1], x[2]] for x in res[:k]]

    

points = [[1,4], [6,5], [9,2], [9, 9], [3, 7]]
print(findClosestsPoints(3, points, [0, 0]))
