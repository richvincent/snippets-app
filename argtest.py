import psycopg2
import logging
import click
from subprocess import call

# Set the log output file and log level
logging.basicConfig(filename='snippets.log', level=logging.DEBUG)

# Connecting to the PostGreSQL Database
logging.debug('Connecting to PostgreSQL')
connection = psycopg2.connect(database='snippets')
logging.debug('Database connection established')


def put(args):
    """The puts function """
    print(args[0])
    print(args[1:])

    name = args[0]
    snippet = args[1]

    logging.info('Storing snippet {!r}: {!r}'.format(name, snippet))
    cursor = connection.cursor()
    command = 'insert into snippets values (%s, %s)'
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully")


def get(args):
    """The gets function"""
    name = args[0]
    logging.info('Retrieving snippet {!r}'.format(name))
    cursor = connection.cursor()
    command = 'select * from snippets where keyword=\'{}\''
    cursor.execute(command.format(name))
    record = cursor.fetchone()
    logging.debug("Snippet retrieved successfully")
    for field in record:
        print(field)


@click.command()
@click.argument('command', nargs=1)
@click.argument('args', nargs=-1)
def main(command, args):
    if command == 'put':
        if len(args) == 2:
            put(args)
        else:
            print('Unexpected arguments {}'.format(args))
    elif command == 'get':
        if len(args) == 1:
            get(args)
        else:
            print('Unexpected arguments {}'.format(args))
    else:
        print('The requested command {{{}}} has not been implemented.'
              .format(command))


if __name__ == '__main__':
    call('clear')
    main()
