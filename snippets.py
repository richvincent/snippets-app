import psycopg2
import logging
import click
from tabulate import tabulate
from subprocess import call
from datetime import datetime as date

# Set the log output file and log level
logging.basicConfig(filename='snippets.log', level=logging.DEBUG)

# Connecting to the PostGreSQL Database
logging.debug('Connecting to PostgreSQL | {}'.format(date.today()))
connection = psycopg2.connect(database='snippets')
logging.debug('Database connection establishe | {}'.format(date.today()))


def put(args):
    """The puts function """
    print(args[0])
    print(args[1:])

    name = args[0]
    snippet = args[1]

    logging.info('Storing snippet {!r}: {!r} | {}'.format(name, snippet,
                                                          date.today()))
    try:
        with connection, connection.cursor() as cursor:
            cursor.execute('insert into snippets values\
                           (\'{}\', \'{}\')'.format(name, snippet))
            print('Record Added')
            logging.debug('Record added: name {} message {} |\
                          {}'.format(name, snippet, date.today()))
    except:
        connection.rollback()
        with connection, connection.cursor() as cursor:
            cursor.execute('update snippets set message=\'{}\' where\
                           keyword=\'{}\''.format(snippet, name))
            print('Record updated')
            logging.debug('Record updated: name {} message {} |\
                          {}'.format(name, snippet, date.today()))


def get(args):
    """The gets function"""
    name = args[0]
    logging.info('Retrieving snippet {!r} | {}'.format(name, date.today()))
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s",
                       (name,))
        record = cursor.fetchone()
        logging.debug("Snippet {} message\
                       {} retrieved successfully | {}".format(name, record[1],
                                                              date.today()))

    if not record:
        print('No snippet was found with the name {}'.format(name))
    else:
        for field in record:
            print(field)

        return(record)


def catalog():
    """The gets function"""
    logging.info('Retrieving all records to build a catalog')
    with connection, connection.cursor() as cursor:
        cursor.execute("select * from snippets")
        records = cursor.fetchall()
    logging.debug("All records retrieved successfully |\
                  {}".format(date.today()))

    if not records:
        print('Table Empty')
    else:
        records.insert(0, ('keyword', 'message'))
        print(tabulate(records, tablefmt='simple', headers='firstrow'))
        return(records)


def search(args):
    """Searches the message of a snippet"""
    search = args[0]
    logging.info('Searching snippet {!r}'.format(search))
    with connection, connection.cursor() as cursor:
        cursor.execute('select * from snippets where message like \'%{}%\''
                       .format(search))
        records = cursor.fetchall()
        logging.debug("Snippet search {} successful | {} \
                      ".format(search, date.today()))

    if not records:
        print('No snippet was found with the name {}'.format(search))
    else:
        records.insert(0, ('keyword', 'message'))
        print(tabulate(records, tablefmt='simple', headers='firstrow'))
        return(records)


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
    elif command == 'catalog':
        catalog()
    elif command == 'search':
        if len(args) == 1:
            search(args)
        else:
            print('Unexpected arguments {}'.format(args))
    else:
        print('The requested command {{{}}} has not been implemented.'
              .format(command))


if __name__ == '__main__':
    call('clear')
    main()
