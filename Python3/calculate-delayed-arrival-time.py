# https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        if arrivalTime + delayedTime > 23:
            return (arrivalTime + delayedTime) % 24
        
        return arrivalTime + delayedTime