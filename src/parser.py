from bs4 import BeautifulSoup


def parse_job_card(card_html: str) -> dict:
    """Parse one Indeed-style job card without making network requests."""
    soup = BeautifulSoup(card_html, "html.parser")

    def value(selector: str) -> str | None:
        tag = soup.select_one(selector)
        return tag.get_text(" ", strip=True) if tag else None

    link = soup.select_one("a.jcs-JobTitle, a[href*='/rc/clk']")
    return {
        "title": value("h2.jobTitle"),
        "company": value("span.companyName"),
        "location": value("div.companyLocation"),
        "summary": value("div.job-snippet"),
        "salary": value("div.salary-snippet, span.salaryText"),
        "job_url": link.get("href") if link else None,
    }
