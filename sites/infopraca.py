from url_helper import extract_offers_from_url


def ippl_title(offer):
    # Returns the title of the job offer
    return offer.get("title")


def ippl_location(offer):
    # Returns the location of the job offer
    return offer.get("city")


def ippl_link(offer):
    # Returns the URL of the job offer
    return offer.get("url")


def search_infopracapl(url):
    # Extracts job offers from the given URL
    infopracapl = extract_offers_from_url(url)

    # Processes each job offer
    job_offers_ippl = []
    for offer in infopracapl:
        title = ippl_title(offer)
        location = ippl_location(offer)
        link = ippl_link(offer)
        # Adds the job offer to the list with default salary information
        job_offers_ippl.append([title, location, "No salary information", link])
    # Returns the list of job offers
    return job_offers_ippl
