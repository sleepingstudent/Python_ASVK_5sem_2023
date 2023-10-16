st = input()
hight = 1
width = len(st) - 2
cnt_water = 0
cnt_nowater = 0
while(True):
    st = input()
    hight += 1
    if st[1] == '.':
        cnt_nowater += width
    elif st[1] == '~':
        cnt_water += width
    else:
        break
print(hight * '#')
hight_water = (cnt_water + hight - 3) // (hight - 2)
hight_nowater = width - hight_water
for i in range(hight_nowater):
    print('#' + (hight - 2) * '.' + '#')
for i in range(hight_water):
    print('#' + (hight - 2) * '~' + '#')
print(hight * '#')
cnt_water = hight_water * (hight - 2)
cnt_nowater = hight_nowater * (hight - 2)
cnt = cnt_water + cnt_nowater
tmp = max(len(str(cnt_water)), len(str(cnt_nowater)))
tmp2 = max(cnt_water, cnt_nowater)
print(f"{'.'*cnt_nowater:<{tmp2 + 1}}{cnt_nowater:>{tmp}}/{cnt}")

print(f"{'~'*cnt_water:<{tmp2 + 1}}{cnt_water:>{tmp}}/{cnt}")
