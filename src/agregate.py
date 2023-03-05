
import sys
from io import StringIO

test_start = "testStarted id=”5” name = “Test Name”"
test_finished = "testFinished id=”5” duration=”100” result=FAIL error=”Error Text”"

class Test:
    def __init__(self, type:str, id:int, name:str=None, duration:float=None, result:str=None, error:str=None):
        self.type = type
        self.id = id
        self.name = name
        self.duration = duration
        self.result = result
        self.error = error

    def __str__(self):
        return f'{self.type} {self.id} {self.name} {self.duration} {self.result} {self.error}'
    

def print_to_stdout() -> None:
    print(test_start)
    print(test_finished)

def main():
    stdout_buffer = StringIO()
    sys.stdout = stdout_buffer
    print_to_stdout()
    sys.stdout = sys.__stdout__
    file_content = stdout_buffer.getvalue()
    tokens = process_test_output(file_content)
    test_aggregation_data = calculate_test_aggregation_data(tokens)
    print_test_aggregation_logs(test_aggregation_data)

def calculate_test_aggregation_data(test: list) -> dict:
    data = {}
    data['total_tests'] = len([1 for t in test if t.type == 'testStarted'])
    data['total_passed'] = sum(1 for t in test if t.result == 'PASS')
    data['total_failed'] = data['total_tests'] - data['total_passed']
    data['total_duration'] = sum(int(t.duration) for t in test if t.duration)
    return data

def print_test_aggregation_logs(test_aggregation_data: dict) -> None:
    print(f'\nTotal tests run: {test_aggregation_data["total_tests"]}')
    print(f'Total passed: {test_aggregation_data["total_passed"]}')
    print(f'Total failed: {test_aggregation_data["total_failed"]}')
    print(f'Total duration: {test_aggregation_data["total_duration"]} ms')


def create_test_object(tokens: list) -> Test:
    type_ = tokens[0]
    id_ = tokens[1].split('=')[1].strip('”')
    if type_ == 'testStarted':
        name_ = tokens[4].strip('”')
        return Test(type_, id_, name_)
    elif type_ == 'testFinished':
        duration_ = tokens[2].split('=')[1].strip('”')
        result_ = tokens[3].split('=')[1].strip()
        error_ = tokens[4].split('=')[1].strip('”')
        return Test(type_, id_, duration=duration_, result=result_, error=error_)
    


def process_test_output(file_content: str) -> list:
    lines = file_content.splitlines()
    tests = []
    for line in lines:
        tokens = line.split(' ')
        tests.append(create_test_object(tokens))
    return tests

        

def read_file(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.read()

if __name__ == '__main__':
    main()

