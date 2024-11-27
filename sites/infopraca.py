from url_helper import extract_offers_from_url


def ippl_title(offer):
    return offer.get("title")


def ippl_location(offer):
    return offer.get("city")


def ippl_link(offer):
    return offer.get("url")


def search_infopracapl(url):
    infopracapl = extract_offers_from_url(url)
    job_offers_ippl = []
    for offer in infopracapl:
        title = ippl_title(offer)
        location = ippl_location(offer)
        link = ippl_link(offer)
        job_offers_ippl.append([title, location, "No salary information", link])

    return job_offers_ippl
