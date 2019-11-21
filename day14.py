class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        min = 101
        max = 0
        for element in self.__elements:
            if element < min:
                min = element
            if element > max:
                max = element
        self.maximumDifference = max-min

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
