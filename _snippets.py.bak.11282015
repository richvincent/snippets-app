import click
import logging
import psycopg2
from subprocess import call


# Set the log output file, and log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

# Connecting to the PostGreSQL Database
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("Database connection established")


@click.command()
@click.option('--name', help='Enter a name')
@click.option('--snippet', help='Enter a snippet')
def main(name, snippet):
    """ Main Funnction """
    call('clear')
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")

    print('\n')
    print(name)
    print(snippet)
    print('\n\n\n')

if __name__ == "__main__":
    main()
