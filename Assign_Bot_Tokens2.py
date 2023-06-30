import requests

def assign_tokens_to_bot(bot_id, token_amount):
    # Make a request to a hypothetical Ethereum API to assign tokens to bot
    api_url = 'https://api.ethereum.com/assign_tokens'

    payload = {
        'bot_id': bot_id,
        'token_amount': token_amount
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        print(f"Tokens assigned to bot {bot_id}: {token_amount}")
    except requests.exceptions.HTTPError as errh:
        print(f"Error assigning tokens to bot {bot_id}: HTTP Error - {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error assigning tokens to bot {bot_id}: Connection Error - {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Error assigning tokens to bot {bot_id}: Timeout Error - {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error assigning tokens to bot {bot_id}: {err}")

# Usage example
assign_tokens_to_bot("bot1", 100)
assign_tokens_to_bot("bot2", 50)
