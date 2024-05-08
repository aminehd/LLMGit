from LLMGit.GitUtils import git

def test_evaluate_initialization():
    repo = git.GitRepo(name='dummyname', url='dummy_url')
    assert repo.name == 'dummyname'