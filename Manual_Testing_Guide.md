# Manual Testing Guide

## Goal
Run the program manually and verify outputs for each sort option.

## Pre Requsites
- Ensure `student_grades.csv` exists at project root.
- Copy the coresponding data sets file for each test case for example if you are testing test case 1 then copy `manual_tests/student_grades_sample1.csv` to `student_grades.csv`.

## Steps (Repeat 4 times, once per test case)
1. Copy the data in the student_grades_sample file of the test case you are testing in `student_grades.csv`
2. Run: `python3 main.py`
3. When prompted, enter one of: `avg`, `high`, `low`, `median`
4. Confirm program completes without errors.
5. Open `sorted_grades.csv` and check if:
   - First line is a header 
   - Rows are present and appear sorted by the chosen metric
   - check the coresponding expected output file. For example, for test case 1 look at `manual_tests/student_grades_sample1_EO.csv` 
   - Check off pass or fail for each test case

## Test Cases
1. 1 of them is all zeros 
    - Avg
        - [ ] Pass
        - [ ] Fail
    - High
        - [ ] Pass
        - [ ] Fail
    - Low
        - [ ] Pass
        - [ ] Fail
    - Median
        - [ ] Pass
        - [ ] Fail

2. 1 of them is all the same number
    - Avg
        - [ ] Pass
        - [ ] Fail
    - High
        - [ ] Pass
        - [ ] Fail
    - Low
        - [ ] Pass
        - [ ] Fail
    - Median
        - [ ] Pass
        - [ ] Fail
3. Just a regular one where it represents a usual (normally seen with different grades) set
    - Avg
        - [ ] Pass
        - [ ] Fail
    - High
        - [ ] Pass
        - [ ] Fail
    - Low
        - [ ] Pass
        - [ ] Fail
    - Median
        - [ ] Pass
        - [ ] Fail
4. 1 of them has all 100s
    - Avg
        - [ ] Pass
        - [ ] Fail
    - High
        - [ ] Pass
        - [ ] Fail
    - Low
        - [ ] Pass
        - [ ] Fail
    - Median
        - [ ] Pass
        - [ ] Fail
5. 2 of them has the same sequence of grades
    - Avg
        - [ ] Pass
        - [ ] Fail
    - High
        - [ ] Pass
        - [ ] Fail
    - Low
        - [ ] Pass
        - [ ] Fail
    - Median
        - [ ] Pass
        - [ ] Fail
