
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words) # 出来就是一个字典
        candidates = list(count.keys())
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]


# import collections
# import heapq
# import functools
#
# # 这个装饰器是在python2.7的时候加上的，它是针对某个类如果定义了__lt__、le、gt、__ge__这些方法中的至少一个，使用该装饰器，则会自动的把其他几个比较函数也实现在该类中
# @functools.total_ordering
# class Element:
#     def __init__(self, count, word):
#         self.count = count
#         self.word = word
#
#     def __lt__(self, other): # less than 小于
#         if self.count == other.count:
#             return self.word > other.word # 字母顺序，按照反着的顺序比较
#         return self.count < other.count  # 字母个数，按照正着的顺序比较
#
#     def __eq__(self, other):
#         return self.count == other.count and self.word == other.word
#
#
# class Solution(object):
#     def topKFrequent(self, words, k):
#         """
#         :type words: List[str]
#         :type k: int
#         :rtype: List[str]
#         """
#         counts = collections.Counter(words) # 一个非常重要的，制作词典的方式
#
#         freqs = []
#         heapq.heapify(freqs)
#         for word, count in counts.items():
#             heapq.heappush(freqs, (Element(count, word), word)) #
#             if len(freqs) > k:
#                 heapq.heappop(freqs)
#
#         res = []
#         for _ in range(k):
#             res.append(heapq.heappop(freqs)[1]) # res 的顺序是从小到大的
#         return res[::-1]                        # 所以这里要倒过来，变成从大到小
