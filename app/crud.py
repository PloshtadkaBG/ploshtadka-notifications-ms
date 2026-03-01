from __future__ import annotations

from ms_core import CRUD

from app.models import Notification, NotificationStatus
from app.schemas import NotificationResponse


class NotificationCRUD(CRUD[Notification, NotificationResponse]):  # type: ignore
    async def log_sent(
        self,
        *,
        recipient: str,
        subject: str,
        template: str,
        resend_id: str,
        triggered_by: str | None = None,
    ) -> NotificationResponse:
        inst = await Notification.create(
            recipient=recipient,
            subject=subject,
            template=template,
            status=NotificationStatus.SENT,
            resend_id=resend_id,
            triggered_by=triggered_by,
        )
        return NotificationResponse.model_validate(inst)

    async def log_failed(
        self,
        *,
        recipient: str,
        subject: str,
        template: str,
        error: str,
        triggered_by: str | None = None,
    ) -> NotificationResponse:
        inst = await Notification.create(
            recipient=recipient,
            subject=subject,
            template=template,
            status=NotificationStatus.FAILED,
            error=error,
            triggered_by=triggered_by,
        )
        return NotificationResponse.model_validate(inst)

    async def list_notifications(
        self,
        *,
        page: int = 1,
        page_size: int = 20,
    ) -> list[NotificationResponse]:
        offset = (page - 1) * page_size
        items = await Notification.all().offset(offset).limit(page_size)
        return [NotificationResponse.model_validate(n) for n in items]


notification_crud = NotificationCRUD(Notification, NotificationResponse)
