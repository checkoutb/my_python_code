
from typing import List
# import 
# import 
# import 


class LT1995:



# D D

    # int cnt[101] = {}, res = 0;
    # for (int k = n.size() - 1; k > 1; ++cnt[n[k--]])
    #     for (int i = 0; i < k; ++i)
    #         for (int j = i + 1; j < k; ++j)
    #             if (n[i] + n[j] + n[k] <= 100)
    #                 res += cnt[n[i] + n[j] + n[k]];
    # return res;     
    # for的最后一个部分。

        # seenAlready = defaultdict(int)
        # n = len(nums)
        # count = 0
        # for a in range(n-1,-1,-1):
        #     for b in range(a-1,-1,-1):
        #         for c in range(b-1,-1,-1):
        #             possibleSum = nums[a]+nums[b]+nums[c]
        #             if possibleSum in seenAlready:
        #                 count += seenAlready[possibleSum]
        #     seenAlready[nums[a]] += 1
        # return count
# 倒序


        # count = 0
        # n = len(nums)
        # seenAlready = defaultdict(int)
        # for a in range(n-1,0,-1):
        #     for b in range(a-1,-1,-1):
        #         count += seenAlready[nums[a]+nums[b]]
        #     for d in range(n-1,a,-1):
        #         seenAlready[nums[d]-nums[a]] += 1         # d-a
        # return count



# Runtime: 1684 ms, faster than 38.15% of Python3 online submissions for Count Special Quadruplets.
# Memory Usage: 14.2 MB, less than 50.26% of Python3 online submissions for Count Special Quadruplets.
    def countQuadruplets2(self, nums: List[int]) -> int:
        ans = 0
        sz1 = len(nums)
        for i in range(0, sz1):
            for j in range(i + 1, sz1):
                for k in range(j + 1, sz1):
                    for m in range(k + 1, sz1):
                        if nums[m] == (nums[i] + nums[j] + nums[k]):
                            ans += 1
        return ans


# ... error.. a<b<c<d  所以不能排序的。。。
    # length<50 for for for ...
    # a+b = d-c 需要确保下标唯一性，
    # a+b 然后 while (l<r) 搜索 d，c ？
    # ...List[T] 3.9 移除了。。。内置的list支持泛型了。
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        # nums = sorted(nums)       # 不修改原来数组。
        nums.sort()
        sz1 = len(nums)
        map2 = {}
        for v in nums:
            map2[v] = (map2[v] if v in map2 else 0) + 1
        # print(nums)
        # print(map2)
        for i, v in enumerate(nums):
            for j in range(i + 1, sz1):
                for k in range(j + 1, sz1):
                    sum2 = v + nums[j] + nums[k]            # no zero
                    if sum2 in map2:
                        print(str(sum2) + ", " + str(i) + ", " + str(j) + ", " + str(k))
                        ans += map2[sum2]
        return ans



if __name__ == '__main__':
    sol = LT1995()
    # arr = [1,2,3,6
    # arr = [3,3,6,4,5]
    # arr = [1,1,1,3,5]
    arr = [28,8,49,85,37,90,20,8]
    # print(arr)
    # print(type(arr))
    print(sol.countQuadruplets2(arr))

    