from django.core.exceptions import ValidationError
import os

def validate_picture(value):
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.jpg', '.png', '.jpeg']
	if not ext.lower() in valid_extensions:
		raise ValidationError('Неподходящий тип файла')

def validate_file(value):
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.pdf', '.doc', '.docx']
	if not ext.lower() in valid_extensions:
		raise ValidationError('Неподходящий тип файла')
