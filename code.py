# ASSEMBLER ERROR DETECTOR 

import difflib

# OPTAB (8085 Instruction Set)
OPTAB = {
    "MOV": "Data Transfer", "MVI": "Immediate Data Transfer",
    "LXI": "Load Register Pair Immediate", "LDA": "Load Accumulator Direct",
    "STA": "Store Accumulator Direct", "LHLD": "Load HL Direct",
    "SHLD": "Store HL Direct", "LDAX": "Load Accumulator Indirect",
    "STAX": "Store Accumulator Indirect", "XCHG": "Exchange Registers",

    "ADD": "Add", "ADI": "Add Immediate", "ADC": "Add with Carry",
    "ACI": "Add Immediate with Carry", "SUB": "Subtract",
    "SUI": "Subtract Immediate", "SBB": "Subtract with Borrow",
    "SBI": "Subtract Immediate with Borrow", "INR": "Increment",
    "DCR": "Decrement", "INX": "Increment Register Pair",
    "DCX": "Decrement Register Pair", "DAD": "Double Add",

    "ANA": "AND", "ANI": "AND Immediate", "ORA": "OR",
    "ORI": "OR Immediate", "XRA": "XOR", "XRI": "XOR Immediate",
    "CMA": "Complement Accumulator", "CMC": "Complement Carry",
    "STC": "Set Carry",

    "JMP": "Jump", "JZ": "Jump if Zero", "JNZ": "Jump if Not Zero",
    "JC": "Jump if Carry", "JNC": "Jump if No Carry",
    "JP": "Jump if Positive", "JM": "Jump if Minus",

    "CALL": "Call Subroutine", "CZ": "Call if Zero",
    "CNZ": "Call if Not Zero",

    "RET": "Return", "RZ": "Return if Zero",
    "RNZ": "Return if Not Zero",

    "PUSH": "Push Stack", "POP": "Pop Stack",

    "RLC": "Rotate Left", "RRC": "Rotate Right",
    "RAL": "Rotate Left through Carry",
    "RAR": "Rotate Right through Carry",

    "IN": "Input", "OUT": "Output",

    "NOP": "No Operation", "HLT": "Halt",
    "EI": "Enable Interrupt", "DI": "Disable Interrupt"
}

# Registers
REGISTERS = ["A", "B", "C", "D", "E", "H", "L", "M"]

# Tables
SYMTAB = {}
errors = []

# TOKENIZER
def tokenize(line):
    tokens = []
    words = line.strip().split()

    if not words:
        return tokens

    # Label
    if ":" in words[0]:
        tokens.append(("LABEL", words[0].replace(":", "")))
        words = words[1:]

    # Opcode
    if len(words) > 0:
        tokens.append(("OPCODE", words[0].upper()))

    # Operands
    if len(words) > 1:
        operand_str = " ".join(words[1:])
        operands = operand_str.split(",")

        for op in operands:
            op = op.strip().upper()
            if op != "":
                tokens.append(("OPERAND", op))

    return tokens

# Suggestion Function
def get_suggestion(opcode):
    match = difflib.get_close_matches(opcode, OPTAB.keys(), n=1, cutoff=0.6)
    return match[0] if match else None

# Read Input File
filename = "input.asm"

with open(filename, "r") as file:
    lines = file.readlines()

# Display Input
print("\nINPUT PROGRAM")
print("--------------------------")
for i, l in enumerate(lines, 1):
    print(f"{i}: {l.strip()}")

print("\nANALYSIS STARTED...\n")

# Process Lines
for line_no, line in enumerate(lines, 1):

    tokens = tokenize(line)

    label = None
    opcode = None
    operands = []

    for t_type, value in tokens:
        if t_type == "LABEL":
            label = value
        elif t_type == "OPCODE":
            opcode = value
        elif t_type == "OPERAND":
            operands.append(value)

    line_error = False

    print(f"\nLine {line_no}: {line.strip()}")

    # LABEL CHECK
    if label:
        if label in SYMTAB:
            print(f"ERROR: Duplicate Symbol '{label}'")
            errors.append(f"Line {line_no}: Duplicate Symbol '{label}'")
            line_error = True
        else:
            SYMTAB[label] = True
            print(f"Label '{label}' added")

    # OPCODE CHECK
    if opcode:
        if opcode not in OPTAB:
            suggestion = get_suggestion(opcode)

            if suggestion:
                print(f"ERROR: Invalid Opcode '{opcode}' -> Suggestion: '{suggestion}' ({OPTAB[suggestion]})")
                errors.append(f"Line {line_no}: Invalid Opcode '{opcode}' -> Suggestion '{suggestion}'")
            else:
                print(f"ERROR: Invalid Opcode '{opcode}'")
                errors.append(f"Line {line_no}: Invalid Opcode '{opcode}'")

            line_error = True
        else:
            print(f"Opcode '{opcode}' is VALID -> {OPTAB[opcode]}")

    # OPERAND CHECK
    for op in operands:
        if op not in REGISTERS:
            if not op.endswith("H") and not op.isdigit():
                if op not in SYMTAB:
                    print(f"ERROR: Undefined Symbol '{op}'")
                    errors.append(f"Line {line_no}: Undefined Symbol '{op}'")
                    line_error = True

    # EXECUTION STATUS
    if line_error:
        print("Line NOT executed due to errors")
    else:
        print("Line executed successfully")

# FINAL REPORT
print("\n\nFINAL ERROR REPORT")
print("--------------------------")

if not errors:
    print("No Errors Found")
else:
    for err in errors:
        print("ERROR:", err)

# SYMBOL TABLE
print("\nSYMBOL TABLE")
print("--------------------------")
for sym in SYMTAB:
    print(sym)