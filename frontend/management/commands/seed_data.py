from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from courses.models import Course, Lesson, Assignment
from django.utils import timezone
import datetime

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create Instructor
        instructor, created = User.objects.get_or_create(
            username='instructor_demo',
            defaults={
                'email': 'inst@example.com',
                'role': 'instructor'
            }
        )
        if created:
            instructor.set_password('demo1234')
            instructor.save()

        # Create Student
        student, created = User.objects.get_or_create(
            username='student_demo',
            defaults={
                'email': 'student@example.com',
                'role': 'student'
            }
        )
        if created:
            student.set_password('demo1234')
            student.save()

        # Create Course
        course, _ = Course.objects.get_or_create(
            title='Python Programming 101',
            instructor=instructor,
            defaults={'description': 'Learn Python from scratch with this beginner-friendly course.'}
        )

        # Create Lesson
        Lesson.objects.get_or_create(
            course=course,
            title='Introduction to Python',
            defaults={'content': 'In this lesson, we cover variables, data types, and basic syntax.', 'order': 1}
        )

        # Create Assignment
        Assignment.objects.get_or_create(
            course=course,
            title='Build a Calculator',
            defaults={
                'description': 'Create a simple calculator that can add, subtract, multiply, and divide.',
                'due_date': timezone.now() + datetime.timedelta(days=7)
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
        self.stdout.write(self.style.SUCCESS('Demo User: student_demo / demo1234'))
        self.stdout.write(self.style.SUCCESS('Demo Instructor: instructor_demo / demo1234'))
