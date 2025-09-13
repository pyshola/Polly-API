import requests

def get_poll_results(poll_id: int):
    """
    Retrieves the results for a specific poll.

    Args:
        poll_id (int): The ID of the poll.

    Returns:
        dict: The JSON response from the server, or None if an error occurs.
    """
    url = f"http://localhost:8000/polls/{poll_id}/results"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    # This is an example of how to use the get_poll_results function.
    
    # Replace with a valid poll ID
    example_poll_id = 1

    print(f"Retrieving results for poll {example_poll_id}...")
    poll_results = get_poll_results(example_poll_id)

    if poll_results:
        print("Poll Results:")
        print(f"  Question: {poll_results.get('question')}")
        for result in poll_results.get('results', []):
            print(f"    - {result.get('text')}: {result.get('vote_count')} votes")
