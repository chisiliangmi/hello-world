# 口令保管箱
import sys, pyperclip

PASSWORDS = {
        '知乎': 'FosTIn703884438nohsg',
        'GitHub': 'oncos8743276@@',
        'QQ邮箱': '123345',
        'CSDN': ''
        }
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print('There is no account named ' + account)
