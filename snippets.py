import logging
import sys
import argparse

# Set the log output file, and lof level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


def put(name, snippet):
    """
    Store a snippet with an associated name.

    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})"
                  .format(name, snippet))
    return name, snippet


def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet...

    Returns the snippet.
    """

    logging.error("FIXME: Umimplemented - get({!r})".format(name))
    return ""

def main():
    """Mian function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(
        description="Store and retrieve snippets of text")
    arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()


