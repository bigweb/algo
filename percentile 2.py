import math


def find_percentile(a, b, p):
    rank = (p / 100) * (len(a) + len(b))
    rank = math.ceil(rank)
    return kth(a, len(a), b, len(b), rank)


def kth(arr1, m, arr2, n, k):
    if k > (m + n) or k < 1:
        return -1

    if m > n:
        return kth(arr2, n, arr1, m, k)

    if m == 0:
        return arr2[k - 1]

    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(m, k // 2)
    j = min(n, k // 2)

    if arr1[i - 1] > arr2[j - 1]:
        return kth(arr1, m, arr2[j:], n - j, k - j)
    else:
        return kth(arr1[i:], m - i, arr2, n, k - i)


# def kth(arr1, arr2, n, m, k):
#
#     if len(arr1) == 0 and len(arr2) > 0:
#         return arr2[k - 1]
#
#     if len(arr1) > 0 and len(arr2) == 0:
#         return arr1[k - 1]
#
#     if n == 1 or m == 1:
#         if m == 1:
#             arr2, arr1 = arr1, arr2
#             m = n
#         if k == 1:
#             return min(arr1[0], arr2[0])
#         elif k == m + 1:
#             return max(arr1[0], arr2[0])
#         else:
#             if arr2[k - 1] < arr1[0]:
#                 return arr2[k - 1]
#             else:
#                 return max(arr1[0], arr2[k - 2])
#
#     mid1 = (n - 1) // 2
#     mid2 = (m - 1) // 2
#
#     if mid1 + mid2 + 1 < k:
#         if arr1[mid1] < arr2[mid2]:
#             return kth(arr1[mid1 + 1:], arr2, n - mid1 - 1, m, k - mid1 - 1)
#         else:
#             return kth(arr1, arr2[mid2 + 1:], n, m - mid2 - 1, k - mid2 - 1)
#     else:
#         if arr1[mid1] < arr2[mid2]:
#             return kth(arr1, arr2[:mid2 + 1], n, mid2 + 1, k)
#         else:
#             return kth(arr1[:mid1 + 1], arr2, mid1 + 1, m, k)


if __name__ == "__main__":
    # test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    # # should print 7
    # print(find_percentile(test_a, test_b, test_p))

    # test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    # # should print 6
    # print(find_percentile(test_a, test_b, test_p))
    #
    test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    # should print 20
    print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    # # should print 20
    # print(find_percentile(test_a, test_b, test_p))
