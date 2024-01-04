# https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        batteryPercentagesLen = len(batteryPercentages)

        for index in range(batteryPercentagesLen):
            if batteryPercentages[index] > 0:
                ans += 1

                for index2 in range(index + 1, batteryPercentagesLen):
                    batteryPercentages[index2] = max(0, batteryPercentages[index2] - 1)

        return ans