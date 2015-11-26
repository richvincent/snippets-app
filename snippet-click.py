import click
import logging

# Set the log output file, and log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


@click.group()
def snippets():
    pass


@click.command()
@click.argument('name')
def gets(name):
    """ Retrieve the snippet with a given name.

    If there is no such snippet...abs

    Return the snippet
    """
    logging.error("FIXME: unimplemented - get({!r})".format(name))
    return ""

    print(name)


@click.command()
@click.argument('name')
@click.argument('content')
def puts(name, content):
    """
    Store a snippet with an associated name.

    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, content
                                                                  ))
    return name, content
    print(name)
    print(content)


@click.command()
@click.option('--name', help='Enter a name')
@click.option('--content', help='Enter some content')
def main(name, content):
    """ Main Funnction """
    logging.info("Constructing parser")
    print(name)
    print(content)

if __name__ == "__main__":
    main()
