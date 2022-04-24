#####################################
# Class Definitions
#####################################

###########################
# Named
class Named:
    def __init__(self, name):
        self.__name = name.title()

    @property
    def name(self):
        return self.__name


###########################
# Register
class Register(Named):

    BITS = 32

    # TODO 7) move BITS from Static variable to instance variable, and add to constructor. Then change PC, MAR to be 8 bits; Status register to 4 bits; CIR to 17 bits keeping MBR and Registers as 32 bits

    def __init__(self, name):
        super().__init__(name)
        self.__value = 0
        self.__mask = (
            2 ** (Register.BITS + 1)
        ) - 1  # Used for a bitwise AND of an assigned value
        self.__recv_callback = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v & self.__mask
        # If the register is connected to something, call the receiving function
        if self.__recv_callback:
            self.__recv_callback(self.value)

    def connect(self, recv_callback):
        self.__recv_callback = recv_callback

    # Allow the register to receive a value from a bus
    def recv(self, v):
        self.__value = v

    def __repr__(self):
        return f"{self.name:>10} : 0x{self.value:08X}"


###########################
# Bus
class Bus(Named):

    ADDRESS = "A"
    DATA = "D"
    CONTROL = "C"
    READ = "R"
    WRITE = "W"

    # TODO 8) Add a Bit Width parameter to the bus constructor and mask any values sent along the bus

    def __init__(self, name):
        super().__init__(name)
        self.__recv_callbacks = []
        self.__value = None

    def connect(self, recv_callback):
        self.__recv_callbacks.append(recv_callback)

    def send(self, value):
        self.__value = value
        for recv in self.__recv_callbacks:
            recv(value)

    def __repr__(self):
        return f"{self.name} : {self.__value}"


###########################
# RAM
class Ram(Named):
    SIZE = 256  # Only 8 bits of DIRECT addressing

    # TODO 9) Change the SIZE to be a per-instance constant rather than a class constant, introducing it into the Ram constructor
    def __init__(self, name):
        super().__init__(name)
        self.__storage = [0] * Ram.SIZE
        self.__send_data = None
        self.__address = 0
        self.__data = 0

    # Allow the RAM to send data out on the data bus when it receives a READ command
    def connect_data(self, send_callback):
        self.__send_data = send_callback

    # To allow [] syntax for the RAM
    def __getitem__(self, a):
        if 0 <= a < Ram.SIZE:
            return self.__storage[a]
        else:
            raise Exception(f"RAM address out of range: {a}")

    # TODO 20) write the __setitem__ method and use it in the WRITE command. Perform a range check on the address

    # Load a program into internal storage
    def load(self, data):
        if len(data) < Ram.SIZE:
            for address, value in enumerate(data):
                self.__storage[address] = value
        else:
            raise Exception(f"Program too large for RAM")

    # The function called when an address is received
    def recv_address(self, a):
        self.__address = a

    # The function called when a data is received
    def recv_data(self, d):
        self.__data = d

    # The function called when a command is received on the control bus
    def recv_control(self, c):
        if c == Bus.READ:
            data = self[self.__address]
            # TODO 10) Raise exception if __send_data has not been set
            if self.__send_data:
                self.__send_data(data)
            else:
                raise Exception("RAM is not connected to the Data Bus")
        elif c == Bus.WRITE:
            # TODO 20) Use the __setitem__ overloading here to re-write as self[self.__address] = self.__data
            self.__storage[self.__address] = self.__data
        # TODO 10) Raise exception if command is not READ or WRITTE
        else:
            raise Exception(f"Unknown Command: {c}")


###########################
# CPU
class Cpu(Named):

    # Pipeline cycles
    FETCH = "F"
    DECODE = "D"
    EXECUTE = "E"
    HALTED = "H"

    # Opcode - 4 bits
    # Addressing mode - 1 bit
    # Operand(s) - 12 bits
    #     LDR Immediate Addressing: 4 bits of Rd and 8 bits of immediate
    #     LDR Direct Addressing: 4 bits of Rd and 8 bits of direct address
    #    STR Direct Addressing: 4 bits of Rd and 8 bits of direct address
    #    STR Immediate Addressing: Unused
    #    ALU Direct(Register) Addressing: 4 bits of Rd, 4 of Rm and 4 of Rn
    #    ALU Immediate Addressing: 4 bits of Rd, 4 of Rm and 4 of Immediate

    # Addressing modes
    DIRECT = 0
    IMMEDIATE = 1

    # Opcodes
    HALT = 0
    LDR = 1
    STR = 2
    ADD = 3
    CMP = 4
    BEQ = 5
    B = 6

    # Status Register Encodings for CMP and B instructions
    EQ = 1
    LT = 2
    GT = 4

    # TODO 19) Define remaining opcodes from AQA spec (BNE, MOV, SUB, LSL, LSR)

    def __init__(self, name):
        super().__init__(name)
        self.__send_control = None
        self.__state = Cpu.FETCH
        # TODO 8) Set Bit widths when making instances of registers in the constructor
        self.__pc = Register("PC")
        self.__cir = Register("CIR")
        self.__mar = Register("MAR")
        self.__mbr = Register("MBR")
        self.__registers = [Register(f"R{n}") for n in range(16)]
        self.__status = Register("Status")
        self.__ticks = 0

    def __repr__(self):
        regs = "\n".join(str(r) for r in self.__registers)
        return f"""
{self.name}
Clock Ticks: {self.__ticks}
State: {self.state}
{self.__pc}
{self.__cir}
{self.mar}
{self.mbr}
{self.__status}
{regs}"""

    @property
    def mar(self):
        return self.__mar

    @property
    def mbr(self):
        return self.__mbr

    # TODO 16) Add setters for the mar, mbr, cir and pc which set the .value of each register, and perform a type check on the value to be an integer

    @property
    def state(self):
        return self.__state

    def connect_control(self, c):
        self.__send_control = c

    def __fetch(self):
        # Copy the PC into the MAR
        self.mar.value = self.__pc.value

        # TODO 1) increment the PC
        self.__pc.value += 1

        # Send a read command on the control bus, causing the RAM to read the the result to be places in the MBR
        self.__send_control(Bus.READ)

        # TODO 2) Copy the MBR into the CIR
        self.__cir.value = self.mbr.value

        # TODO 3) Set the state to DECODE
        self.__state = Cpu.DECODE

    # TODO 17) Add  __getitem__ and __setitem__ methods for accessing the CPU registers which access the .value properties and also do a range check on the register number

    def __decode(self):
        # Break the CIR up into addressing mode, opcode and operand
        self.__addrmode = (self.__cir.value >> 12) & 0x01
        self.__opcode = (self.__cir.value >> 13) & 0xF
        self.__operand = self.__cir.value & 0xFFF
        # TODO 4) Set the state to EXECUTE
        self.__state = Cpu.EXECUTE

    def __execute(self):
        # TODO 11) If you have Python 10 installed, try using the match/case syntax for if/elif/elif statement based on the opcode

        ##################
        # Load instruction
        if self.__opcode == Cpu.LDR:
            rd = (self.__operand >> 8) & 0xF
            if self.__addrmode == Cpu.DIRECT:
                self.mar.value = self.__operand & 0xFF
                self.__send_control(Bus.READ)
                self.__registers[rd].value = self.mbr.value
            elif self.__addrmode == Cpu.IMMEDIATE:
                self.__registers[rd].value = self.__operand & 0xFF
            self.__state = Cpu.FETCH

        ##################
        # Store instruction
        elif self.__opcode == Cpu.STR:
            # TODO 12) This code for extracting rd from the operand is used in several places. Create a private function to do it to reduce repeated code
            rd = (self.__operand >> 8) & 0xF
            if self.__addrmode == Cpu.DIRECT:
                self.mar.value = self.__operand & 0xFF
                self.mbr.value = self.__registers[rd].value
                self.__send_control(Bus.WRITE)
            elif self.__addrmode == Cpu.IMMEDIATE:
                raise Exception("Cannot use immediate addressing for store")
            self.__state = Cpu.FETCH

        ##################
        # Add instruction
        elif self.__opcode == Cpu.ADD:
            # TODO 13) Implement Immediate addressing for ADD with Rn
            rd = (self.__operand >> 8) & 0xF
            rm = (self.__operand >> 4) & 0xF
            rn = (self.__operand) & 0xF
            # TODO 17) When the __getitem__ method is written, this next line should read op1 = self[rm]
            op1 = self.__registers[rm].value
            op2 = self.__registers[rn].value
            result = op1 + op2
            # TODO 17) When the __setitem__ method is written, this next line should read self[rd] = result
            self.__registers[rd].value = result
            self.__state = Cpu.FETCH

        ##################
        # Halt instruction
        elif self.__opcode == Cpu.HALT:
            self.__state = Cpu.HALTED

        # TODO 15) Implement SUB, CMP, MOV, BEQ, B, LSL, LSR

        ##################
        # Error
        else:
            raise Exception(f"Unknown opcode: {self.__opcode}")

    # Each clock tick runs F/D/E
    def clock(self):

        # TODO 5) Increment the 'ticks' private property
        self.__ticks += 1

        # TODO 6) Call the pipeline stage depending on state (use match/case if you have Python 10)
        if self.state == Cpu.FETCH:
            self.__fetch()
        elif self.state == Cpu.DECODE:
            self.__decode()
        elif self.state == Cpu.EXECUTE:
            self.__execute()

        # TODO (Hard) Use pipelining to be able to run fech, decode and execute on 3 different instructions in one clock cycle
        # Solution (remove above code and replace with this) ...
        # if self.__ticks > 2: self.__execute()
        # if self.__ticks > 1 and self.state != Cpu.HALTED: self.__decode()
        # if self.state != Cpu.HALTED: self.__fetch()


###########################
# System
# TODO Allow the System to be Named using inheritance, add the name to the repr method
class System:
    def __init__(self):
        # TODO (Extension) Create a Harvard Architecture
        # TODO (Super Extension) Create a secondary storage controller class with address-mapped control registers, and an SSD class which stores data in a file on your filesystem. Write a program to access secondary storage.
        P = Cpu("Processor")
        R = Ram("Random Access Memory")

        # TODO 8) Once Bit Widths are implemented, set the address but to 8-bits, the data bus to 32-bits and the control bus to 1-bit
        A = Bus(Bus.ADDRESS)
        D = Bus(Bus.DATA)
        C = Bus(Bus.CONTROL)

        P.mar.connect(A.send)
        P.mbr.connect(D.send)
        P.connect_control(C.send)
        R.connect_data(D.send)

        A.connect(R.recv_address)
        D.connect(R.recv_data)
        C.connect(R.recv_control)

        D.connect(P.mbr.recv)

        # Save the components in the system object
        self.__A = A
        self.__D = D
        self.__C = C
        self.__P = P
        self.__R = R

    def load(self, program):
        self.__R.load(program)

    def run(self):
        print(f"{self.__P.name} Running")
        while self.__P.state != Cpu.HALTED:
            self.__P.clock()
        print(f"{self.__P.name} Halted")

    def peek(self, addr):
        return self.__R[addr]

    def memdump(self, start, stop):
        result = []
        for addr in range(start, stop):
            result.append(f"0x{addr:<4X}: 0x{self.peek(addr):04X}")
        return "\n".join(result)

    def __repr__(self):
        return f"""
{self.__P}

Busses:
{self.__A}
{self.__D}
{self.__C}

RAM:
{self.memdump(0, 10)}"""


#####################################
# Main Program
#####################################

# TODO (Hard) Write an assembler sub-program to create the binary values from the assembly code
# TODO (Extension) Assembler needs to create program images for instruction memory and data memory separately

R0, R1, R2, X, Y, Z = 0, 1, 2, 5, 6, 7

# Assembler code for x = 2; y = 3; z = x + y
program = [
    (Cpu.LDR << 13) | (Cpu.DIRECT << 12) | (R0 << 8) | X,  # 0 : LDR r0, x (address 5)
    (Cpu.LDR << 13) | (Cpu.DIRECT << 12) | (R1 << 8) | Y,  # 1 : LDR r1, y (address 6)
    (Cpu.ADD << 13)
    | (Cpu.DIRECT << 12)
    | (R2 << 8)
    | (R1 << 4)
    | R0,  # 2 : ADD r2, r1, r0
    (Cpu.STR << 13) | (Cpu.DIRECT << 12) | (R2 << 8) | Z,  # 3 : STR r2, z (address 7)
    Cpu.HALT,  # 4 : HALT
    2,  # 5 : x = 2
    3,  # 6 : y = 3
    0,  # 7 : z = 0
]

# TODO 14) Introduce static constants for the bit shifts needed for assembling and disassembling (13, 12, 8, 4)
# TODO 13) Try changing the program to load the IMMEDIATE values of 10 and 11 into r0 and r1

if __name__ == "__main__":
    # Only runs when this program is executed, not if imported by another file
    S = System()
    S.load(program)
    S.run()
    assert S.peek(Z) == 5  # Check the program produced the expected result
    print(S)
