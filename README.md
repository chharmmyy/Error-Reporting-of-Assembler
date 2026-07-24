# Design an Error Reporting Assembler

## Project Overview

This project is a Python-based Error Reporting Assembler that analyzes 8085 assembly language programs and detects common programming errors before execution.

The assembler performs:

- Tokenization
- Opcode validation
- Operand validation
- Label validation
- Duplicate symbol detection
- Undefined symbol detection
- Opcode suggestions for misspelled instructions
- Symbol Table generation
- Final Error Report generation

---

## Features

✅ Tokenizes assembly instructions

✅ Detects invalid opcodes

✅ Suggests nearest valid opcode

✅ Detects duplicate labels

✅ Detects undefined symbols

✅ Generates Symbol Table

✅ Generates Final Error Report

---

## Project Workflow

Input Assembly Program
        ↓
Tokenization
        ↓
Validation
(Label, Opcode, Operand)
        ↓
Error Logging
        ↓
Final Error Report
&
Symbol Table

---

## Technologies Used

- Python 3
- difflib Library
- 8085 Assembly Language

---

## Project Structure

```
code.py
input.asm
workflow.txt
README.md
requirements.txt
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/Error-Reporting-Assembler.git
```

Move into the project folder

```bash
cd Error-Reporting-Assembler
```

Run

```bash
python code.py
```

---

## Sample Errors Detected

- Invalid Opcode
- Duplicate Symbol
- Undefined Symbol
- Misspelled Opcode Suggestion

---

## Author

Your Name
