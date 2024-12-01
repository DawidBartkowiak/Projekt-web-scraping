from sites.nofluffjobs import search_nofluffjobs
from sites.pracujpl import search_pracujpl
from sites.infopraca import search_infopracapl


def extract_data(url):
    # Checks if the URL is from 'pracuj.pl' and extracts job offers
    if "pracuj.pl" in url:
        return search_pracujpl(url)
    # Checks if the URL is from 'nofluffjobs.com' and extracts job offers
    elif "nofluffjobs.com" in url:
        return search_nofluffjobs(url)
    # Checks if the URL is from 'infopraca.pl' and extracts job offers
    elif "infopraca.pl" in url:
        return search_infopracapl(url)
    # Returns an empty list if the URL does not match any known sites
    return []
