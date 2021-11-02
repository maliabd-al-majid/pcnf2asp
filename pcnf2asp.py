import sys


def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result


# print sys.argv[1]
cnf = open(sys.argv[1], 'r')
f = open(sys.argv[1] + '.asp', "w")

# asp = set()
showRule = ''
for line in cnf.readlines():
    if not ('p' and 'c') in line:
        propositional = line.split(' ')
        del propositional[-1]
        if 'vp' not in line:
            atoms = set()
            negated_atoms = set()
            for p in propositional:  # re format input
                if int(p) < 0:
                    original_p = p.replace('-', 'x')
                    not_p = p.replace('-', 'x')
                else:
                    original_p = 'x' + p
                    not_p = 'not x' + p
                atoms.add(original_p)
                negated_atoms.add(not_p)
            # atoms =['x'+s for s in propositional]
            choiceRule = '{' + ''.join(intersperse(atoms, ';')) + '}.'
            constraint = ':-' + ''.join(intersperse(negated_atoms, ',')) + '.'
            f.write(choiceRule + '\n')
            f.write(constraint + '\n')
        else:
            del propositional[0]

            for p in propositional:
                showRule += '#show x' + str(abs(int(p))) + '/0.' + '\n'

f.write(showRule + '\n')
f.close()
