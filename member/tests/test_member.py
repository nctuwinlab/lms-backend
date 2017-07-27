from django.test import TestCase
from django.core.urlresolvers import resolve

from member.views import user_login

class MemberLoginTest(TestCase):
    def test_resolve(self):
        match = resolve('/member/login/')
        self.assertEqual(match.func, user_login)

