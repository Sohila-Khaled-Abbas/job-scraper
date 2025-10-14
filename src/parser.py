from typing import Optional

def parse_job_card(card_html: str) -> dict:
    """
    Parse one job card HTML and return a dict. Keep this function pure and unit-testable.
    The HTML structure for Indeed may change; update selectors if tests fail.
    """
    soup = BeautifulSoup(card_html, "html.parser")
    # selectors used in main scraper (tweak if site changed)
title_tag = soup.select_one("h2.jobTitle")
title = title_tag.get_text(strip=True) if title_tag else None


company_tag = soup.select_one("span.companyName")
company = company_tag.get_text(strip=True) if company_tag else None


location_tag = soup.select_one("div.companyLocation")
location = location_tag.get_text(strip=True) if location_tag else None


summary_tag = soup.select_one("div.job-snippet")
summary = summary_tag.get_text(separator=" ", strip=True) if summary_tag else None


salary_tag = soup.select_one("div.salary-snippet") or soup.select_one("span.salaryText")
salary = salary_tag.get_text(strip=True) if salary_tag else None


link_tag = soup.select_one("a.jcs-JobTitle") or soup.select_one("a[href*='/rc/clk']")
job_url = link_tag.get("href") if link_tag else None


return {
"title": title,
"company": company,
"location": location,
"summary": summary,
"salary": salary,
"job_url": job_url,
}