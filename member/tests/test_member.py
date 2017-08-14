from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase

from member.models import Profile, Position, Grade


class MemberManageTest(APITestCase):

    def setUp(self):
        # Super User's Login Crendential
        self.super_credential = {
            'username': 'lms',
            'password': 'password'
        }

        # Regular User's Login Credential
        self.regular_credential = {
            'username': 'test',
            'password': 'tset'
        }

        # Regular User's Data
        self.userdata = {
            "user": {
                "username": "test",
                "email": "test@winlab.tw",
                "first_name": "Win",
                "last_name": "Lab"
            },
            "grade": 1,
            "position": 1,
            "github": "nctuwinlab",
            "student_id": "0123456",
            "birth": "2017-07-31",
            "mobile": "0987654321",
            "website": "https://win.cs.nctu.edu.tw",
            "address": "No.1001, Daxue Rd., Hsinchu City 300, Taiwan",
            "telphone": ""
        }

        # Super User's Data
        self.superuserdata = {
            "user": {
                "username": "lms",
                "email": "lms@winlab.tw",
                "first_name": "Administrator",
                "last_name": "WinLab"
            },
            "grade": 1,
            "position": 1,
            "github": "",
            "student_id": "0000000",
            "birth": "2017-07-30",
            "mobile": "0987654321",
            "website": "https://win.cs.nctu.edu.tw",
            "address": "No.1001, Daxue Rd., Hsinchu City 300, Taiwan",
            "telphone": ""
        }

        # Create Position
        position = Position.objects.create(
            name='Network Administrator'
        )
        position.save()

        # Create Grade
        grade = Grade.objects.create(
            name='Freshman'
        )
        grade.save()

        # Create a SuperUser
        superuser = User.objects.create_superuser(
            email='lms@winlab.tw',
            first_name='Administrator',
            last_name='WinLab',
            **self.super_credential
        )

        superuserdata = self.superuserdata.copy()

        for key in ['user', 'grade', 'position']:
            superuserdata.pop(key)

        superuser.profile = Profile(
            user=superuser, grade=grade, position=position, **superuserdata
        )

        superuser.save()
        superuser.profile.save()

        # Initialize client
        self.client = APIClient()

    def test_CreateRegularUser(self):
        self.client.login(**self.super_credential)

        # Create Regular User
        response = self.client.post('/member/profile/',
                                    data=self.userdata, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, self.userdata)

    def test_GetUserProfile(self):
        self.client.login(**self.super_credential)

        response = self.client.get('/member/profile/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.superuserdata)

    def test_UpdateUserProfile(self):
        self.client.login(**self.super_credential)

        response = self.client.get('/member/profile/',
                                   data=self.superuserdata, format='json')

        self.assertEqual(response.data, self.superuserdata)

        self.superuserdata['website'] = 'https://winlab.tw'
        response = self.client.put('/member/profile/',
                                   data=self.superuserdata, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.superuserdata)
