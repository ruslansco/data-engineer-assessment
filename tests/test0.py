"""Example test.

After copying our tests into this folder, we'll run `pytest` at the top level of the
repo and inspect the output.
"""
import requests

PORT = 8000
"""Change this depending on the port this is running on."""


def test_sanity():
    """If this fails, then something outside the repo is broken."""
    assert True


def test_simple_set_and_get():
    """Simple example test for minimal set + get action."""
    # /set shouldn't immediately fail
    resp = requests.post(
        f"http://localhost:{PORT}/set",
        json={
            "key": "hello",
            "val": "world",
        },
    )
    assert resp.status_code == 200

    # /get/hello should return `world`
    resp = requests.get(f"http://localhost:{PORT}/get/hello")
    assert resp.status_code == 200
    assert resp.json()["val"] == "world"

def test_all():
    """Test for /all endpoint."""

    resp = requests.get(
        f"http://localhost:{PORT}/all"
    )
    assert resp.status_code == 200