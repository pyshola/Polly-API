import requests
import json

def cast_vote(poll_id: int, option_id: int, token: str):
    """
    Casts a vote on a specific poll option.

    Args:
        poll_id (int): The ID of the poll to vote on.
        option_id (int): The ID of the option to vote for.
        token (str): The JWT authentication token.

    Returns:
        dict: The JSON response from the server, or None if an error occurs.
    """
    url = f"http://localhost:8000/polls/{poll_id}/vote"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "option_id": option_id
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    # This is an example of how to use the cast_vote function.
    # In a real application, you would first need to log in to get a token.
    
    # Replace with a valid poll ID, option ID, and JWT token
    example_poll_id = 1
    example_option_id = 1 
    # You would get this token from the /login endpoint
    example_jwt_token = "your_jwt_token_here" 

    print(f"Casting vote for option {example_option_id} on poll {example_poll_id}...")
    vote_response = cast_vote(example_poll_id, example_option_id, example_jwt_token)

    if vote_response:
        print("Vote cast successfully!")
        print("Response:", vote_response)
