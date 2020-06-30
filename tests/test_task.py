from tasks import Task
import pytest


def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.run_these
def test_member_access():
    t = Task("buy milk", "tyler")
    assert t.summary == "buy milk"
    assert t.owner == "tyler"
    assert (t.done, t.id) == (False, None)


def test_asdict():
    t_task = Task("this is a task", "tyler", True, 21)
    t_dict = t_task._asdict()
    expected = {"summary": "this is a task", "owner": "tyler", "done": True, "id": 21}
    assert t_dict == expected


def test_replace():
    t_before = Task("finish", "tyler", False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task("finish", "tyler", True, 10)
    assert t_after == t_expected
