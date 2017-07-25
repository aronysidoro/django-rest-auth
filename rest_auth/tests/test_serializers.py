from django.test import TestCase
from django.utils.translation import ugettext_lazy as _

from rest_auth.serializers import (LoginSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer)


class LoginSerializerTests(TestCase):

    def test_error_messages(self):
        self.assertEqual(
            LoginSerializer.EMAIL_PASSWORD_REQUIRED,
            _('Must include "email" and "password".'))
        self.assertEqual(
            LoginSerializer.USERNAME_PASSWORD_REQUIRED,
            _('Must include "username" and "password".'))
        self.assertEqual(
            LoginSerializer.USERNAME_PASSWORD_DONT_MATCH,
            _('Unable to log in with provided credentials.'))
        self.assertEqual(
            LoginSerializer.USERNAME_EMAIL_PASSWORD_REQUIRED,
            _('Must include either "username" or "email" and "password".'))
        self.assertEqual(
            LoginSerializer.ACCOUNT_DISABLED, _('User account is disabled.'))
        self.assertEqual(
            LoginSerializer.EMAIL_NOT_VERIFIED, _('E-mail is not verified.'))


class PasswordResetConfirmSerializerTests(TestCase):

    def test_error_messages(self):
        self.assertEqual(
            PasswordResetConfirmSerializer.INVALID_UID,
            {'uid': ['Invalid value']}
        )
        self.assertEqual(
            PasswordResetConfirmSerializer.INVALID_TOKEN,
            {'token': ['Invalid value']}
        )

class PasswordChangeSerializerTests(TestCase):

    def test_error_messages(self):
        self.assertEqual(
            PasswordChangeSerializer.INVALID_PASSWORD,
            _('Invalid password')
        )    
