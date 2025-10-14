import pandas as pd
from pathlib import Path

def export_to_csv(conn, out: str = "jobs_export.csv", limit: int = 1000):
	df = pd.read_sql("SELECT * FROM jobs ORDER BY scraped_at DESC LIMIT ?", conn, params=(limit,))
	df.to_csv(out, index=False)
	return Path(out)