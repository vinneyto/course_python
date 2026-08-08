import pytest

from .task import parse_endpoint


def test_parses_hostname_ipv4_and_bracketed_ipv6():
    assert parse_endpoint("example.com:443", 80) == ("example.com", 443)
    assert parse_endpoint("127.0.0.1", 8080) == ("127.0.0.1", 8080)
    assert parse_endpoint("[2001:db8::1]:8443", 80) == ("2001:db8::1", 8443)
    assert parse_endpoint("[::1]", 8000) == ("::1", 8000)


@pytest.mark.parametrize(
    "value, default_port",
    [("", 80), ("host:0", 80), ("host:65536", 80), ("host:http", 80), ("::1", 80)],
)
def test_rejects_invalid_endpoints(value, default_port):
    with pytest.raises(ValueError):
        parse_endpoint(value, default_port)
