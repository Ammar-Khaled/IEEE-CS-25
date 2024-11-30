keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
dir = input()
after = input()
n = len(after)
before = ''

for i in range(n):
    ch = after[i]
    if dir == 'R':
        before += keyboard[keyboard.index(ch) - 1]
    else:
        before += keyboard[keyboard.index(ch) + 1]

print(before)