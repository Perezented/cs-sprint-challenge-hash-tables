negs = {}


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    tester = {}
    # Your code here
    a.sort()
    if a[0] >= 0:
        return result
    for num in a[0:25]:

        if num < 0:
            print(num)
            tester[num] = num
    for h in a[0:25]:
        if -h in tester:
            print(f'llooookkk: {h}')
            result.append(h)

    print(tester)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
