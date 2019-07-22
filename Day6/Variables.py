# input_var = input("Enter some data:  ")
# e = ("This is your data" + input_var)
# print(e)

l1 = [1,5]
l1.append(8)
l1.append(7)
print(l1)

l1.pop()
print(l1)

l1.append(7)
l1.append(4)
l1[0] = 675
print(l1)

print(l1[0:2])
print(l1[::2])
print(l1[::-1])

del l1[2]
print(l1)

l2 =  [14,44,65,2,25,56]
l3 = l1 + l2
print(l3)
# print(l1.extend(l2))

l3.remove(44)
print(l3)
if 1 in l3:
    print("True")
else:
    print("False")

print(len(l3))

f, g, h = 6, 7, 10
print(f+g+h)

if f > g:
    print("False")
else:
    print("True")

empty_dict = {}
filled_dictionary = {"one":1, "two":2, "three":3}
print(filled_dictionary.values())

print(filled_dictionary.items())

if "four" in filled_dictionary:
    print("True")
else:
    print("False")

print(filled_dictionary.get("one"))

filled_dictionary["four"] = 4

print(filled_dictionary)
filled_dictionary.setdefault("five", 5)
print(filled_dictionary)
