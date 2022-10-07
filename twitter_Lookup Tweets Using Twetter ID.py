# This will import the Twarc2 client and expansions class from twarc library and also the json library
from twarc import Twarc2, expansions
import json

# This is where you initialize the client with your own bearer token (replace the XXXXX with your own bearer token)
client = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAAMcdhwEAAAAAPtKQyJaEJzPuNPHbCgLP8QbECas%3DrUyDuqGoVxveXSRCB7OqteQNndqXG36z2ENrbpHGUepvp6wV3X")

def main(): 
    # List of user IDs to lookup, add the ones you would like to lookup
    users = ['2244994945']
    # The user_lookup function gets the hydrated user information for specified users
    lookup = client.user_lookup(users=users)
    for page in lookup:
        result = expansions.flatten(page)
        for user in result:
            # Here we are printing the full Tweet object JSON to the console
            print(json.dumps(user))


if __name__ == "__main__":
    main()