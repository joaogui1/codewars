def simple_assembler(code):
    ptr = 0
    registers = dict()
    get_value = lambda y: registers[y] if y.isalpha() else int(y)
    while ptr < len(code):
        command = code[ptr]
        match command.split():
            case [op, reg]:
                if op == "inc": registers[reg] += 1
                else: registers[reg] -= 1
            case ["mov", reg, y]:
                registers[reg] = get_value(y)
            case ["jnz", x, y]:
                x_val, y_val = get_value(x), get_value(y)
                if x_val != 0: ptr += (y_val - 1)
        ptr += 1

    return registers

simple_assembler('''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''.splitlines())