# nested loop is a loop inside a loop


# 2 dimensional list
my_list = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

#print(my_list[2][2])

for lists in my_list:
    for row in lists:
        print(row)