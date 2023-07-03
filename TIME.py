from timeit import timeit


# functions

class Solution:
    @staticmethod
    def twoSum(numbers: list[int], target: int) -> list[int]:
        hash_map = {}

        for idx, num in enumerate(numbers):

            diff = target - num

            if diff in hash_map:
                return [hash_map[diff], idx + 1]

            else:
                hash_map[num] = idx + 1

    @staticmethod
    def twoSum1(numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l + 1, r + 1]

            if sum < target:
                l += 1

            else:
                r -= 1


# variables

numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9

# timeit functions

project_1 = timeit(lambda: Solution.twoSum(numbers, target), number=10000)
project_2 = timeit(lambda: Solution.twoSum1(numbers, target), number=10000)
# project_3 = timeit(lambda: isPalindrome(sample), number=10000)

print("{:.3f}".format(project_1))
print("{:.3f}".format(project_2))
