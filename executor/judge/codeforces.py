import re
import requests
import bs4 as bs
import executor.utility

# time out for requesting the html page.
TIMEOUT = 5


def get_sample_cases(test_cases, case_type):
    """ Returns a dictionary of input/output cases"""

    sample_cases = test_cases.find_all('div', class_=case_type)
    sample_cases = [case.pre for case in sample_cases]
    test_cases = {}

    for index, each_case in enumerate(sample_cases):
        lines = []
        for line in each_case.children:
            if line.string != None:
                lines.append(line)

        test_cases[index] = '\n'.join(lines).strip().replace('\r', '')

    return test_cases


def parse(response):
    """ Parses the test-cases from the html response obtained. """

    soup = bs.BeautifulSoup(response.text, 'lxml')
    title = str(soup.title.string)

    if title.find('Problem') == -1:
        raise Exception('Problem could not be found')

    test_cases_html = soup.find('div', class_='sample-test')

    # stores all input test cases.
    input_cases = get_sample_cases(test_cases_html, 'input')

    # stores all corresponding output test cases.
    output_cases = get_sample_cases(test_cases_html, 'output')

    # for a json with input and output test cases.
    test_cases = {}
    test_cases['input'] = input_cases
    test_cases['output'] = output_cases

    return test_cases


def form_url(problem_tag):
    """ Returns a codeforces url for the problem tag. """

    # problem tag is of the form pXXX or cXXX, denoting contest/problemset.
    problem_tag = problem_tag.lower()
    regex = re.compile(r'([cp])(\d+)([a-z])')

    if not re.match(regex, problem_tag):
        raise Exception('Incorrect Problem tag')

    group = re.findall(regex, problem_tag)[0]

    prob_lvl = group[2].upper()
    prob_num = group[1]

    if group[0] == 'p':
        return 'http://codeforces.com/problemset/problem/{}/{}'.format(prob_num, prob_lvl)
    else:
        return 'http://codeforces.com/contest/{}/problem/{}'.format(prob_num, prob_lvl)


def retrieve_test_cases(problem_tag):
    """ Retrieves and stores the test-cases for the given problem tag."""

    # Obtain url from the problem tag
    url = form_url(problem_tag)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
    }

    response = requests.get(url, headers=headers, timeout=TIMEOUT)

    # If page could not be loaded.
    if response.status_code != 200:
        raise Exception('Codeforces failed to load!')

    # Store the sample test cases.
    test_cases = parse(response)
    executor.utility.write_json(test_cases)


if __name__ == '__main__':
    retrieve_test_cases('p4a')
