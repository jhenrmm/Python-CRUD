import where

username = input('Type the person name: ')
user_email = input('Type the e-mail of this person: ')

while True:
    ans = input('Do you want to continue? [Y/N] ').strip().lower()
    if ans in ('y', 'n'):
        break
    print('ERROR! Type only [Y/N]')

where.create_user(username, user_email)
