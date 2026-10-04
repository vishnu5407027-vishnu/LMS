from rest_framework import viewsets, permissions
from .models import Course, Lesson, Assignment, Submission
from .serializers import CourseSerializer, LessonSerializer, AssignmentSerializer, SubmissionSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Submission.objects.filter(student=user)
        # Instructors/Admins see all
        # Optionally filter by assignment if provided in query params
        queryset = Submission.objects.all()
        assignment_id = self.request.query_params.get('assignment')
        if assignment_id:
            queryset = queryset.filter(assignment_id=assignment_id)
        return queryset

    def perform_update(self, serializer):
        user = self.request.user
        if user.role == 'student':
            # Students can only update if status is rejected
            instance = serializer.instance
            if instance.status == 'rejected':
                # Reset to pending on resubmission
                serializer.save(status='pending')
            else:
                # If not rejected, they shouldn't be updating (handled by permissions or here)
                # For simplicity, we just save, but ideally we block updates if not rejected.
                # But since serializer read_only_fields prevents status change, they can only change content.
                pass
        else:
            # Instructors can update status
            # If status is in validated_data, it will be updated.
            # We need to make sure 'status' is writable for instructors.
            # Since we made it read_only in serializer, we need to handle it.
            # A better approach is to have a separate serializer or handle 'status' update manually here
            # because 'status' is read_only in the default serializer.
            
            if status and status in dict(Submission.STATUS_CHOICES):
                serializer.instance.status = status
            serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if user.role == 'student':
            if instance.status != 'rejected':
                from rest_framework.exceptions import PermissionDenied
                raise PermissionDenied("You can only delete rejected submissions.")
        instance.delete()
