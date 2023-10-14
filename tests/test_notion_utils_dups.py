import os
import pprint

from notion_utils.MyNotionDBLoader import MyNotionDBLoader
from dotenv import load_dotenv
load_dotenv()

NOTION_MOVIE_DATABASE_ID1 = os.getenv("NOTION_MOVIE_DATABASE_ID1")
NOTION_SERIES_DATABASE_ID2 = os.getenv("NOTION_SERIES_DATABASE_ID2")
databases = [
    ('movies', NOTION_MOVIE_DATABASE_ID1, "id"),
    ('series', NOTION_SERIES_DATABASE_ID2, "id"),
]
notion_token = os.getenv("NOTION_TOKEN")

# loop over all databases
for db_name, db_id, uniq_col_name in databases:
    print(f"Checking duplicates for database: {db_name} on column: {uniq_col_name}")
    notion = MyNotionDBLoader(
        integration_token=notion_token,
        database_id=db_id,
        verbose=True,
    )
    dups = notion.duplicates(query_dict={})
    pprint.pprint(dups)
    print()
    print()
