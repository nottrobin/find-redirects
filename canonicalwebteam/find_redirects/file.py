# Core packages
import glob
import os
import re

# Local packages
from .url import get_redirect_url


def find_files(file_globs):
    """
    Given a list of glob patterns, find all matching files
    """

    filepaths = []

    for file_glob in file_globs:
        if os.path.isdir(file_glob):
            file_glob = os.path.join(file_glob, '**')

        for glob_item in glob.iglob(file_glob, recursive=True):
            if os.path.isfile(glob_item):
                filepaths.append(glob_item)

    return filepaths


def find_redirects(urls, logger, check_https=False, permanent_only=False):
    """
    Check all URLs in list, find those that redirect to new URLs,
    and return a mapping of old to new URLs.
    """

    redirects = {}
    failed_urls = {}

    for url in urls:
        redirect_url = None

        if check_https and url.startswith('http:'):
            redirect_url, request_error = get_redirect_url(
                url.replace('http:', 'https:'),
                permanent_only
            )

        if not redirect_url:
            redirect_url, request_error = get_redirect_url(url, permanent_only)

            if request_error:
                failed_urls[url] = str(request_error)

        if redirect_url:
            logger.log("Found redirect: {} - {}".format(url, redirect_url))
            redirects[url] = redirect_url

    return redirects, failed_urls


def find_urls_in_files(filepaths):
    """
    Search each file for URLs, and return a list of the found
    URLs, removing any duplicates
    """

    url_match = re.compile(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]'
        '|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    urls = []

    for filepath in filepaths:
        with open(filepath) as file_handle:
            urls += url_match.findall(file_handle.read())

    return sorted(list(set(urls)))


def replace_in_files(filepaths, string_mapping, logger):
    """
    For each file in the list, replace each string with a new value
    """

    for filepath in filepaths:
        logger.log("Updating {}".format(filepath))

        with open(filepath) as file_handle:
            contents = file_handle.read()

        for old_value, new_value in string_mapping.items():
            contents = contents.replace(old_value, new_value)

        with open(filepath, 'w') as file_handle:
            file_handle.write(contents)
