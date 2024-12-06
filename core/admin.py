from django.contrib import admin

from core.models import MuscleGroup, Exercise, Training, UserProfile, TrainingExercise, Meal, MealFood, Food


@admin.register(MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass


class TrainingExerciseAdmin(admin.TabularInline):
    model = TrainingExercise
    list_display = ['id', 'training', 'exercise', 'repetitions', 'series', 'rest_time']


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [
        TrainingExerciseAdmin,
    ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'login', 'age', 'weight', 'height', 'active']


@admin.register(Food)
class MealAdmin(admin.ModelAdmin):
    pass

class MealFoodAdmin(admin.TabularInline):
    model = MealFood

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    inlines = [
        MealFoodAdmin,
    ]
