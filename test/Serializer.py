from rest_framework import serializers
from .models import Award, FormApply, StudentTranscript, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email','first_name','last_name','clas','adress')
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'desc', 'price')


class FormApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormApply
        fields = ('student_id', 'award_id', 'context', 'email','status')


class StudentTranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTranscript
        fields = ('student_id','name', 'poin')

    def to_representation(self, instance):
        rep = super(StudentTranscriptSerializer, self).to_representation(instance)
        rep['name'] = instance.student_id.username
        return rep



