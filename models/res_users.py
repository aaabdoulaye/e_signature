from odoo import _, api, Command, fields, models
from odoo.exceptions import ValidationError
import logging
import requests
from .config import BASE_URL, CERTIFICATE

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    cni = fields.Char(string="CNI", required=False)
    sign_application_id = fields.Char(string="Sign application Id", required=False)
    phone_number = fields.Char(string="User phone number", required=False)
    code_pin = fields.Char(string="code pin", required=False)
    sign_id = fields.Char(string="Sign Id", required=False)
    certificate = fields.Char(string="Certificate", required=False)

    def enroll_for_signature(self):
        for record in self:
            _logger.debug(f"Enroll user {record.name}")
            if not record.sign_id and not record.code_pin:
                try:
                    _logger.debug(f"No credential found")
                    data = {"cni": record.cni, "idApplication": record.sign_application_id, "nomSignataire": record.name, "telephone": record.phone_number}
                    enroll = requests.post(f"{BASE_URL}/enroll", json=data, verify=CERTIFICATE)
                    enroll = enroll.json()
                    _logger.debug(f"enroll data {enroll}")
                    if "certificate" in enroll:
                        record.write({"code_pin": enroll["codePin"], "sign_id": enroll["id_signer"], "certificate": enroll["certificate"]})
                        _logger.info(f"user {record.name} successfully enrolled")
                    else:
                        _logger.warning(f"Error found when enrolling {enroll}")
                except Exception as e:
                    _logger.error(f"Error when contacting enroll {e}")
            else:
                _logger.info(f"User already enrolled {record.name}")




