import re
from url_helper import extract_offers_from_url


def nfj_title(offer):
    # Extracts the title of the job offer
    title_nfj = offer.find("h3", {"data-cy": re.compile(r"title position")})
    return title_nfj.get_text().strip().replace("NOWA", "")


def nfj_location(offer):
    # Extracts the location of the job offer
    return offer.find("span", class_=re.compile(r"tw-text-ellipsis")).get_text().strip()


def nfj_salary(offer):
    # Extracts the salary of the job offer
    return offer.find("span", {"data-cy": re.compile(r"salary ranges")})


def nfj_link(offer):
    # Extracts the URL of the job offer
    block_name = {"data-cy": re.compile(r"title position")}
    super_weird_block = offer.find("h3", block_name).parent.parent.parent.parent
    link = super_weird_block.get("href")
    return link


def search_nofluffjobs(url):
    # Extracts job offers from the given URL
    nofluffjobs = extract_offers_from_url(url)
    job_offers_nfj = []

    # Processes each job offer
    for offer in nofluffjobs:
        title = nfj_title(offer)  # Gets the title of the offer
        location = nfj_location(offer)  # Gets the location of the offer
        salary = nfj_salary(offer)  # Gets the salary of the offer
        if salary is not None:
            salary = salary.get_text().strip().replace("\xa0", " ")
        else:
            salary = "No salary information"
        link = nfj_link(offer)  # Gets the URL of the offer
        job_offers_nfj.append(
            [title, location, salary, f"https://nofluffjobs.com{link}"]
        )
    # Returns the list of job offers
    return job_offers_nfj
