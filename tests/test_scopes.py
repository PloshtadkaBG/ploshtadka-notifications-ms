"""Tests that PaymentScope values and descriptions stay in sync."""

from app.scopes import PAYMENT_SCOPE_DESCRIPTIONS, PaymentScope


def test_all_scopes_have_descriptions():
    for scope in PaymentScope:
        assert scope in PAYMENT_SCOPE_DESCRIPTIONS, (
            f"PaymentScope.{scope.name} missing from PAYMENT_SCOPE_DESCRIPTIONS"
        )


def test_scope_values_are_strings():
    for scope in PaymentScope:
        assert isinstance(scope.value, str)
        assert len(scope.value) > 0


def test_customer_read_scope():
    assert PaymentScope.READ == "payments:read"


def test_admin_scopes_prefixed():
    admin_scopes = [
        PaymentScope.ADMIN,
        PaymentScope.ADMIN_READ,
        PaymentScope.ADMIN_WRITE,
        PaymentScope.ADMIN_DELETE,
    ]
    for scope in admin_scopes:
        assert scope.startswith("admin:"), f"{scope} should start with 'admin:'"
