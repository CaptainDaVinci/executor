from os.path import splitext
import subprocess
import click
import executor.utility

TIMEOUT = 1

TICK = u'\u2714'
CROSS = u'\u2718'
BORDER = u'\u2550'

def time_it(func):
    def wrapper(*args, **kwargs):
        from time import time

        start = time()
        result = func(*args, **kwargs)
        return result.decode('utf-8'), time() - start

    return wrapper


@time_it
def run(test_case, obj):
    """
    Run the object file against test cases.
    Return a tuple with the output and timet taken.
    """

    return subprocess.check_output(['./' + obj], input=test_case, timeout=TIMEOUT)


def compile_file(cmd, file, obj):
    """
    Compile_files the given file.
    returns 0 if successful, non-zero other wise.
    """
    return subprocess.call([cmd, file, '-o', obj])


def run_test_cases(test_cases, obj_file):
    """ Runs the code on every test case matchin the output with expected output. """

    border = BORDER * click.get_terminal_size()[0]
    for i in range(len(test_cases['input'])):
        # Get the input and output test case as a string.
        test_case = test_cases['input'][str(i)]
        expected_output = test_cases['output'][str(i)]

        output, time_taken = run(str.encode(test_case), obj_file)
        output = output.strip()

        # Display Input/output.
        msg = '{}\nInput\n{}'.format(border, test_case)
        click.echo(msg)

        msg = 'Output\n{}\n'.format(output)
        click.echo(msg)

        if expected_output == None:
            continue

        msg = 'Expected Output\n{}\n'.format(expected_output)
        click.echo(msg)

        if expected_output == output:
            msg = 'ACCEPTED {}'.format(TICK)
            click.secho(msg, fg='green', bold=True)
        else:
            msg = 'WRONG ANSWER {}'.format(CROSS)
            click.secho(msg, fg='red', bold=True)

        msg = 'Time: {:.2f} seconds\n{}\n\n'.format(time_taken, border)
        click.echo(msg)


def evaluate(file_name):
    """ Entry point, runs the given file against test cases. """

    # Get file name and extension.
    name, extension = splitext(file_name)

    # Only C and C++ files are evaluated. For now.
    if extension == '.c':
        command = 'gcc'
    elif extension in ['.C', '.cpp', '.cc']:
        command = 'g++'
    else:
        raise Exception('Unrecognised file!')

    try:
        border = BORDER * click.get_terminal_size()[0]
        msg = '{}\nCOMPILING\n{} {} -o {}'.format(border, command, file_name, name)
        click.echo(msg)

        # Raise exception on compilation fail.
        if compile_file(command, file_name, name) != 0:
            raise Exception('Compilation Failed!')

        msg = 'File {} COMPILED SUCCESSFULLY\n\n{}\n\nRUNNING AGAINST TEST CASES\n'.format(file_name, border)
        click.echo(msg)

        test_cases = executor.utility.load_json()
        run_test_cases(test_cases, name)
    except subprocess.TimeoutExpired as e:
        # TLE.
        message = 'Time limit exceeded! {:.2f} second'.format(TIMEOUT)
        click.secho(message, fg='yellow', bold=True)

if __name__ == '__main__':
    evaluate('test.cc')