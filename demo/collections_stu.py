names = ["max", "james", "lulu"]

names.extend(["hoo"])
names.extend("bob")

n = names.pop()
print(n)
print(names)

nums = (1, 2, 3, 5, 12, 11, 1, 0)  # tuple
cnt = nums.count(1)
print(cnt)
idx = nums.index(11)
print(idx)
