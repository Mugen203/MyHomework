# list = []
# def min(list):
#      cur_min = list[0]
#      second_min = list[1]
#      for i in list:
#         if i < cur_min:
#             cur_min = i
#         elif second_min == list[1] or second_min > i:
#             second_min = i
#
#      print("Smallest number in this list:", cur_min)
#      print("Second smallest number in this list:", second_min)
#
# list = [11,5,3,6,7,-1,77]
# print(min(list))
list = []
def min(list):
        list.sort()

        print("Smallest number in this list:", list[0])
        print("Second smallest number in this list", list[1])
list = [11,5,3,6,7,-1,77]
print(min(list))
