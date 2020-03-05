
#树状数组是用来解决在数组元素动态变化的情况下，高效的计算子数组和的一种数据结构，其更新效率和计算和的效率均为O（logn）      非常非常精彩1!!!!!!!!!!虽然可以说懂了,能讲明白,但是细节可能口的还不够. 感觉还是没发用的灵活.

class FenwickTree:
    def __init__(self, SIZE):  # create fenwick tree with size SIZE
        self.Size = SIZE
        self.ft = [0 for i in range(0, SIZE)]

    def update(self, i, val):  # update data (adding) in index i in O(lg N)
        while i < self.Size:
            self.ft[i] += val
            i += i & (-i)       # 这个地方用位运算, 重点, 可以让效率到logn
# i&(-i) 的研究  https://blog.csdn.net/u012479682/article/details/79881611
    # 在这个问题中,就是一个数的值,我们把上面这个while 循环中每一次遍历到的i值,记作
    # 最初是这个i值的path. 其实就是i的按照2的幂次往上提升的结果.
    def query(self, i):  # query cumulative data from index 0 to i in O(lg N)
        ret = 0
        # 而查询就牛逼了. 一个大数他的i & (-i) 就是他的 最低2次幂的数,
        # 所以直接就查询到了之前update里面存过的数.
        while i > 0:
            ret += self.ft[i]
            i -= i & (-i)

            # 这里面是算法核心!!!!!!!!!!
            # 理解的本质是: 比如数字 i二进制101101010110
            # 那么这个数字self.ft[i]必然是101101010101所加过来的数字
            # 所以把最后一个1给减下去,就计算完了最后一个1所引发的加量.
            # 这养有多少个1,就循环多少次!!!!!!!!!!!!!!!


        return ret


if __name__ == "__main__":
    f = FenwickTree(100)
    f.update(1, 20)
    f.update(4, 4)
    print(f.query(1))
    print(f.query(3))
    print(f.query(4))
    f.update(2, -5)
    print(f.query(1))
    print(f.query(3))
