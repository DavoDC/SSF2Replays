# SSF2Replays - Claude Notes

## Repo layout

- `commitNewReplays.sh` - main entry point; run from repo root
- `Helper_Scripts/commitToGit.sh` - git workflow (fetch, check, commit, push)
- `Helper_Scripts/update_readme.py` - counts .ssfrec files, updates README replay count

## Two local clones

- `C:\Users\David\SSF2Replays` - e15 working clone; run scripts from here
- `C:\Users\David\GitHubRepos\SSF2Replays` - workspace-adjacent; edit and commit here, then push, then `git pull` on the other clone

## OSTYPE on Windows

Old Git for Windows (Cygwin runtime): `$OSTYPE=cygwin`
Modern Git for Windows (MSYS2 runtime): `$OSTYPE=msys`

`commitToGit.sh` handles both. If a new Windows machine is added, check `echo $OSTYPE` and update the elif condition if needed.
