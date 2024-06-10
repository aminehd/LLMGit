from LLMGit.GitUtils.git import GitClient, GitCommit


def test_get_last_n_commits():
    # Instantiate GitRepo
    git_client = GitClient(repo_url="https://github.com/django/django.git",branchName="main" )

    # Call the method
    commits = git_client.get_last_n_commits(1)
    mock_patch = \
        "diff --git a/example.py b/example.py\n" \
        "index abcdef0..1234567 100644\n" \
        "--- a/example.py\n" \
        "+++ b/example.py\n" \
        "@@ -1,3 +1,7 @@\n" \
        " def existing_function():\n" \
        "     print(\"This is an existing function\")\n" \
        " \n" \
        "+def new_function():\n" \
        "+    print(\"This is a new function\")\n" \
        "+\n" \
        "+def another_new_function():\n" \
        "+    print(\"This is another new function\")\n"

    # Expected results
    expected_commits = [
        GitCommit(patch='mock_patch', hash="commit_hash_1", author="Author One", email="author1@example.com", date="Date One", message="Commit message one"),
    ]

    # Assertions
    assert commits == expected_commits
    assert len(commits) == 1
    assert commits[0].patch.patch_raw_text == mock_patch
    assert commits[0].pathc.get_changed_files() == '/acme/acme'
