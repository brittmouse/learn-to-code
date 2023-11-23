#!/usr/bin/python3
# CCC07J1 - Who's in the Middle?
def middle(a, b, c):
  user_list = [a, b, c]
  user_list.sort()
  return user_list[1]

print(middle(5, 7, 1))
print(middle(93, 2, 56))
