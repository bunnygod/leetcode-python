class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        index = 0

        for i in range(1, n + 1):
            if index == len(target):
                break

            if target[index] == i:
                res.append("Push")
                index += 1
            else:
                res.append("Push")
                res.append("Pop")

        return res