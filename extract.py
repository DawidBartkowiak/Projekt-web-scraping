from sites.nofluffjobs import search_nofluffjobs
from sites.pracujpl import search_pracujpl
from sites.infopraca import search_infopracapl

def extract_data(url):
    
    results = []
    if 'pracuj.pl' in url:
        search_pracujpl(url)
    elif 'nofluffjobs.com' in url:
        search_nofluffjobs(url)
    elif 'infopraca.pl' in url:
        search_infopracapl(url)
    return results
