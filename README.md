# Release Notes Generator 🚀

### Scripts to automatically create tag + release notes: <br>

* [Create Tag & Release](https://github.com/seljabali/release-notes-generator/blob/main/.github/workflows/create-tag-and-release.yml)
  * Creates release notes via [Python script](https://github.com/seljabali/release-notes-generator/blob/main/.github/scripts/generate_release_notes.py).
  * Pro: most custimizable approach.
  * Con: rather brittle & needs altering when copying to new repo.

* [Create Tag & Github Release](https://github.com/seljabali/release-notes-generator/blob/main/.github/workflows/create-new-github-release.yml)
  * Creates release notes via Github's [Release.yml](https://github.com/seljabali/release-notes-generator/blob/main/.github/release.yml). See [documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes).
  * Pro: Most reusable approach.
  * Con: does not capture commit changes, only PR changes. Hard to customize.

--------------

Tags are created in `yyyy-week-patch` format.
- Year: 2024
- Week in year: 1-52
- Patch: 0, 1, 2, etc. Every release increments patch count by 1.

Example:
* [2024.14.01](https://github.com/seljabali/release-notes-generator/releases/tag/2024.14.01)

----------------

Library dependencies:
* [Action GH-Release](https://github.com/softprops/action-gh-release)

