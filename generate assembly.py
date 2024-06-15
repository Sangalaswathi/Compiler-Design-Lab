def generate_assembly(intermediate_code):
    assembly_code = ""

    for instruction in intermediate_code:
        opcode = instruction[0]
        operands = instruction[1:]

        if opcode == "ADD":
            assembly_code += f"ADD {operands[0]}, {operands[1]}\n"
        elif opcode == "SUB":
            assembly_code += f"SUB {operands[0]}, {operands[1]}\n"
        elif opcode == "MUL":
            assembly_code += f"MUL {operands[0]}, {operands[1]}\n"
        elif opcode == "DIV":
            assembly_code += f"DIV {operands[0]}, {operands[1]}\n"
        elif opcode == "MOV":
            assembly_code += f"MOV {operands[0]}, {operands[1]}\n"
        elif opcode == "JMP":
            assembly_code += f"JMP {operands[0]}\n"
        elif opcode == "CMP":
            assembly_code += f"CMP {operands[0]}, {operands[1]}\n"
        elif opcode == "JNE":
            assembly_code += f"JNE {operands[0]}\n"
        elif opcode == "JGE":
            assembly_code += f"JGE {operands[0]}\n"
        

    return assembly_code


intermediate_code = [
    ("MOV", "R1", "10"),
    ("MOV", "R2", "5"),
    ("ADD", "R3", "R1", "R2"),
    ("SUB", "R4", "R3", "R1"),
    ("JMP", "END"),
    ("ADD", "R5", "R4", "R2"),
    ("END",)
]

assembly = generate_assembly(intermediate_code)
print(assembly)
