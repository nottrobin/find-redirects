# Third party packages
import requests


def head_url(url):
    """
    Get the response by heading a URL and following all redirects
    """

    # Some servers refuse connections if there's no user-agent
    user_agent = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    )

    response = requests.head(
        url,
        allow_redirects=True,
        headers={'User-Agent': user_agent}
    )
    if response.status_code == 405:
        # If HEAD isn't allow, try a GET
        response = requests.get(
            url,
            allow_redirects=True,
            headers={'User-Agent': user_agent}
        )
    response.raise_for_status()

    return response


def get_redirect_url(url, permanent_only=False):
    """
    Given a URL, check if it HTTP redirects to another URL.
    Follow the chain and return the final URL. Or return None if there is no
    redirect.
    """

    redirect = False

    try:
        response = head_url(url)
    except Exception as request_error:
        return None, request_error
    else:
        final_url = response.url

        for step in response.history:
            if permanent_only and step.status_code == 302:
                final_url = step.url
            else:
                redirect = True

        if redirect:
            return final_url, None
        else:
            return None, None
