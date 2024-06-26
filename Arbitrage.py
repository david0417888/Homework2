def RESERVES_FROM_POOL(POOLS, TOKEN_IN, TOKEN_OUT):
    if (TOKEN_IN, TOKEN_OUT) in POOLS:
        RESERVE_IN, RESERVE_OUT = POOLS[(TOKEN_IN, TOKEN_OUT)]
    else:
        RESERVE_OUT, RESERVE_IN = POOLS[(TOKEN_OUT, TOKEN_IN)]  # Swap reserves
    
    return RESERVE_IN, RESERVE_OUT
POOLS = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
path=[]
def Find_Cycles_B(POOLS,tokens):
    cycles = []
    for token in tokens:
        if token == "tokenB":
            path = ["tokenB"]
            Find_Cycles_recursive(POOLS,token, path, cycles)
    return cycles

def AMOUNT_OUTPUT(AMOUNT_IN, RESERVE_IN, RESERVE_OUT):
    # Example implementation, replace with actual logic to calculate output AMOUNT
    AMOUNT_IN_with_fee = AMOUNT_IN * 997  # Applying fee
    numerator = AMOUNT_IN_with_fee * RESERVE_OUT
    denominator = RESERVE_IN * 1000 + AMOUNT_IN_with_fee  # Adding fee to RESERVE_IN
    GET_AMOUNT_OUT = numerator / denominator
    return GET_AMOUNT_OUT

def GET_AMOUNT_OUT(POOLS, AMOUNT_IN, path):
    if len(path) < 2:
        raise ValueError('Invalid path: Path should contain at least two tokens')

    AMOUNTS = [0] * len(path)
    AMOUNTS[0] = AMOUNT_IN

    for i in range(len(path) - 1):
        RESERVE_IN, RESERVE_OUT = RESERVES_FROM_POOL(POOLS, path[i], path[i + 1])
        AMOUNTS[i + 1] = AMOUNT_OUTPUT(AMOUNTS[i], RESERVE_IN, RESERVE_OUT)

    return AMOUNTS
def Find_Cycles_recursive(POOLS,current_token, path, cycles):
    if len(path) > 2:
        pathB=path+["tokenB"]
        AMOUNT_IN = 5
        AMOUNTS_out = GET_AMOUNT_OUT(POOLS, AMOUNT_IN, pathB)
        final_AMOUNT = AMOUNTS_out[-1]
        if final_AMOUNT > 20:
            cycles.append((pathB, final_AMOUNT))

    for token in tokens:
        if token not in path and ((current_token, token) in POOLS or (token, current_token) in POOLS):
            new_path = path + [token]
            Find_Cycles_recursive( POOLS,token, new_path, cycles)

cycles = Find_Cycles_B(POOLS, tokens)

MAX_AMOUNT = 0
MAX_cycle = None
for cycle, final_AMOUNT in cycles:
    if final_AMOUNT > MAX_AMOUNT:
        MAX_AMOUNT = final_AMOUNT
        MAX_cycle = cycle
MAX_cycle_str = '->'.join(MAX_cycle) 
print(f"path: {MAX_cycle_str}, tokenB balance={MAX_AMOUNT:.10f}")

AMOUNTS_out = GET_AMOUNT_OUT(POOLS,5, MAX_cycle)
print(AMOUNTS_out)