from url_helper import extract_offers_from_url


def ppl_title(offer):
    # Extracts the title of the job offer
    return offer.find("h2", {"data-test": "offer-title"}).get_text().strip()


def ppl_location(offer):
    # Extracts the location of the job offer
    return offer.find("h4", {"data-test": "text-region"}).get_text().strip()


def ppl_salary(offer):
    # Extracts the salary of the job offer
    return offer.find("span", {"data-test": "offer-salary"})


def ppl_link(offer):
    # Extracts the URL of the job offer
    return offer.find("a", href=True).get("href")


def search_pracujpl(url):
    # Extracts job offers from the given URL
    ppl_offers = extract_offers_from_url(url)
    job_offers_ppl = []

    # Processes each job offer
    for offer in ppl_offers:
        title = ppl_title(offer)  # Gets the title of the offer
        location = ppl_location(offer)  # Gets the location of the offer
        salary = ppl_salary(offer)  # Gets the salary of the offer
        if salary is not None:
            salary = salary.get_text().strip().replace("\xa0", " ")
        else:
            salary = "No salary information"
        link = ppl_link(offer)  # Gets the URL of the offer
        # Adds the job offer to the list
        job_offers_ppl.append([title, location, salary, link])
    # Returns the list of job offers
    return job_offers_ppl
