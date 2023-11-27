import sys
sys.getdefaultencoding()

while st := sys.stdin.readline():
    st = st.encode("latin1", errors='replace')
    print(st.decode("CP1251", errors='replace'), end='')