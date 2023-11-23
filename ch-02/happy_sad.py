#!/usr/bin/python3
# CCC15J2 - Happy or Sad
def happysad(user_in):
  if ':-)' not in user_in and ':-(' not in user_in:
    return 'none'
  elif user_in.count(':-)') > user_in.count(':-('):
    return 'happy'
  elif user_in.count(':-)') < user_in.count(':-('):
    return 'sad'
  return 'unsure'

print(happysad('I can\'t believe he left me :-('))
print(happysad(':-) Finally, a good grade :-)'))
print(happysad('Yay Mcdonalds! :-) Wait why is he getting coffee? :-('))
print(happysad('Somebody once told me the world was gonna roll me'))
