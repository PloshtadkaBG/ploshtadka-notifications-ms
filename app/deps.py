from dataclasses import dataclass, field
from urllib.parse import unquote
from uuid import UUID

from fastapi import Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.scopes import NOTIFICATION_SCOPE_DESCRIPTIONS, NotificationScope

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
    scopes={**NOTIFICATION_SCOPE_DESCRIPTIONS},
)


# ---------------------------------------------------------------------------
# Auth — reads Traefik-injected headers
# ---------------------------------------------------------------------------


@dataclass
class CurrentUser:
    id: UUID
    username: str
    scopes: list[str] = field(default_factory=list)

    @property
    def is_admin(self) -> bool:
        return "admin:scopes" in self.scopes


def get_current_user(
    x_user_id: str = Header(...),
    x_username: str = Header(...),
    x_user_scopes: str = Header(default=""),
) -> CurrentUser:
    """
    Reads headers injected by Traefik after forwardAuth validation.
    JWT has already been verified at the gateway — never validate it here.
    """
    try:
        user_id = UUID(x_user_id)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user identity from gateway",
        ) from None

    scopes = x_user_scopes.split(" ") if x_user_scopes else []
    return CurrentUser(id=user_id, username=unquote(x_username), scopes=scopes)


def require_scopes(*required: str):
    """Factory that returns a scope-enforcing dependency."""

    async def _dep(
        current_user: CurrentUser = Depends(get_current_user),
    ) -> CurrentUser:
        missing = [s for s in required if s not in current_user.scopes]
        if missing:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Missing required scopes: {', '.join(missing)}",
            )
        return current_user

    return _dep


# Pre-built scope dependencies
can_read_notifications = require_scopes(NotificationScope.ADMIN_READ)
can_send_notification = require_scopes(NotificationScope.ADMIN_WRITE)
