# 5 kyu  Python
# https://www.codewars.com/kata/5dd82b7cd3d6c100109cb4ed
d = [[0] * 6 for i in range(6)]
x = 1
y = 5
for i in range(0, 6):
    for j in range(0, 6):
        d[i][j] = i + j

print(d)
# def distancesum(a, n):
#     # sorting the att\\rr[ay.
#     a.sort()
#
#     # for each point, finding
#     # the distance.
#     res = 0
#     sum = 0
#     for i in range(n):
#         res += (a[i] * i - sum)
#         sum += a[i]
#
#     return res
#
#
# def totaldistancesum(x, y, n):
#     return distancesum(x, n) + distancesum(y, n)
#
#
# # Driven Code
# x = [-1, 1, 3, 2]
# y = [5, 6, 5, 3]
# n = len(x)
# print(totaldistancesum(x, y, n))

# @test.describe("sample tests")
# def basic_tests():
#     @test.it("Returnes top left corner for agent in the bottom right")
#     def test_2x2grid1():
#         test.assert_equals(advice([(1, 1)], 2), [(0, 0)])
#
#     @test.it("Returns empty list for size 0")
#     def test_size_0():
#         test.assert_equals(advice([(1, 1)], 0), [])
#
#     @test.it("Works for the example in description")
#     def test_description():
#         test.assert_equals(advice([(0, 0), (1, 5), (5, 1)], 6), [(2, 2), (3, 3), (4, 4), (5, 5)])
#
#     @test.it("returns empty list for agents everywhere")
#     def test_agents_everywhere():
#         agents = []
#         for x in range(10):
#             for y in range(10):
#                 agents.append((x, y))
#         test.assert_equals(advice(agents, 10), [])
#
#     @test.it("Returns all locations for only ignored agents")
#     def test_size_0():
#         test.assert_equals(advice([(9, 9)], 1), [(0, 0)])
#
#     @test.it("returns correct solutions for six agents")
#     def six_agents():
#         test.assert_equals(
#             sorted(advice([(1, 1), (3, 5), (4, 8), (7, 3), (7, 8), (9, 1)], 10)),
#             sorted([(0, 9), (0, 7), (5, 0)])
#         )
#
#     @test.it("returns correct solutions for seven agents")
#     def seven_agents():
#         test.assert_equals(
#             sorted(advice([(1, 3), (2, 3), (2, 7), (4, 1), (5, 9), (7, 0), (9, 5)], 10)),
#             sorted([(0, 0), (0, 9), (4, 5), (5, 5), (5, 4), (6, 3), (6, 4),
#                     (6, 6), (7, 7), (8, 8), (9, 9)])
#         )
#
#     @test.it("returns correct solutions for another six agents")
#     def six_agents_2():
#         test.assert_equals(
#             sorted(advice([(0, 0), (0, 9), (1, 5), (5, 1), (9, 0), (9, 9)], 10)),
#             sorted([(5, 7), (6, 6), (7, 5)]))
#
#     @test.it("single agent in top left corner of large grid")
#     def test_single_agent():
#         test.assert_equals(advice([(0, 0)], 10), [(9, 9)])
#
#     @test.it("agent in top left and bottom right")
#     def test_two_agents():
#         test.assert_equals(sorted(advice([(0, 0), (1, 1), (99, 99)], 2)), sorted([(0, 1), (1, 0)]))
# def advice():
#     return y
#
#
# if __name__ == '__main__':
#     print(xxxxxx()
#     s = value
#     assert xxxxxx(s) == answer
#
#     if __name__ == '__main__':
#         print(xxxxxx(x))
