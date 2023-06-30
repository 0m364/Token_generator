import web3

def get_total_supply(w3, address):
  abi = [
    {
      "constant": True,
      "inputs": [],
      "name": "totalSupply",
      "outputs": [{"name":"","type":"uint256"}],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    }
  ]

  contract = w3.eth.contract(address=address, abi=abi)
  total_supply = contract.functions.totalSupply().call()
  return total_supply

if __name__ == "__main__":
  w3 = web3.Web3(web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
  address = "0xYOUR_TOKEN_ADDRESS"

  total_supply = get_total_supply(w3, address)

  print(total_supply)
