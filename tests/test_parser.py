from pathlib import Path

from src.parser import parse_job_card


def test_parse_job_card():
    path = Path(__file__).parent / "fixtures" / "indeed_card.html"
    html = path.read_text(encoding="utf-8")
    job = parse_job_card(html)
    assert isinstance(job, dict)
    assert job["title"] == "Data Analyst"
    assert job["company"] == "TechCorp"
    assert job["location"] == "Cairo, Egypt"
    assert "Analyze data trends" in job["summary"]
