import click
import executor.judge.codeforces
import executor.judge.spoj
from sys import stdin
import executor.utility
from executor.evaluate import *

class Config(object):
    """ Config file to communicate between commands """

    def __init__(self):
        self.fname = None

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.argument('file', type=click.File('r'))
@pass_config
def cli(config, file):
    config.fname = file.name


@cli.command()
@click.argument('tag')
@pass_config
def codeforces(config, tag):
    """ Arguement: problem tag """

    try:
        executor.judge.codeforces.retrieve_test_cases(tag)
        evaluate(config.fname)
    except Exception as e:
        click.secho(str(e), fg='red')

@cli.command()
@click.argument('tag')
@pass_config
def spoj(config, tag):
    """ Arguement: problem tag """

    try:
        executor.judge.spoj.retrieve_test_cases(tag)
        evaluate(config.fname)
    except Exception as e:
        click.secho(str(e), fg='red')

@cli.command()
@pass_config
def check(config):
    """
    Checks code against already
    generated test cases.
    """

    try:
        evaluate(config.fname)
    except Exception as e:
        click.echo(str(e))


@cli.command()
@pass_config
def custom(config):
    """ Test your code against custom test cases """

    click.echo('Input test case (Press CTRL + D to exit).')
    a = stdin.read()

    input_case = dict()
    input_case[0] = a
    output_case = dict()
    output_case[0] = None

    test_cases = dict()
    test_cases['input'] = input_case
    test_cases['output'] = output_case

    executor.utility.write_json(test_cases)

    try:
        evaluate(config.fname)
    except Exception as e:
        print(str(e))