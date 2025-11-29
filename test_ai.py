import statistics
import pytest

from student import Student  # uses existing Student class
import main as m             # provides merge_sort_* functions


def nondecreasing(seq, key):
    """Return True if key(seq) is non-decreasing."""
    return all(key(seq[i]) <= key(seq[i + 1]) for i in range(len(seq) - 1))


def make_students(pattern):
    """
    Construct Student lists for the Base Choice Coverage (BCC) patterns.

    Grade pattern characteristic:
      A1 = all zeros
      A2 = all same number
      A3 = typical mixed grades   (base)
      A4 = duplicate sequences
    """
    if pattern == "A1_all_zeros":
        # Two all-zero students + one normal student
        return [
            Student("Zara", ["0", "0", "0", "0", "0", "0", "0"]),
            Student("Amy",  ["0", "0", "0", "0", "0", "0", "0"]),
            Student("Liam", ["50", "60", "70", "80", "90", "40", "30"]),
        ]
    if pattern == "A2_all_same":
        # Everyone has the same mark in every assignment
        return [
            Student("Zara", ["75"] * 7),
            Student("Amy",  ["75"] * 7),
            Student("Liam", ["75"] * 7),
        ]
    if pattern == "A4_duplicates":
        # Two students share identical full grade sequences
        return [
            Student("Zara", ["60", "70", "80", "90", "100", "80", "70"]),
            Student("Amy",  ["60", "70", "80", "90", "100", "80", "70"]),
            Student("Liam", ["40", "50", "60", "70", "80", "90", "100"]),
        ]
    # Default base case: A3 = typical mixed grades
    return [
        Student("Ava",  ["90", "88", "92", "95", "91", "89", "93"]),
        Student("Ben",  ["70", "75", "72", "68", "74", "71", "69"]),
        Student("Cara", ["100", "99", "100", "100", "98", "100", "99"]),
        Student("Drew", ["40", "55", "60", "65", "50", "70", "60"]),
    ]


# Map sort option (input space characteristic B) to merge sort + key
def sort_config(option):
    """
    Sorting criterion characteristic:
      B1 = avg
      B2 = high
      B3 = low
      B4 = median
    """
    if option == "avg":
        return m.merge_sort_avg, lambda s: s.get_avg()
    if option == "high":
        return m.merge_sort_high, lambda s: int(s.get_highest())
    if option == "low":
        return m.merge_sort_low, lambda s: int(s.get_lowest())
    if option == "median":
        # Convert median to float for consistent numeric comparison
        return m.merge_sort_median, lambda s: float(s.get_median())
    raise ValueError(f"Unknown option: {option!r}")


# -------- Base Choice Coverage (BCC) test suite --------
#
# Base choices:
#   A3 (typical mixed grades), B1 (avg)
#
# Tests:
#   T0: (A3, B1)   - base test
#   T1: (A1, B1)   - vary A -> all zeros
#   T2: (A2, B1)   - vary A -> all same number
#   T3: (A4, B1)   - vary A -> duplicate sequences
#   T4: (A3, B2)   - vary B -> high
#   T5: (A3, B3)   - vary B -> low
#   T6: (A3, B4)   - vary B -> median
#
# This satisfies Base Choice Coverage for characteristics A and B.


@pytest.mark.parametrize("pattern, option", [
    ("A3_mixed", "avg"),     # base test
    ("A1_all_zeros", "avg"),
    ("A2_all_same", "avg"),
    ("A4_duplicates", "avg"),
    ("A3_mixed", "high"),
    ("A3_mixed", "low"),
    ("A3_mixed", "median"),
])
def test_bcc_patterns_sort_correctly(pattern, option):
    """BCC: every pattern/option pair should sort in non-decreasing order."""
    students = make_students(pattern)
    sort_fn, key = sort_config(option)
    sort_fn(students)
    assert nondecreasing(students, key)


# -------- Targeted AI-generated tests for tricky tie cases --------

def get_names(students):
    return [s.name for s in students]


def test_ties_on_average_should_break_by_name():
    """
    AI-designed tie case:
    Two students with identical averages should be ordered alphabetically.
    Current implementation only compares averages, so this test exposes
    the missing tie-breaking rule.
    """
    students = [
        Student("Zoe", ["80", "90"]),      # avg = 85
        Student("Aaron", ["85", "85"]),    # avg = 85
    ]
    m.merge_sort_avg(students)
    # Expected "Aaron" then "Zoe" if tie-breaking by name is implemented
    assert get_names(students) == sorted(get_names(students))


def test_ties_on_median_should_break_by_name():
    """
    AI-designed tie case for median.
    Again, this test encodes the *desired* behaviour, not the current one,
    so a failure indicates a defect in the sorting logic.
    """
    students = [
        Student("Zoe", ["70", "80", "90"]),     # median = 80
        Student("Aaron", ["80", "80", "80"]),   # median = 80
    ]
    m.merge_sort_median(students)
    assert get_names(students) == sorted(get_names(students))


def test_csv_writer_creates_separate_columns(tmp_path, monkeypatch):
    """
    AI-designed I/O test:
    Verifies that Write_file writes each grade into its own CSV column
    rather than concatenating everything into a single cell.
    """
    # Use a dataset with the expected 7 grades per student
    students = [
        Student("Ava", ["90", "80", "70", "60", "50", "40", "30"]),
        Student("Ben", ["70", "60", "50", "40", "30", "20", "10"]),
    ]

    # Run writer in a temporary directory
    monkeypatch.chdir(tmp_path)
    m.Write_file(students)

    out_path = tmp_path / "sorted_grades.csv"
    content = out_path.read_text().strip().splitlines()
    header = content[0].split(",")
    row = content[1].split(",")

    # Expect header: Name + 7 assignment columns
    assert header == ["Name", "A0", "A1", "A2", "A3", "A4", "A5", "A6"]
    # Expect data row to have the same number of columns as the header
    assert len(row) == len(header)