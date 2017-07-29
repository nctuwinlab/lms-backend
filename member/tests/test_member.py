from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve

from member.models import Profile
from member.views import user_login


class MemberLoginTest(TestCase):

    def setUp(self):
        self.username = 'lms'
        self.email = 'lms@win'
        self.password = 'password'
        self.user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.user.Profile = Profile()
        self.user.save()

    def test_resolve(self):
        match = resolve('/member/login/')
        self.assertEqual(match.func, user_login)

    def test_AccessMemberBeforeLogin(self):
        self.client.logout()
        response = self.client.get('/member/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/member/login/?next=/member/')

    def test_AccessMemberAfterLogin(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/member/')
        self.assertEqual(response.status_code, 200)
