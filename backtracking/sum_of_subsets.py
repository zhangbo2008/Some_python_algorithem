"""
        The sum-of-subsetsproblem states that a set of non-negative integers, and a value M,
        determine all possible subsets of the given set whose summation sum equal to given M.

        Summation of the chosen numbers must be equal to given number M and one number can
        be used only once.
"""
# 这个问题有意思, 一个数组,一个sum,让你从数组中每一个数字只能至多用一次,频出sum. 求出所有解

def generate_sum_of_subsets_soln(nums, max_sum):
    result = []
    path = []
    num_index = 0
    remaining_nums_sum = sum(nums)
    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum)
    return result

# 需要一个数据结构.
def create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum):
    """
        Creates a state space tree to iterate through each branch using DFS.
        It terminates the branching of a node when any of the two conditions
        given below satisfy.
        This algorithm follows depth-fist-search and backtracks when the node is not branchable.

        """
    if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
        return
    if sum(path) == max_sum:
        result.append(path)
        return
    for num_index in range(num_index, len(nums)):
        create_state_space_tree(
            nums,
            max_sum,
            num_index + 1,
            path + [nums[num_index]],   # 迭代就在这2步,选中
            result,
            remaining_nums_sum - nums[num_index],  #  然后在剩余中剔除.
        )# 所以这个算法也就是暴力算法,等于把所有组合都品一边然后试试sum而已.


"""
remove the comment to take an input from the user

print("Enter the elements")
nums = list(map(int, input().split()))
print("Enter max_sum sum")
max_sum = int(input())

"""
nums = [3, 34, 4, 12, 5, 2]
max_sum = 9
result = generate_sum_of_subsets_soln(nums, max_sum)
print(*result)
