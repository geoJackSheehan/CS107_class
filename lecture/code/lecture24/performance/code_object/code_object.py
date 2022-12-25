#!/usr/bin/env python3
import dis

a = 1
b = 2

# source to be compiled into a code object
source = 'a + 1'
# source = 'a + b'

# compile code object
co = compile(source, '<string>', mode='eval')

# disassembly columns are:
# line_number   byte_offset   instruction_name   argument_value
dis.dis(co)

# names and constants
print(f'names:               {co.co_names}')
print(f'constants:           {co.co_consts}')

# opcodes and opargs in binary
print(f'raw binary bytecode: {co.co_code}')
h = co.co_code.hex()
inst_code = " ".join([h[i:i + 4] for i in range(0, len(h), 4)]).split()
print(f'hex representation:  {" ".join(inst_code)}')

for code in inst_code:
    opcode = f'0x{code[0:2]}'
    oparg = f'0x{code[2:4]}'
    print(f'opname lookup:  {opcode} -> {dis.opname[int(opcode, 16)]}')
