# LLMGit
Use llm to talk to git


### build & run tests
from the root directory 
run 
```
.devcontainer/post_create.sh
poetry install
poetry shell
poetry run pytest --disable-warnings
```

### install new packages
```
poetry add pack
git add poetry.lock pyproject.toml && git commit "installed new pkg" 
git push origin
```