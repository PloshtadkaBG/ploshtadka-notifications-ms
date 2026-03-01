from app.scopes import NOTIFICATION_SCOPE_DESCRIPTIONS, NotificationScope


class TestNotificationScopes:
    def test_all_scopes_have_descriptions(self):
        for scope in NotificationScope:
            assert scope in NOTIFICATION_SCOPE_DESCRIPTIONS

    def test_scope_values(self):
        assert NotificationScope.ADMIN == "admin:notifications"
        assert NotificationScope.ADMIN_READ == "admin:notifications:read"
        assert NotificationScope.ADMIN_WRITE == "admin:notifications:write"
