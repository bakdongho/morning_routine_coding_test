class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs or not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        temp_strs = strs.copy()

        first_string = temp_strs.pop(0)
        index = 0

        for idx, s in enumerate(first_string):
            try:
                if any(s != other_s[idx] for other_s in temp_strs):
                    index = idx
                    break
                else:
                    index = idx + 1
            except IndexError:
                index = idx
                break

        return first_string[:index]


inputs = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["flower", "flow", "flowell"],
    ["flower", "flower", "flower"],
    ["a"],
]
expects = ["fl", "", "flow", "flower", "a"]

if __name__ == "__main__":
    solution = Solution()
    for num, (input, expected) in enumerate(zip(inputs, expects)):
        result = (
            "통과" if expected == solution.longestCommonPrefix(strs=input) else "실패"
        )
        print(f"{num+1}번째 테스트 {result}!!")
