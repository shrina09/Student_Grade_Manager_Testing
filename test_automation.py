import builtins
import importlib
from pathlib import Path
import io, sys, statistics
import pytest

# ---------- Unit tests for Student class ----------

def test_student_avg_high_low_median():
    from student import Student
    s = Student("Ava", ["90", "88", "92", "95", "91", "89", "93"])
    assert pytest.approx(s.get_avg(), rel=1e-6) == (90 + 88 + 92 + 95 + 91 + 89 + 93) / 7
    assert int(s.get_highest()) == 95
    assert int(s.get_lowest()) == 88
    assert float(s.get_median()) == statistics.median([90,88,92,95,91,89,93])
    

# def test_student_duplicates_and_even_count():
#     from student import Student
#     s = Student("Even", ["10","20","30","40"])
#     assert float(s.get_median()) == 25.0
#     dup = Student("Dup", ["80","80","80","80"])
#     assert dup.get_avg() == 80
#     assert int(dup.get_highest()) == 80

# ---------- Algorithm tests for merge sorts ----------

def mk_students():
    from student import Student
    return [
        Student("Ava",  ["90","88","92","95","91","89","93"]),
        Student("Ben",  ["70","75","72","68","74","71","69"]),
        Student("Cara", ["100","99","100","100","98","100","99"]),
    ]

def nondec(seq, key):
    return all(key(seq[i]) <= key(seq[i+1]) for i in range(len(seq)-1))

@pytest.mark.parametrize("func_name,key", [
    ("merge_sort_avg", lambda s: s.get_avg()),
    ("merge_sort_high", lambda s: int(s.get_highest())),
    ("merge_sort_low", lambda s: int(s.get_lowest())),
    ("merge_sort_median", lambda s: int(float(s.get_median()))),
])
def test_mergesort_variants(func_name, key):
    from main import merge_sort_avg, merge_sort_high, merge_sort_low, merge_sort_median
    fn = locals()[func_name]
    students = mk_students()
    fn(students)
    assert nondec(students, key)

# ---------- Integration (I/O) tests ----------

SAMPLE = (
    "Name,A0,A1,A2,A3,A4,A5,A6\n"
    "Ava,90,88,92,95,91,89,93\n"
    "Ben,70,75,72,68,74,71,69\n"
    "Cara,100,99,100,100,98,100,99\n"
)

@pytest.mark.parametrize("option,expect", [
    ("avg", "Ava"),
    ("high", "Cara"),
    ("low", "Ben"),
    ("median", "Cara"),
])
def test_integration_runs_and_writes(tmp_path, monkeypatch, option, expect):
    csv_path = tmp_path / "student_grades.csv"
    csv_path.write_text(SAMPLE)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(builtins, "input", lambda _: option)

    # Capture output
    import main as m
    importlib.reload(m)
    if hasattr(m, "main"):
        buf, old = io.StringIO(), sys.stdout
        try:
            sys.stdout = buf
            m.main()
        finally:
            sys.stdout = old

    out_path = tmp_path / "sorted_grades.csv"
    assert out_path.exists()
    content = out_path.read_text()
    assert expect in content
