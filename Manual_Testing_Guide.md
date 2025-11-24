# Manual Testing Guide

## Goal
Run the program manually for each test case described later and verify outputs for each sort option.

## Pre Requsites
- Ensure `student_grades.csv` exists at project root.
- Copy the coresponding data sets file for each test case for example if you are testing test case 1 then copy `manual_tests/student_grades_testcase1.csv` to `student_grades.csv`.

## Steps (Repeat 4 times, once per test case)
1. Copy the data in the test case file of the test case being tested from test_files folder to `student_grades.csv`. Test case files are named as follows `T#.csv` # is the testcase number.
2. Run: `python3 main.py`
3. When prompted, enter one of: `avg`, `high`, `low`, `median`
4. Confirm program completes without errors.
5. Open `sorted_grades.csv` and check if:
   - First line is a header 
   - Rows are present and appear sorted by the chosen metric
   - check the coresponding expected output file. For example, for test case 1 look at `T1/expected/actual_avg.csv`
   - Add the results of what the actual output was under for example for T1 `T1/actual/actual_avg.csv`'.
   - Check off pass or fail for each test case. Give the reason a short concise sentences of why the test failed.

## Test Cases
1. 1 of the students has all zeros 
    - Avg
        - [X] Pass
        - [ ] Fail
    - High
        - [X] Pass
        - [ ] Fail
    - Low
        - [X] Pass
        - [ ] Fail
    - Median
        - [ ] Pass
        - [X] Fail: This happens because the code only compares median values. When two students have the same median, the program does not apply any alphabetical tie-breaking, even though it should. Proper handling of this edge case would require sorting by name when the medians are equal.

2.  1 of the students has all the same number
    - Avg
        - [] Pass
        - [X] Fail: This happens because the code only compares avg values. When two students have the same avgs, the program does not apply any alphabetical tie-breaking, even though it should. Proper handling of this edge case would require sorting by name when the avgs are equal.
    - High
        - [X] Pass
        - [ ] Fail
    - Low
        - [X] Pass
        - [ ] Fail
    - Median
        - [ ] Pass
        - [X] Fail: This happens because the code only compares median values. When two students have the same median, the program does not apply any alphabetical tie-breaking, even though it should. Proper handling of this edge case would require sorting by name when the medians are equal.
3. Just a regular one where it represents a usual (normally seen with different grades) set
    - Avg
        - [X] Pass
        - [ ] Fail
    - High
        - [X] Pass
        - [ ] Fail
    - Low
        - [X] Pass
        - [ ] Fail
    - Median
        - [X] Pass
        - [ ] Fail
4. 2 of the students have the same sequence of grades
    - Avg
        - [ ] Pass
        - [X] Fail: This happens because the code only compares avg values. When two students have the same avgs, the program does not apply any alphabetical tie-breaking, even though it should. Proper handling of this edge case would require sorting by name when the avgs are equal.
    - High
        - [ ] Pass
        - [X] Fail: This happens because the code only compares high values. When two students have the same high, the program does not apply any alphabetical tie-breaking, even though it should. Proper handling of this edge case would require sorting by name when the highs are equal.
    - Low
        - [ ] Pass
        - [X] Fail: This happens because the code only compares lows values. When two students have the same lows, the program does not apply any alphabetical tie-breaking, even though it should. Proper handling of this edge case would require sorting by name when the lows are equal.
    - Median
        - [ ] Pass
        - [X] Fail: This happens because the code only compares median values. When two students have the same median, the program does not apply any alphabetical tie-breaking, even though it should. Proper handling of this edge case would require sorting by name when the medians are equal.
5. 2 of them has the same sequence of grades
    - Avg
        - [X] Pass
        - [ ] Fail
    - High
        - [X] Pass
        - [ ] Fail
    - Low
        - [X] Pass
        - [ ] Fail
    - Median
        - [X] Pass
        - [ ] Fail
