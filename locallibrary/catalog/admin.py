from django.contrib import admin

from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
# Define the admin class
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    class AuthorAdmin(admin.ModelAdmin):
     
        list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    pass
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'display_genre')
        inlines = [BooksInstanceInline]
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
        

    pass
def display_genre(self):
    """
    Creates a string for the Genre. This is required to display genre in Admin.
    """
    return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
display_genre.short_description = 'Genre'


