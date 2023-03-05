# Test Aggregator

This program processes a log file containing test results and aggregates the data to provide summary statistics.

## Usage

To use the program, run the `main` function. The program expects a file named `test_logs.txt` to be present in the same directory.

## Data Model

The program uses a `Test` class to represent each test. Each `Test` object has the following attributes:

    `type`: a string indicating the type of test event (either `testStarted` or `testFinished`)
    `id`: a string identifying the test
    `name`: a string containing the name of the test (only present if `type` is `testStarted`)
    `duration`: an integer indicating the duration of the test in milliseconds (only present if `type` is `testFinished`)
    `result`: a string indicating the result of the test (`PASS` or `FAIL`) (only present if `type` is `testFinished`)
    `error`: a string containing the error message (only present if `type` is `testFinished` and the test failed)

## Functions
`calculate_test_aggregation_data(test: list) -> dict`

This function takes a list of `Test` objects and returns a dictionary containing summary statistics. The dictionary has the following keys:

    `total_tests`: the total number of tests
    `total_passed`: the number of tests that passed
    `total_failed`: the number of tests that failed
    `total_duration`: the total duration of all tests in milliseconds

`print_test_aggregation_logs(test_aggregation_data: dict) -> None`
This function takes a dictionary containing summary statistics and prints them to the console in a user-friendly format.

`create_test_object(tokens: list) -> Test`
This function takes a list of tokens (strings) and returns a `Test` object based on the contents of the tokens.

`process_test_output(file_content: str) -> list`
This function takes a string containing the contents of a log file and returns a list of `Test` objects based on the log data.

`read_file(file_name: str) -> str`
This function takes a string containing the name of a file and returns the contents of the file as a string.

`main()`
This function is the main entry point of the program. It reads the log file, processes the data, aggregates the results, and prints them to the console.
