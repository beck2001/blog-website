from django.shortcuts import render

posts = [
    {
        'author': 'Muratbek',
        'title': 'Blog post #1',
        'content': 'First post on this blog website',
        'date_posted': 'December 21, 2021'
    },
    {
        'author': 'Sophia',
        'title': 'Blog post #2',
        'content': 'Second post on this blog website',
        'date_posted': 'December 22, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
