#!/usr/bin/python3
# WC18C3J1 - An Honest Day's Work
def daily_income(p, b, d):
  # p: how many litres of paint Jesse has
  # b: how many litres of paint it takes to forge a bottlecap 'badge'
  # d: the price each badge will sell for
  # 'p // b * d' takes the number of painted bottlecaps (paint // paint per cap) and multiplies by price of cap
  # 'p % b' takes the leftover paint (remainer) and sells it for one pokebuck
  return (p // b * d) + (p % b)

print('TEAM ROCKET NEEDS SOME FUNDS')
paint = int(input('How many litres of paint does Jesse have on him? '))
bottlecaps = int(input('How many litres of paint does it take to paint a bottlecap? '))
price = int(input('How many Pokebucks does each painted bottlecap sell for? '))
print(daily_income(paint, bottlecaps, price))
