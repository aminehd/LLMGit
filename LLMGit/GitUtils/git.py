from pydantic import BaseModel

class GitRepo(BaseModel):
    name: str
    url: str

    def get_commit(self, commit: str) -> str:
        return commit 