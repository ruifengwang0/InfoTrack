from django.contrib import admin
from InfoTrack.models import UserProfile, Post, Comment


admin.site.site_header = "InfoTrack Administration"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("PostType","title",'context', 'time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('context', 'time')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'phone', 'user_info')

    def user_info(self, obj):
        return obj.description
    
    #customise object sort order in Admin Pages
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user','-location')
        return queryset
    user_info.short_description = 'Description'

admin.site.register(UserProfile,UserProfileAdmin)

