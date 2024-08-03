from collections import Counter, defaultdict, namedtuple

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
print(Counter(mylist))

mylist = ["a", "a", 10, 10, 10]
print(Counter(mylist))

print(Counter("aaaaabbbbbcccee"))

sentence = "How may times does each word show up in this sentence with a word"
print(Counter(sentence.lower().split()))

letters = "aaaaabbbcccccdddd"

c = Counter(letters)
print(c.most_common())


d = defaultdict(lambda: 0)

d["correct"] = 100
print(d)

print(d["WRONG KEY"])

mytuple = (10, 20, 30)

print(mytuple[0])

Dog = namedtuple("Dog", ["age", "breed", "name"])

print(Dog)


sammy = Dog(age=5, breed="Husky", name="Sam")
print(type(sammy))
