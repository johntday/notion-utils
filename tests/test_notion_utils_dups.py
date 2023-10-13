import os
import pprint

from notion_utils.MyNotionDBLoader import MyNotionDBLoader
from dotenv import load_dotenv
load_dotenv()

databases = [
    ('movies', "47f5bc1a6b6242b68d048a199a17b19a", "id"),
    ('series', "bb5dac327c664f8ea6a7ce4b5e3bc1a0", "id"),
]
notion_token = os.getenv("NOTION_TOKEN")

# loop over all databases
for db_name, db_id, uniq_col_name in databases:
    print(f"Checking duplicates for database: {db_name}")
    notion = MyNotionDBLoader(integration_token=notion_token, database_id=db_id, verbose=True)
    dups = notion.duplicates()
    pprint.pprint(dups)
    print()
    print()
