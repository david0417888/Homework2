def TRADE(liquidity, AMOUNT, m1, m2):
    ##print(AMOUNT, m1, m2)
    AMOUNT_m1, AMOUNT_m2 = liquidity[m1][m2]
    AMOUNT_am2 = AMOUNT_m1*AMOUNT_m2/(AMOUNT_m1+AMOUNT)
    liquidity[m2][m1]= (AMOUNT_am2, AMOUNT_m1+AMOUNT)
    liquidity[m1][m2]= (AMOUNT_m1+AMOUNT, AMOUNT_am2)
    AMOUNT = AMOUNT_m2-AMOUNT_am2
    return AMOUNT

def aRBITRAGE(liquidity, AMOUNT, BASE_TOKEN, m1, m2, m3):
    ##print(f"input:{AMOUNT}")
    AMOUNT = TRADE(liquidity, AMOUNT, BASE_TOKEN, m1)
    ##print(f"m1:{AMOUNT}")
    AMOUNT = TRADE(liquidity, AMOUNT, m1, m2)
    ##print(f"m2:{AMOUNT}")
    if m3 == -1:
        AMOUNT = TRADE(liquidity, AMOUNT, m2, BASE_TOKEN)
        ##print(f"output:{AMOUNT}")
        return AMOUNT
    AMOUNT = TRADE(liquidity, AMOUNT, m2, m3)
    ##print(f"m3:{AMOUNT}")
    AMOUNT = TRADE(liquidity, AMOUNT, m3, BASE_TOKEN)
    ##print(f"output:{AMOUNT}")
    return AMOUNT


def ARBITRAGE(Graph, start):
    # Initialize liquidity pool
    AMOUNT_In = 5
    tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
    liquidity = [[() for _ in range(len(tokens))] for _ in range(len(tokens))]
    BASE_TOKEN = tokens.index(start)
    # Fill the 2D array with the tuples from the liquidity dictionary
    for token1, token2, (a_1, a_2) in Graph:
        liquidity[tokens.index(token1)][tokens.index(token2)] = (a_1, a_2)
        liquidity[tokens.index(token2)][tokens.index(token1)] = (a_2, a_1)
    # Relax edges repeatedly
    while(AMOUNT_In<20.5):
        result = checkARBITRAGE(liquidity, tokens, BASE_TOKEN)
        if result == (-1, -1):
            print("HAHAFAILURE")
            return AMOUNT_In, path
        if len(result)==4:
            m1, m2, m3, AMOUNT = result
            ##print(m1,m2,m3,f"AMOUNTIn={AMOUNT}")
            path.append([m1,m2,m3,AMOUNT]) 
            AMOUNT_In = AMOUNT_In- AMOUNT 
            ##print(f"AMOUNTIn={AMOUNT}")
            AMOUNT = aRBITRAGE(liquidity, AMOUNT, BASE_TOKEN, m1, m2, m3)
            AMOUNT_In += AMOUNT
        if len(result)==3:
            m1, m2, AMOUNT = result
            path.append([m1,m2,AMOUNT])
            ##print(m1,m2,f"AMOUNTIn={AMOUNT}") 
            AMOUNT = min(AMOUNT, AMOUNT_In)
            AMOUNT_In -= AMOUNT
            AMOUNT = aRBITRAGE(liquidity, AMOUNT, BASE_TOKEN, m1, m2, -1)
            AMOUNT_In += AMOUNT
    return AMOUNT_In, path
    
def checkARBITRAGE(liquidity, tokens, BASE_TOKEN):
    for i in range(len(tokens) - 1):
        if i == BASE_TOKEN:
            continue
        for j in range(len(tokens) - 1):
            if j == i or j == BASE_TOKEN:
                continue
            for k in range(len(tokens) - 1):
                if k == i or k ==j or k ==BASE_TOKEN:
                    continue
                R0, R1 = liquidity[BASE_TOKEN][i]
                R_1, R2 = liquidity[i][j]
                R_2, R3 = liquidity[j][k]
                R_3, R_0 = liquidity[k][BASE_TOKEN]
                M0 = R0*R_1/(R_1+R1*0.997)
                m2 = 0.997*R1*R2/(R_1+R1*0.997)
                M_2 = R2*R3/(R_3+R3*0.997)
                M_0 = 0.997*R3*R_0/(R_3+R3*0.997)
                E_BEFORE = M0*M_2/(m2+M_2*0.997)
                E_AFTER = 0.997*m2*M_0/(m2+M_2*0.997)
                AMOUNT = (E_BEFORE*E_AFTER*0.997)**0.5-E_BEFORE
                if E_AFTER>E_BEFORE and AMOUNT >1:
                    return (i,j,k,AMOUNT)
    for i in range(len(tokens) - 1):
        if i == BASE_TOKEN:
            continue
        for j in range(len(tokens) - 1):
            if j == i or j == BASE_TOKEN:
                continue
            R0, R1 = liquidity[BASE_TOKEN][i]
            R_1, R2 = liquidity[i][j]
            R_2, R_0 = liquidity[j][BASE_TOKEN]
            M0 = R0*R_1/(R_1+R1*0.997)
            m2 = 0.997*R1*R2/(R_1+R1*0.997)
            E_BEFORE = M0*R_2/(m2+R_2*0.997)
            E_AFTER = 0.997*m2*R_0/(m2+R_2*0.997)
            AMOUNT = (E_BEFORE*E_AFTER*0.997)**0.5-E_BEFORE
            if E_AFTER>E_BEFORE and AMOUNT >1:
                return (i,j,AMOUNT)
    return (-1,-1)

liquidity = {
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
# Construct the Graph from the liquidity dictionary
Graph = [(token1, token2, liquidity[(token1, token2)]) for (token1, token2) in liquidity]
# Find the profitable path starting from tokenB
result,path = ARBITRAGE(Graph, "tokenB")
for i in range(len(path)):
    print("path: tokenB->",end=" ")
    for j in range(len(path[i])-1):
        print(tokens[path[i][j]], end=" ")
        print("->", end=" ")
print(f"tokenB, tokenB balance={result}")