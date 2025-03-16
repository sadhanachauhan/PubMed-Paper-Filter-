import requests
import pandas as pd
import argparse
from typing import List, Dict, Optional

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

def fetch_papers(query: str) -> List[Dict]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 1000
    }
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def get_paper_details(pubmed_id: str) -> Optional[Dict]:
    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "json"
    }
    response = requests.get(details_url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("result", {}).get(pubmed_id, {})

def is_non_academic(author: Dict) -> bool:
    affiliations = author.get("affiliation", "").lower()
    return "university" not in affiliations and "lab" not in affiliations

def main():
    query="cancer AND 2023"
    file = " output.csv"
    
    

    papers = fetch_papers(query)
    results = []

    for pubmed_id in papers:
        details = get_paper_details(pubmed_id)
        if not details:
            continue

        non_academic_authors = []
        company_affiliations = set()
        corresponding_email = ""

        for author in details.get("authors", []):
            if is_non_academic(author):
                non_academic_authors.append(author.get("name", ""))
                affiliations = author.get("affiliation", "").split(";")
                for aff in affiliations:
                    if "pharma" in aff.lower() or "biotech" in aff.lower():
                        company_affiliations.add(aff.strip())

            if author.get("corresponding", "N") == "Y":
                corresponding_email = author.get("email", "")

        if non_academic_authors:
            results.append({
                "PubmedID": pubmed_id,
                "Title": details.get("title", ""),
                "Publication Date": details.get("pubdate", ""),
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": corresponding_email
            })

    df = pd.DataFrame(results)
    if file:
        df.to_csv(file, index=False)
    else:
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()