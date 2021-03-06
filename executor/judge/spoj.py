import requests
import bs4 as bs
import executor.utility

TIMEOUT = 5


def get_test_cases(response):
    response = response.strip().split('Output:')

    input_cases = dict()
    output_cases = dict()

    input_cases[0] = '\n'.join(response[0].split(
        '\n')[1:]).strip().replace('\r', '')
    output_cases[0] = '\n'.join(
        response[1].split('\n')).strip().replace('\r', '')

    test_cases = dict()
    test_cases['input'] = input_cases
    test_cases['output'] = output_cases

    return test_cases


def parse(response):
    soup = bs.BeautifulSoup(response.text, 'lxml')
    problem = soup.find(id='problem-body')
    test_cases_html = problem.find('pre')
    test_cases = get_test_cases(test_cases_html.text)

    return test_cases


def retrieve_test_cases(tag):
    url = 'http://www.spoj.com/problems/{}'.format(tag)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
    }

    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    test_cases = parse(response)

    executor.utility.write_json(test_cases)


if __name__ == '__main__':
    retrieve_test_cases('TEST')
