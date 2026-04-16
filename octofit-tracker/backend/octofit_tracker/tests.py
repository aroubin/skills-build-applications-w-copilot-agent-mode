from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')
    def test_user_creation(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(email='batman@dc.com', name='Batman', team=team)
        self.assertEqual(str(user), 'batman@dc.com')
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')
    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=team)
        workout = Workout.objects.create(name='Squats', description='Do squats', difficulty='Medium')
        activity = Activity.objects.create(user=user, workout=workout, duration=30)
        self.assertEqual(str(activity), 'ironman@marvel.com - Squats')
    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'spiderman@marvel.com: 100')
