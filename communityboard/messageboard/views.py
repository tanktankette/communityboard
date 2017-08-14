from django.shortcuts import render, get_object_or_404
from .models import Board, Post
from .forms import PostForm


def board(request, slug):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.author == '':
                post.author = 'Anon'
            post.board = Board.objects.get(slug=slug)
            post.save()
        else:
            print(form.errors)

    b = get_object_or_404(Board, slug=slug)
    posts = b.posts.all()
    pinned = b.posts.filter(pinned=True)

    context_dict = {'board': b,
                    'posts': posts,
                    'pinned': pinned,
                    'form': form}

    return render(request, 'messageboard/board.html', context_dict)
