#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.

    Note:
        Invalid subreddits may return a redirect to search results.
        Ensure that you are not following redirects.

    Example:
        >>> number_of_subscribers('programming')
        756024
    """
    # Reddit API endpoint for retrieving subreddit information
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Your User-Agent Name'}

    # Send the GET request to the Reddit API
    response = requests.get(api_url, headers=headers)

    # Check if the response status code is valid (e.g., 200 OK)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Invalid subreddit or other error, return 0
        return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        print(num_subscribers)
