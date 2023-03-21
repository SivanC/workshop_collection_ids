# workshop_collection_ids

A small Python script that uses the Steam Web API to retrieve the IDs of 
workshop items in a collection and prints them in a comma-separated or 
formatted list to an output stream.

---
## Usage

    usage: workshop_collection_ids [-h] [-f FILE] [-F] collection_id [collection_id ...]

    positional arguments:
      collection_id         one or more space-separated Steam Workshop collection IDs

    options:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  write the output to FILE
      -F, --format          formats the list with collection ID, quotes, and newlines

To find the ID associated with a Steam Workshop collection, click on the
collection on the steam workshop, then click "Share," and copy the numbers at 
the end of the share link to use as a `collection_id`.

### Windows Users

Windows users should use the same options as above, but append `python3` before
the command in the command line, unless they are using bash or some other 
similar tool.

---
## Installation

This script requires Python 3. If you're not sure if you have it installed, 
type `python --version` to see your installed Python version, or install it
from [python.org](python.org).

Once Python is installed, simply download or copy `workshop_collection_ids.py` 
to your computer and run it from your file browser or command line.
