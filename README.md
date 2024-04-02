# Release Notes Generator 🚀

### Scripts to automatically create tag + release notes based on changes from latest previous release. <br>

* [Create Tag & Release](https://github.com/seljabali/release-notes-generator/blob/main/.github/workflows/create-tag-and-release.yml)
  * Creates release notes via [Python script](https://github.com/seljabali/release-notes-generator/blob/main/.github/scripts/generate_release_notes.py).

* [Create Tag & Fancy Release](https://github.com/seljabali/release-notes-generator/blob/main/.github/workflows/create-new-fancy-release.yml)
  * Creates release notes via Github's [Release.yml](https://github.com/seljabali/release-notes-generator/blob/main/.github/release.yml).
  * Con is that it does not capture commit changes, only PR changes.
