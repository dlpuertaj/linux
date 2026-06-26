# Fix Log

## 2026-05-14 — git push failing (GitHub HTTPS auth)

**Symptom:** `git push` fails with auth errors.

**Root cause:** `gh auth setup-git` had not been run, so git had no credential helper for HTTPS remotes.

**Fix:**
```bash
gh auth setup-git
```

**Notes:**
- Repo uses HTTPS remotes (`https://github.com/dlpuertaj/linux.git`), not SSH.
- SSH key troubleshooting is irrelevant for this setup.
- Only needs to be run once per machine; persists across sessions.
