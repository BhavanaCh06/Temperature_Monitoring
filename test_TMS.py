from TMS import get_status


def test_normal_temperature():
    assert get_status(50) == "NORMAL"


def test_warning_temperature():
    assert get_status(85) == "WARNING"


def test_critical_temperature():
    assert get_status(110) == "CRITICAL"


def test_boundary_warning():
    assert get_status(80) == "WARNING"


def test_boundary_critical():
    assert get_status(100) == "CRITICAL"
