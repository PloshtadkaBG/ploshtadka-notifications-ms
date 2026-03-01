from enum import StrEnum


class NotificationScope(StrEnum):
    # Admin scopes — this is an internal service, no customer-facing scopes
    ADMIN = "admin:notifications"
    ADMIN_READ = "admin:notifications:read"
    ADMIN_WRITE = "admin:notifications:write"


NOTIFICATION_SCOPE_DESCRIPTIONS: dict[str, str] = {
    NotificationScope.ADMIN: "Full access to notifications (admin super-scope).",
    NotificationScope.ADMIN_READ: "View notification history (admin).",
    NotificationScope.ADMIN_WRITE: "Send notifications (admin).",
}
