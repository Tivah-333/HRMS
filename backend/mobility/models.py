from django.db import models

class MobilityStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PENDING = "PENDING", "Pending"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"
    CANCELLED = "CANCELLED", "Cancelled"
    IMPLEMENTED = "IMPLEMENTED", "Implemented"

class TransferRequest(models.Model):
    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="transfer_requests"
    )
    current_department = models.ForeignKey(
        "employees.Department",
        on_delete=models.PROTECT,
        related_name="outgoing_transfers"
    )
    proposed_department = models.ForeignKey(
        "employees.Department",
        on_delete=models.PROTECT,
        related_name="incoming_transfers"
    )
    current_position = models.ForeignKey(
        "employees.Position",
        on_delete=models.PROTECT,
        related_name="current_transfer_positions"
    )
    proposed_position = models.ForeignKey(
        "employees.Position",
        on_delete=models.PROTECT,
        related_name="proposed_transfer_positions"
    )
    reason = models.CharField(max_length=255)
    effective_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=MobilityStatus.choices,
        default=MobilityStatus.DRAFT
    )
    initiated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="initiated_transfers"
    )
    approved_at = models.DateTimeField(
        null=True,
        blank=True
    )
    implemented_at = models.DateTimeField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]