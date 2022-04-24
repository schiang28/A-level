from sys import argv
from os import path
from re import sub, search

OK = 0
ERROR = 1


def r(operand):
    try:
        if operand[0].lower() == "r":
            return int(operand[1:])
        raise SyntaxError(operand)
    except (ValueError, IndexError):
        raise SyntaxError(operand)


def op2(operand, regs):
    try:
        if operand[0].lower() == "r":
            return regs[int(operand[1:])]
        elif operand[0] == "#":
            return int(operand[1:])
        raise SyntaxError(operand)
    except (ValueError, IndexError):
        raise SyntaxError(operand)


def mem(operand, memory):
    if operand.startswith("#"):
        raise SyntaxError(f"No # in memory reference with {operand}")
    try:
        return int(memory[int(operand)])
    except (ValueError, IndexError):
        raise SyntaxError(operand)


def load(operands, memory, regs, status):
    regs[r(operands[0])] = mem(operands[1], memory)


def store(operands, memory, regs, status):
    if operands[1].startswith("#"):
        raise SyntaxError(f"No # in memory reference with {operands[1]}")
    try:
        memory[int(operands[1])] = regs[r(operands[0])]
    except (ValueError, IndexError):
        raise SyntaxError(operands)


def add(operands, memory, regs, status):
    regs[r(operands[0])] = regs[r(operands[1])] + op2(operands[2], regs)


def multiply(operands, memory, regs, status):
    print("Note that MUL is not in AQA Exam Assembler")
    regs[r(operands[0])] = regs[r(operands[1])] * op2(operands[2], regs)


def subtract(operands, memory, regs, status):
    regs[r(operands[0])] = regs[r(operands[1])] - op2(operands[2], regs)


def bitwise_or(operands, memory, regs, status):
    regs[r(operands[0])] = regs[r(operands[1])] | op2(operands[2], regs)


def bitwise_and(operands, memory, regs, status):
    regs[r(operands[0])] = regs[r(operands[1])] & op2(operands[2], regs)


def bitwise_eor(operands, memory, regs, status):
    regs[r(operands[0])] = regs[r(operands[1])] ^ op2(operands[2], regs)


def assign(operands, memory, regs, status):
    regs[r(operands[0])] = op2(operands[1], regs)


def bitwise_not(operands, memory, regs, status):
    regs[r(operands[0])] = ~op2(operands[1], regs)


def shift_left(operands, memory, regs, status):
    regs[r(operands[0])] = regs[r(operands[1])] << op2(operands[2], regs)


def shift_right(operands, memory, regs, status):
    regs[r(operands[0])] = regs[r(operands[1])] >> op2(operands[2], regs)


def compare(operands, memory, regs, status):
    o1 = regs[r(operands[0])]
    o2 = op2(operands[1], regs)
    status["EQ"] = o1 == o2
    status["NE"] = o1 != o2
    status["GT"] = o1 > o2
    status["LT"] = o1 < o2


def branch(operands, memory, regs, status):
    regs["pc"] = int(operands[0])


def branch_lt(operands, memory, regs, status):
    if status["LT"]:
        branch(operands, memory, regs, status)


def branch_gt(operands, memory, regs, status):
    if status["GT"]:
        branch(operands, memory, regs, status)


def branch_eq(operands, memory, regs, status):
    if status["EQ"]:
        branch(operands, memory, regs, status)


def branch_ne(operands, memory, regs, status):
    if status["NE"]:
        branch(operands, memory, regs, status)


def halt(operands, memory, regs, status):
    status["RUN"] = False


def nop(operands, memory, regs, status):
    raise SyntaxError
    # print("NOP parsed with operands:",*operands)


def show_regs(regs):
    print("Registers:\n", "\n".join([f"{r} : {v}" for r, v in regs.items()]), sep="")


def show_memory(memory, address=None):
    if address:
        print(f"Memory[{address}]: {memory[address]}")
    else:
        print("Memory:", *[str(data) for data in memory], sep="\n")


def show_labels(labels, memory):
    print(
        "Labels:",
        *[
            f"{label} : {memory[address]}"
            for label, address in labels.items()
            if memory[address]
        ],
        sep="\n",
    )


def fetch(regs, memory):
    cir = memory[regs["pc"]]
    regs["pc"] += 1
    return cir


def decode(cir):
    if cir:
        opcode, *operands = [x.strip() for x in cir.split()]
        return opcode, operands
    else:
        return "NOP", []


def execute(opcode, operands, memory, regs, status):
    alu = {
        "LDR": load,
        "STR": store,
        "ADD": add,
        "MUL": multiply,
        "SUB": subtract,
        "ORR": bitwise_or,
        "AND": bitwise_and,
        "EOR": bitwise_eor,
        "MOV": assign,
        "MVN": bitwise_not,
        "LSL": shift_left,
        "LSR": shift_right,
        "CMP": compare,
        "B": branch,
        "BEQ": branch_eq,
        "BNE": branch_ne,
        "BGT": branch_gt,
        "BLT": branch_lt,
        "NOP": nop,
        "HALT": halt,
    }
    alu.get(opcode, nop)(operands, memory, regs, status)


def preprocessor(asmfile):
    with open(asmfile, "r") as fp:
        asm = sub(r";.*?\n", r"\n", fp.read())  # Strip comments
        asm = sub(r"(\w+)\s*:\s*\n", r"\1:", asm)  # Move bare labels onto line below
        asm = sub(r"\n\s*\n", r"\n", asm)  # Strip bare lines
        memory = [data.rstrip() for data in asm.splitlines()]

    labels = {}

    for address, data in enumerate(memory):
        labelpat = r"\A\s*(\w+)\s*:"
        if m := search(labelpat, data):
            labels[m.group(1)] = address
        memory[address] = sub(labelpat, "", memory[address])

    memory = [data.replace(",", " ") for data in memory]
    memory = [data.strip() for data in memory]
    memory = [
        sub(r"\b0x([\dA-Fa-f]+)\b", lambda x: str(int(x.group(1), 16)), data)
        for data in memory
    ]

    for label, address in labels.items():
        pat = f"\\b{label}\\b"
        memory = [sub(pat, str(address), data) for data in memory]

    return memory, labels


def vm(asmfile):
    numregs = 10
    status = {"EQ": False, "NE": False, "GT": False, "LT": False, "RUN": True}
    regs = {r: 0 for r in range(numregs)}
    regs["pc"] = 0

    memory, labels = preprocessor(asmfile)

    returncode = OK
    while status["RUN"]:
        try:
            cir = fetch(regs, memory)
            opcode, operands = decode(cir)
            execute(opcode, operands, memory, regs, status)
        except SyntaxError as e:
            print(f"Syntax Error: {cir}", e)
            returncode = ERROR
            break

    return regs, memory, labels, returncode


def run():
    usage = f"Usage: {argv[0]} <asm>"

    if len(argv) != 2:
        print(usage)
        quit()

    asmfile = argv[1]

    if not (path.exists(asmfile) and path.isfile(asmfile)):
        print(usage)
        quit()

    regs, memory, labels, returncode = vm(asmfile)

    if returncode == OK:
        show_regs(regs)
        print()
        show_memory(memory)
        print()
        show_labels(labels, memory)


run()
