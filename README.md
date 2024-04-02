# Release Notes Generator 🚀

### Scripts to automatically create tag + release notes. <br>

* [Create Tag & Release](https://github.com/seljabali/release-notes-generator/blob/main/.github/workflows/create-tag-and-release.yml)
  * Creates release notes via [Python script](https://github.com/seljabali/release-notes-generator/blob/main/.github/scripts/generate_release_notes.py).
  * Most custimizable approach.
  * Con is that it's rather brittle & needs altering when copying to new repo.

* [Create Tag & Github Release](https://github.com/seljabali/release-notes-generator/blob/main/.github/workflows/create-new-github-release.yml)
  * Creates release notes via Github's [Release.yml](https://github.com/seljabali/release-notes-generator/blob/main/.github/release.yml).
  * Most reusable approach..
  * Con is that it does not capture commit changes, only PR changes.

--------------

Tags are created in `yyyy-week-patch` format.
- Year: 2024
- Week in year: 1-52
- Patch: 0, 1, 2, etc. Every release increments patch count by 1.

Example:
* https://github.com/seljabali/release-notes-generator/releases/tag/2024.14.01

----------------

Library dependencies:
* [Action GH-Release](https://github.com/softprops/action-gh-release)

