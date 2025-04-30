from odoo import _, api, Command, fields, models
from odoo.exceptions import ValidationError
import logging
import requests
from .config import BASE_URL

_logger = logging.getLogger(__name__)

class purchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def sign_document(self):
        _logger.info(f"retriving env {self.env}")
        for record in self:
            _logger.debug(f"Signing document")
            user = record.env.user
            _logger.info(f" user found {user}")
            if user:
                user.enroll_for_signature()
                try:
                    # todo sign the document
                    pass
                except Exception as e:
                    _logger.error(f"Error when contacting sign {e}")
            else:
                _logger.warning(f"User not found")




