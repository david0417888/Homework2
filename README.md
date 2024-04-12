# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.1298889441
[5, 5.655321988655322, 2.4587813170979333, 5.0889272933015155, 20.129888944077443]
## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.
The slippage means the difference between trade price and expected price. The Uniswap V2 address this issue by using the costant product formula. For example, in the traditional market, if we want to execute large trade, due to insufficient sell orders in the market, we must execute the order gradually. However, in this process, the price will increase, which make us pay higher price to execute the order. If we use Uniswap to address the problem, we find that even we execute the order gradually, we pay the same price eventually. It is because Uniswap V2 follow the constant formula: x'*y'=k, if x' is same, y' is same too regardless of the process.

> Solution

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
I think having very small liquidity positions could lead to inefficient use of resources within the Uniswap ecosystem. It's more efficient to have liquidity providers contribute a minimum amount of liquidity, ensuring that the liquidity pool remains sufficiently capitalized to support trading activities.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
The intention behind this specific formula is to maintain the stability and efficiency of the Uniswap liquidity pool. By utilizing this formula, Uniswap aims to prevent any manipulation or imbalance in the liquidity pool, thus ensuring a fair and efficient trading environment for users. This approach helps to prevent large traders from exploiting the system and helps to maintain the overall integrity of the Uniswap protocol.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
A sandwich attack is a type of front-running attack that occurs in decentralized exchanges (DEXs) like Uniswap and other automated market makers (AMMs). In a sandwich attack, an attacker exploits the predictability of blockchain transactions to manipulate the price of a token in their favor.The impact may cause token's price slippage, meaning you may end up paying a higher price for the tokens you're buying or receiving a lower price for the tokens you're selling. This can result in less favorable exchange rates and reduced profitability for your trade.

