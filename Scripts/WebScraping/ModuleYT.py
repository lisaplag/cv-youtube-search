import webbrowser

from Scripts.WebScraping.VerifyRequest import get_verified_response
from Scripts.WebScraping.FilterTerms import SortBy, UploadDate, Features, Duration
from Scripts.WebScraping.PullThumbnail import get_thumbnail
from bs4 import BeautifulSoup
from re import compile


# @Description Filters hyper-links using regex pattern matching
# @argument <class 'list'>
# @return <class 'list'>
def filter_watch_only(_list):
    """Returns list of filtered youtube hyper-links"""
    result = list()
    pattern = compile('^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.?be)\/watch.+$')
    for href in _list:
        if pattern.match(href):
            result.append(href)
    return result


# @Description Lists youtube response videos from given url
# @argument <class 'string'>
# @return <class 'list'>
def import_youtube_data(_youtube_url):
    """Returns list of urls from url response"""
    result = list()
    response = get_verified_response(_youtube_url)  # Get server response from url request
    soup = BeautifulSoup(response.data, 'html.parser')
    for vid in soup.findAll('a', attrs={'class': 'yt-uix-tile-link'}):  # Find all <a> tags on page
        result.append('https://www.youtube.com' + vid['href'])  # Extracting web links using 'href' property
    return filter_watch_only(result)


# @Description Concatenates Enum filter values to a valid string
# @argument <class 'Enum'>, ...
# @return <class 'string'>
def filter_search_string(_search_term, _filter=list()):
    # TODO: '+recipe' For a forced recipe video
    result = f'{_search_term} +recipe'
    for term in _filter:
        if term != '':
            result += f', {term}'
    return result


# @Description Higher order function to scrape and store data
# @argument <class 'string'> and <class 'string'>
# @return <class 'list'>
def search_and_store(_search_term, _filename, _sortby_filter='', _uploadtime_filter='', _duration_filter='', _feature_filter=list()):
    """Returns list of search results while storing them in json"""
    print('Scraping Youtube data')

    filter_term = filter_search_string(_search_term, [_uploadtime_filter, _duration_filter] + _feature_filter)  # Format filter terms
    formatted_search_term = filter_term.replace("+", "%2B").replace(",", "%2C").replace(" ", "+")  # Format search term with pluses, commas, spaces
    print(f'Using filter search term: {formatted_search_term}')

    youtube_url = f'https://www.youtube.com/results?{_sortby_filter}search_query={formatted_search_term}'
    print(youtube_url)
    return import_youtube_data(youtube_url)


if __name__ == '__main__':
    _list = search_and_store('banana', 'unused', SortBy.ViewCount.value, UploadDate.ThisYear.value, Duration.Short.value, [Features.Subtitles.value])
    print('--- Search function ---')
    for link in _list:
        print(f'Video: {link}')
        print(f'Thumbnail: {get_thumbnail(link)}')
        # webbrowser.open(get_thumbnail(link))
    print(len(_list))
