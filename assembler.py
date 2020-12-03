CODE_SEGMENT_SIZE = 2048
MEM_SEGMENT_SIZE = 512
opcodes = {
    "MUL": 1,
    "SUB": 2,
    "NOT": 3,
    "XOR": 4,
    "MOVI": 5,
    "MOV": 6,
    "JMP": 7,
    "OUT": 8,
    "XIT": 9,
    "IN": 10,
    "LSHIFT": 11,
    "AND": 12,
    "OR": 13,
    "ADD": 14, # add register
    "HALT": 101,
}

regs = {
    "REG1": 0,
    "REG2": 1,
    "REG3": 2,
    "REG4": 3
}

program = """MOV REG1,0
MOV REG2,1
MOV REG3,2
MOV REG4,3
NOT REG1
NOT REG2
NOT REG3
NOT REG4
OUT
MOVI REG1,REG2
OUT
MOVI REG1,REG3
OUT
MOVI REG1,REG4
OUT

MOV REG1,4
MOV REG2,5
MOV REG3,6
MOV REG4,7
NOT REG1
NOT REG2
NOT REG3
NOT REG4
OUT
MOVI REG1,REG2
OUT
MOVI REG1,REG3
OUT
MOVI REG1,REG4
OUT

MOV REG1,8
MOV REG2,9
MOV REG3,10
MOV REG4,11
NOT REG1
NOT REG2
NOT REG3
NOT REG4
OUT
MOVI REG1,REG2
OUT
MOVI REG1,REG3
OUT
MOVI REG1,REG4
OUT

MOV REG1,12
MOV REG2,13
MOV REG3,14
MOV REG4,15
NOT REG1
NOT REG2
NOT REG3
NOT REG4
OUT
MOVI REG1,REG2
OUT
MOVI REG1,REG3
OUT
MOVI REG1,REG4
OUT

# x ^ 99
#c
IN
XOR REG1,16
ADD REG4,REG1

# ~(x ^ 7) + x
#t
IN
MOVI REG2,REG1
XOR REG1,17
NOT REG1
ADD REG1,REG2
ADD REG4,REG1

#((x ^ 138) + ((x & 138) << 1) | 16) + ((x ^ 138) + ((x & 138) << 1) & 16)
#f
IN
MOVI REG2,REG1
#x^138
XOR REG1,18
#x&138
AND REG2,18
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,19
OR REG3,19
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

# (x ^ 133) + 2*(x & 133)
#{
IN
MOVI REG2,REG1
XOR REG2,20
AND REG1,20
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

# (x ^ 133) + 2*(x & 133)
#{
IN
MOVI REG2,REG1
XOR REG2,20
AND REG1,20
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

# (x ^ 138) + 2*(x & 138)
#v
IN
MOVI REG2,REG1
XOR REG2,21
AND REG1,21
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1


HALT
"""

program = program.splitlines()

assembled = []

mem = [
    # map(lambda x: (~ord(x))&0xff,"Enter the flag: ")
    186, 145, 139, 154, 141, 223, 139, 151, 154, 223, 153, 147, 158, 152, 197, 223,


    # c
    99,
    # t
    7,
    # f
    138, 16,
    # {
    133,
    # v
    138,

]


for inst in program:
    if len(inst) == 0:
        continue
    if inst[0] == "#":
        continue
    o = inst.split()
    oo = o[0]
    if len(o) == 1:
        assembled.extend([opcodes[o[0]], 0, 0])

    # two operand instructions
    elif oo == "NOT":
        arg1 = o[1]
        assembled.extend( [opcodes["NOT"], regs[arg1], 0] )
    else:
        arg1, arg2 = o[1].split(',')
        if oo == "MUL":
            assembled.extend( [opcodes["MUL"], regs[arg1], int(arg2)] )
        elif oo == "SUB":
            assembled.extend( [opcodes["SUB"], regs[arg1], int(arg2)] )
        elif oo == "NOT":
            assembled.extend( [opcodes["NOT"], regs[arg1], 0] )
        elif oo == "XOR":
            assembled.extend( [opcodes["XOR"], regs[arg1], int(arg2)] )
        elif oo == "MOVI":
            assembled.extend( [opcodes["MOVI"], regs[arg1], regs[arg2]] )
        elif oo == "MOV":
            assembled.extend( [opcodes["MOV"], regs[arg1], int(arg2)] )
        elif oo == "ADD":
            assembled.extend( [opcodes["ADD"], regs[arg1], regs[arg2]] )
        elif oo == "AND":
            assembled.extend( [opcodes["AND"], regs[arg1], int(arg2)] )
        elif oo == "LSHIFT":
            assembled.extend( [opcodes["LSHIFT"], regs[arg1], int(arg2)] )
        elif oo == "OR":
            assembled.extend( [opcodes["OR"], regs[arg1], int(arg2)] )
        else:
            print(oo)
            raise Exception

# filling array
while len(assembled) < 512:
    assembled.append(0)

output = assembled + mem

ooo = str(output).replace('[', '{').replace(']', '}') + ";"
print(ooo)