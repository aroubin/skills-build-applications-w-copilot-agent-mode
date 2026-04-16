from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy'),
            Workout.objects.create(name='Squats', description='Do squats', difficulty='Medium'),
            Workout.objects.create(name='Running', description='Go for a run', difficulty='Hard'),
        ]

        # Activities
        Activity.objects.create(user=users[0], workout=workouts[0], duration=30)
        Activity.objects.create(user=users[1], workout=workouts[1], duration=45)
        Activity.objects.create(user=users[2], workout=workouts[2], duration=60)
        Activity.objects.create(user=users[3], workout=workouts[0], duration=25)
        Activity.objects.create(user=users[4], workout=workouts[1], duration=35)
        Activity.objects.create(user=users[5], workout=workouts[2], duration=50)

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=120)
        Leaderboard.objects.create(user=users[1], score=110)
        Leaderboard.objects.create(user=users[2], score=130)
        Leaderboard.objects.create(user=users[3], score=140)
        Leaderboard.objects.create(user=users[4], score=100)
        Leaderboard.objects.create(user=users[5], score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
