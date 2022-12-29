# KOHilites

A lightweight command line tool to extract and save highlights and notes made on [KOReader](https://github.com/koreader/koreader).

KOHilites takes `metadata.*.lua` files, extracts the content of each highlight or note, and saves them as formatted markdown files.

## Installation

Install this package from PyPi using

```
pip install kohilites
```

## Quick Start

KOHilites is run from the command line. It can import and process multiple metadatafiles from a directory or single files if a specific path is given. The options available are:

- `--input`: Path to a single document's metadata or a directory containing metadata from several documents.
- `--output`: Directory to save parsed document metadata. If not given, outputs are saved to the root input directory. Defaults to blank.

### Examples

When given a directory input, KOHilites will search that directory and all its subdirectories for metadata files and parse them. It will save all of the outputs to the output directory (not copying any nested structure).

```bash
$ kohilites --input directory/containing/multiple/metadata/files --output directory/to/save/highlights
```

When given the path to a file, KOHilites will parse only that file. If no output directory is given, the output is saved to the same directory that contained the input file.

```bash
$ kohilites --input path/to/metatdata.epub.lua
```
