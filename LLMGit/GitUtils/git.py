from pydantic import BaseModel, HttpUrl
from typing import List, Optional
class Files:
    path: str
class Patch:
    patch_raw_text: str
    def get_changed_files(self) -> List[Optional[Files]]:
        return []
class GitCommit(BaseModel):
    hash: str
    author: str
    email: str
    date: str
    message: str
    patch: str


class GitClient(BaseModel):
    repo_url: HttpUrl
    branchName: str
    
    def get_last_n_hash_codes(self, n: int) -> List[Optional[str]]:
        return []
    def get_last_n_commits(self, n: int) -> List[GitCommit]:
        return []
    def get_commit(self, hash: str) -> Optional[ GitCommit ]:
        return None