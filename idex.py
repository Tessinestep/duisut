import random

swaps_1inch = [
    {"fromToken": "WETH", "toToken": "DAI", "amount": 100},
    {"fromToken": "DAI", "toToken": "USDC", "amount": 100},
    {"fromToken": "USDC", "toToken": "WETH", "amount": 100},
]

random.shuffle(swaps_1inch)
