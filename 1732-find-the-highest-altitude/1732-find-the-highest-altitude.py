class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude=[0]
        start=0
        for i in gain:
            inc=i+start
            altitude.append(inc)
            start=inc
        return max(altitude)