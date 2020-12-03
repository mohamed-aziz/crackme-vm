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

MOV REG4,0
XOR REG4,0

# x ^ 99
#c
IN
XOR REG1,16
ADD REG4,REG1

# ~x ^ 139
#t
IN
NOT REG1
XOR REG1,17
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

# (x ^ 138) + 2*(x & 138)
#v
IN
MOVI REG2,REG1
XOR REG2,21
AND REG1,21
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

# ~(x ^ 1) + x
#1
IN
MOVI REG2,REG1
XOR REG1,22
NOT REG1
ADD REG1,REG2
ADD REG4,REG1

# (x ^ 142) + 2*(x & 142)
# r
IN
MOVI REG2,REG1
XOR REG2,23
AND REG1,23
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

# x ^ 116
#t
IN
XOR REG1,24
ADD REG4,REG1

#(x ^ 139) + 2*(x & 139)
#u
IN
MOVI REG2,REG1
XOR REG2,25
AND REG1,25
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#(x ^ 204) + 2*(x & 204)
#4
IN
MOVI REG2,REG1
XOR REG2,26
AND REG1,26
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#(x ^ 148) + 2*(x & 148)
#l
IN
MOVI REG2,REG1
XOR REG2,27
AND REG1,27
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#x ^ 95
#_
IN
XOR REG1,28
ADD REG4,REG1

#~x ^ 146
#m
IN
NOT REG1
XOR REG1,29
ADD REG4,REG1

#~x ^ 203
#4
IN
NOT REG1
XOR REG1,30
ADD REG4,REG1

#((x ^ 237) + ((x & 237) << 1) | 176) +
#((x ^ 237) + ((x & 237) << 1) & 176)
#c
IN
MOVI REG2,REG1
#x^138
XOR REG1,31
#x&138
AND REG2,31
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,32
OR REG3,32
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

#~x ^ 151
#h
IN
NOT REG1
XOR REG1,33
ADD REG4,REG1

#x ^ 105
#i
IN
XOR REG1,34
ADD REG4,REG1

#~x ^ 145
#n
IN
NOT REG1
XOR REG1,35
ADD REG4,REG1

# (x ^ 155) + 2*(x & 155)
#e
IN
MOVI REG2,REG1
XOR REG2,36
AND REG1,36
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#x ^ 95
#_
IN
XOR REG1,37
ADD REG4,REG1

#((x ^ 80) + ((x & 80) << 1) | 64) +
#((x ^ 80) + ((x & 80) << 1) & 64)
#p
IN
MOVI REG2,REG1
#x^138
XOR REG1,38
#x&138
AND REG2,38
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,39
OR REG3,39
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

#x ^ 114
#r
IN
XOR REG1,40
ADD REG4,REG1

#~x ^ 207
#0
IN
NOT REG1
XOR REG1,41
ADD REG4,REG1

#(x ^ 140) + 2*(x & 140)
#t
IN
MOVI REG2,REG1
XOR REG2,42
AND REG1,42
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#((x ^ 27) + ((x & 27) << 1) | 128) +
#((x ^ 27) + ((x & 27) << 1) & 128)
#e
IN
MOVI REG2,REG1
#x^138
XOR REG1,43
#x&138
AND REG2,43
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,44
OR REG3,44
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

#~x ^ 156
#c
IN
NOT REG1
XOR REG1,45
ADD REG4,REG1

#((x ^ 60) + ((x & 60) << 1) | 80) +
#((x ^ 60) + ((x & 60) << 1) & 80)
#t
IN
MOVI REG2,REG1
#x^138
XOR REG1,46
#x&138
AND REG2,46
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,47
OR REG3,47
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

#~x ^ 150
#i
IN
NOT REG1
XOR REG1,48
ADD REG4,REG1

#x ^ 111
#o
IN
XOR REG1,49
ADD REG4,REG1

#(x ^ 146) + 2*(x & 146)
#n
IN
MOVI REG2,REG1
XOR REG2,50
AND REG1,50
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#((x ^ 64) + ((x & 64) << 1) | 97) +
#((x ^ 64) + ((x & 64) << 1) & 97)
#_
IN
MOVI REG2,REG1
#x^138
XOR REG1,51
#x&138
AND REG2,51
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,52
OR REG3,52
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

#(x ^ 151) + 2*(x & 151)
#i
IN
MOVI REG2,REG1
XOR REG2,53
AND REG1,53
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#~x ^ 140
#s
IN
NOT REG1
XOR REG1,54
ADD REG4,REG1

#~x ^ 160
#_
IN
NOT REG1
XOR REG1,55
ADD REG4,REG1

#(x ^ 141) + 2*(x & 141)
#s
IN
MOVI REG2,REG1
XOR REG2,56
AND REG1,56
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#~x ^ 144
#o
IN
NOT REG1
XOR REG1,57
ADD REG4,REG1

#(x ^ 145) + 2*(x & 145)
#o
IN
MOVI REG2,REG1
XOR REG2,58
AND REG1,58
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#((x ^ 64) + ((x & 64) << 1) | 97) +
#((x ^ 64) + ((x & 64) << 1) & 97)
#_
IN
MOVI REG2,REG1
#x^138
XOR REG1,59
#x&138
AND REG2,59
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,60
OR REG3,60
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

#(x ^ 206) + 2*(x & 206)
#2
IN
MOVI REG2,REG1
XOR REG2,61
AND REG1,61
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#~x ^ 207
#0
IN
NOT REG1
XOR REG1,62
ADD REG4,REG1

#(x ^ 207) + 2*(x & 207)
#1
IN
MOVI REG2,REG1
XOR REG2,63
AND REG1,63
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#((x ^ 144) + ((x & 144) << 1) | 64) +
#((x ^ 144) + ((x & 144) << 1) & 64)
IN
MOVI REG2,REG1
#x^138
XOR REG1,64
#x&138
AND REG2,64
#(x&138) << 1
LSHIFT REG2,1
MOVI REG3,REG2
ADD REG2,REG1
ADD REG3,REG1
AND REG2,65
OR REG3,65
ADD REG2,REG3
MOVI REG1,REG2
MOVI REG4,REG2

#(x ^ 161) + 2*(x & 161)
#_
IN
MOVI REG2,REG1
XOR REG2,66
AND REG1,66
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#~x ^ 135
#x
IN
NOT REG1
XOR REG1,67
ADD REG4,REG1

#(x ^ 188) + 2*(x & 188)
#D
IN
MOVI REG2,REG1
XOR REG2,68
AND REG1,68
MUL REG1,2
ADD REG1,REG2
ADD REG4,REG1

#~x ^ 130
#}
IN
NOT REG1
XOR REG1,69
ADD REG4,REG1

MOVI REG1,REG4
JMP 66
MOV REG1,70
OUT
MOV REG1,71
OUT
MOV REG1,72
OUT
MOV REG1,73
OUT
MOV REG1,74
OUT
MOV REG1,75
OUT
MOV REG1,76
OUT
MOV REG1,77
OUT
MOV REG1,78
OUT
MOV REG1,0
XOR REG1,0
XIT

MOV REG1,79
OUT
MOV REG1,80
OUT
MOV REG1,81
OUT
MOV REG1,82
OUT
MOV REG1,83
OUT
MOV REG1,84
OUT
MOV REG1,85
OUT
MOV REG1,86
OUT
MOV REG1,87
OUT
MOV REG1,88
OUT

MOV REG1,0
XIT
"""

program = program.splitlines()

assembled = []

mem = [
    # map(lambda x: (~ord(x))&0xff,"Enter the flag: ")
    186, 145, 139, 154, 141, 223, 139, 151, 154, 223, 153, 147, 158, 152, 197, 223,

    # c
    99,
    # t
    139,
    # f
    138, 16,
    # {
    133,
    # v
    138,
    # 1
    1,
    # r
    142,
    #t
    116,
    #u
    139,
    #4
    204,
    #l
    148,
    #_
    95,
    #m
    146,
    #4
    203,
    #c
    237, 176,
    #h
    151,
    #i
    105,
    #n
    145,
    #e
    155,
    #_
    95,
    #p
    80,64,
    #r
    114,
    #0
    207,
    #t
    140,
    #e
    27,128,
    #c
    156,
    #t
    60,80,
    #i
    150,
    #o
    111,
    #n
    146,
    #_
    64,97,
    #i
    151,
    #s
    140,
    #_
    160,
    #s
    141,
    #o
    144,
    #o
    145,
    #_
    64,97,
    #2
    206,
    #0
    207,
    #1
    207,
    #0
    144,64,
    #_
    161,
    #x
    135,
    #D
    188,
    #}
    130,
    # Good Job\n
    71, 111, 111, 100, 32, 74, 111, 98, 10,

    # Try again\n
    84, 114, 121, 32, 97, 103, 97, 105, 110, 10,
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
    elif oo == "JMP":
        arg1 = o[1]
        assembled.extend( [opcodes["JMP"], int(arg1), 0] )        
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
while len(assembled) < CODE_SEGMENT_SIZE:
    assembled.append(0)

output = assembled + mem

ooo = str(output).replace('[', '{').replace(']', '}') + ";"
print(ooo)