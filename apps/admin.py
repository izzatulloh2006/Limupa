from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from apps.models import Blog, Tag , Category, Comment,User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class CustomAdmin(UserAdmin):
    list_display = ('custom_image', "username", "email", "first_name", "last_name", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Person info"), {"fields": ("first_name", "last_name", "email", 'image')}),
        (
            _("Permissions"),
            {
                'fields' : (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"),{"fields": ("last_login", "data_joined")}),

    )

    def custom_image(self, obj: User):
        return  mark_safe('<img scr="{}"/>'.format(obj.image.url))

    custom_image.short_description = "Image"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass




