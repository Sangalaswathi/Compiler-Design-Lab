def first(grammar, symbol, first_sets):
    if symbol not in grammar:  # Terminal symbol
        return {symbol}
    if symbol in first_sets:  # Already computed First set
        return first_sets[symbol]

    first_set = set()
    for production in grammar[symbol]:
        if production == 'ε':  # If the production is epsilon
            first_set.add('ε')
        else:
            for char in production:
                first_char_set = first(grammar, char, first_sets)
                first_set.update(first_char_set - {'ε'})
                if 'ε' not in first_char_set:
                    break
            else:
                first_set.add('ε')
    first_sets[symbol] = first_set  # Memoize the result
    return first_set


def follow(grammar, symbol, start_symbol, first_sets, follow_sets):
    if symbol not in follow_sets:  # Initialize Follow set
        follow_sets[symbol] = set()
    if symbol == start_symbol:
        follow_sets[symbol].add('$')  # End of input marker

    for nt, productions in grammar.items():
        for production in productions:
            for index, char in enumerate(production):
                if char == symbol:
                    next_symbols = production[index + 1:]
                    if next_symbols:
                        first_of_next = set()
                        for next_symbol in next_symbols:
                            first_of_next.update(first(grammar, next_symbol, first_sets))
                            if 'ε' not in first(grammar, next_symbol, first_sets):
                                break
                        follow_sets[symbol].update(first_of_next - {'ε'})
                        if 'ε' in first_of_next:
                            follow_sets[symbol].update(follow(grammar, nt, start_symbol, first_sets, follow_sets))
                    else:
                        if nt != symbol:
                            follow_sets[symbol].update(follow(grammar, nt, start_symbol, first_sets, follow_sets))
    return follow_sets[symbol]


example_grammar = {
    'bexp': ['bexpr', 'bexpr or bterm', 'bterm'],
    'bterm': ['bterm and bfactor', 'bfactor'],
    'bfactor': ['not bfactor', '(bexpr)', 'true', 'false']
}

first_sets = {}
for nt in example_grammar:
    first(grammar=example_grammar, symbol=nt, first_sets=first_sets)

follow_sets = {}
for nt in example_grammar:
    follow(grammar=example_grammar, symbol=nt, start_symbol='bexp', first_sets=first_sets, follow_sets=follow_sets)

print("First Sets:")
for nt, f_set in first_sets.items():
    print(f"First({nt}) = {f_set}")

print("\nFollow Sets:")
for nt, f_set in follow_sets.items():
    print(f"Follow({nt}) = {f_set}")

# construct_parsing_table(grammar, first_sets, follow_sets)

def construct_parsing_table(grammar, first_sets, follow_sets):
    parsing_table = {}
    for non_terminal, productions in grammar.items():
        for production in productions:
            first_of_production = first(grammar, production[0], first_sets)
            for terminal in first_of_production:
                if terminal != 'ε':
                    parsing_table[(non_terminal, terminal)] = production
            if 'ε' in first_of_production:
                for terminal in grammar, first_sets, follow_setsfollow_sets[non_terminal]:
                    parsing_table[(non_terminal, terminal)] = production
        if 'ε' in first_sets[non_terminal]:
            for terminal in follow_sets[non_terminal]:
                if (non_terminal, terminal) not in parsing_table:
                    parsing_table[(non_terminal, terminal)] = 'ε'
    return parsing_table

parsing_table = construct_parsing_table(example_grammar, first_sets, follow_sets)

print("\nParsing Table:")
for key, value in parsing_table.items():
    print(f"Parsing Table[{key}] = {value}")
