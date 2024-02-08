import os

from notion_utils.MyNotionDBLoader import MyNotionDBLoader
from dotenv import load_dotenv

load_dotenv()

NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
NOTION_TOKEN = os.getenv("NOTION_TOKEN")

notion = MyNotionDBLoader(
    integration_token=NOTION_TOKEN,
    database_id=NOTION_DATABASE_ID,
    verbose=True,
    metadata_filter_list=[],
    validate_missing_content=False,
    validate_missing_metadata=[],
)
docs = notion.load(query_dict={}, is_test_only=True)
