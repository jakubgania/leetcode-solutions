# https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = round(celsius + 273.15, 5)
        farenheit = round(celsius * 1.80 + 32.00, 5)

        return [kelvin, farenheit]