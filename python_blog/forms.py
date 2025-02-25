import re
from django import forms
from .models import Post, Category, Tag
from django.utils.text import slugify
from unidecode import unidecode

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            'name': 'Название',
        }
        help_texts = {
            'name': 'Введите название тега',
        }
        error_messages = {
            'name': {
                'min_length': 'Название должно быть не менее 2 символов',
                'max_length': 'Название должно быть не более 200 символов',
                'required': 'Название обязательно для заполнения',
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Python',
                'id': 'tag-name'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Tag.objects.filter(name=name).exists():
            raise forms.ValidationError('Тег с таким названием уже существует')
        return name
    

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['tags_input'].initial = ', '.join(
                tag.name for tag in instance.tags.all()
            )

    
    tags_input = forms.CharField(
        label='Теги',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'django, python, разработка',
        }),
        help_text='Введите теги через запятую'
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст поста'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }

    def clean_tags_input(self):
        tags_input = self.cleaned_data.get('tags_input', '')
        
        if tags_input:
            return [tag.strip().lower() for tag in tags_input.split(',') if tag.strip()]
        return []

    def save(self, commit=True):
        # Создаем экземпляр модели, но не сохраняем его пока в БД
        post = super().save(commit=False)
        post.status = 'review'
        
        if commit:
            # Сохраняем пост один раз в БД
            post.save()
            
            # Обработка тегов
            tag_names = self.cleaned_data.get('tags_input', [])
            tags_to_add = []
            for tag_name in tag_names:
                tag_slug = slugify(unidecode(tag_name))
                tag, created = Tag.objects.get_or_create(
                    slug=tag_slug,
                    defaults={"name": tag_name}
                )
                tags_to_add.append(tag)
            if tags_to_add:
                # Добавляем все теги за один вызов, чтобы минимизировать операции записи
                post.tags.add(*tags_to_add)
                
        return post