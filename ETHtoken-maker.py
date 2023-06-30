import web3

def generate_token(web3, address, symbol, decimals):
  contract = web3.eth.contract(
    abi="[{"
    "constant": True,
    "inputs": [],
    "name": "totalSupply",
    "outputs": [{"type": "uint256", "name": "totalSupply"}],
    "payable": False,
    "stateMutability": "view",
    "type": "function"}],
    address=address,
  )

  total_supply = contract.functions.totalSupply().call()
  token = contract.functions.createToken(symbol, decimals, total_supply).call()

  return token

if __name__ == "__main__":
  web3 = web3.Web3(web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
  address = "0xYOUR_TOKEN_ADDRESS"
  symbol = "YOUR_TOKEN_SYMBOL"
  decimals = 18

  token = generate_token(web3, address, symbol, decimals)

  print(token)
