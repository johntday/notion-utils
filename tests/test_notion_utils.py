import os

from notion_utils.MyNotionDBLoader import MyNotionDBLoader
from dotenv import load_dotenv

load_dotenv()

NOTION_DATABASE_ID = "47f5bc1a6b6242b68d048a199a17b19a" # movies
notion_token = os.getenv("NOTION_TOKEN")


notion = MyNotionDBLoader(
    integration_token=notion_token,
    database_id=NOTION_DATABASE_ID,
    verbose=True,
    # metadata_filter_list = ['id', 'title', 'tags', 'version', 'source id', 'published', 'source', 'myid'],
    metadata_filter_list=['title', 'plot'],
    validate_missing_content=False,
    validate_missing_metadata=['title', 'genres'],
)
docs = notion.load({})
