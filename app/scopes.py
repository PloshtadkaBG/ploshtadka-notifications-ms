from enum import StrEnum


class PaymentScope(StrEnum):
    # Customer scopes
    READ = "payments:read"  # view own payment history

    # Admin scopes
    ADMIN = "admin:payments"
    ADMIN_READ = "admin:payments:read"
    ADMIN_WRITE = "admin:payments:write"
    ADMIN_DELETE = "admin:payments:delete"


PAYMENT_SCOPE_DESCRIPTIONS: dict[str, str] = {
    PaymentScope.READ: "View your own payment history.",
    PaymentScope.ADMIN: "Full access to all payments (admin super-scope).",
    PaymentScope.ADMIN_READ: "Read any payment (admin).",
    PaymentScope.ADMIN_WRITE: "Modify any payment or issue refunds (admin).",
    PaymentScope.ADMIN_DELETE: "Hard-delete any payment record (admin).",
}
