import z3
import random
import sys
num_params = {
    0: 2,
    1: 3,
    2: 2,
    3: 2,
    4: 2,
    #5: 3
}

operations = [
    lambda x,y: (x^y)+2*(x & y), # x+y
    lambda x,y,z: ((x ^ y) + ((x & y) << 1) | z) +((x ^ y) + ((x & y) << 1) & z), # x + y + z
    lambda x,y: x^y,
    lambda x,y: ~(x)^y,
    #lambda x,y: ~(x^y)+x,
]

flag = "ctf{v1rtu4l_m4chine_pr0tection_is_soo_2010_xD}"
import time 
random.seed(time.time())
print(flag[:1+int(sys.argv[1])])

print("Generating constraints for {}".format(flag[int(sys.argv[1])]))

for f in flag[int(sys.argv[1])]:
    solver = z3.Solver()
    x = ord(f)
    symx = z3.BitVec('x', 8)
    y = z3.BitVec('y', 8)

    choice = random.randint(0, len(operations)-1)
    if num_params[choice] == 2:
        o = operations[choice](x,y)
        solver.add(o == 0)
    elif num_params[choice] == 3:
        z = z3.BitVec('z', 8)
        o = operations[choice](x,y,z)
        solver.add(o == 0)
    print(solver)
    if solver.check() == z3.sat:
        m = solver.model()
        if num_params[choice] == 2:
            my = m[y].as_long()
            print(operations[choice](symx,my))
        elif num_params[choice] == 3:
            my = m[y].as_long()
            mz = m[z].as_long()
            print(operations[choice](symx,my,mz))

    else:
        raise Exception
