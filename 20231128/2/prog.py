import math
import sys

oper =  ['add', 'sub', 'mul', 'div']
ifs = ['ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle']
pr = list()
vrs, lbls = dict(), dict()
id_of_pos = 0
for st in sys.stdin.readlines():
    st = st.strip()
    st = st.split()
    if len(st) == 0:
        continue
    if st[0][-1] == ':':
        lbls[st[0][:-1]] = id_of_pos
        st.pop(0)
        if len(st) == 0:
            continue
    match st:
        case ['stop']:
            pr.append(['stop', ])
        case ['store', n, vr]:
            pr.append(['store', n, vr])
        case [op, r_1, r_2, r_3] if op in oper:
            pr.append([op, r_1, r_2, r_3])
        case [comp, r_1, r_2, lab] if comp in ifs:
            pr.append([comp, r_1, r_2, lab])
        case ['out', vr]:
            pr.append(['out', vr])
        case _:
            continue
    id_of_pos += 1
tmp = False
pr.append(['stop'])
for id in pr:
    if id[0] in ifs and id[3] not in lbls:
    	exit(0)

id = 0
while True:
	st = pr[id]
	match st:

		case ['store', n, vr]:
			try:
				vrs[vr] = float(n)
			except Exception:
				pass
			id += 1
		case ['stop']:
			break
		case [op, r_1, r_2, r_3] if op in oper:
			r_1 = vrs.setdefault(r_1, 0)
			r_2 = vrs.setdefault(r_2, 0)
			match op:
				case 'add':
					vrs[r_3] = r_1 + r_2
				case 'sub':
					vrs[r_3] = r_1 - r_2
				case 'mul':
					vrs[r_3] = r_1 * r_2
				case 'div':
					try:
						vrs[r_3] = r_1 / r_2
					except Exception:
						vrs[r_3] = math.inf

			id += 1
		case [comp, r_1, r_2, lab] if comp in ifs:
			r_1 = vrs.setdefault(r_1, 0)
			r_2 = vrs.setdefault(r_2, 0)
			match comp:
				case 'ifeq':
					if r_1 == r_2:
						id = lbls[lab]
					else:
						id += 1
				case 'ifne':
					if r_1 != r_2:
						id = lbls[lab]
					else:
						id += 1
				case 'ifgt':
					if r_1 > r_2:
						id = lbls[lab]
					else:
						id += 1
				case 'ifge':
					if r_1 >= r_2:
						id = lbls[lab]
					else:
						id += 1
				case 'iflt':
					if r_1 < r_2:
						id = lbls[lab]
					else:
						id += 1
				case 'ifle':
					if r_1 <= r_2:
						id = lbls[lab]
					else:
						id += 1
		case ['out', vr]:
			print(vrs.setdefault(vr, 0))
			id += 1
		case _:
			id += 1
			continue