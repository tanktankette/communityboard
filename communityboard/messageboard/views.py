from django.shortcuts import render, get_object_or_404
from .models import Board, Post


def board(request, slug):
    board = get_object_or_404(Board, slug=slug)
    posts = board.posts.all()
    pinned = board.posts.filter(pinned=True)

    context_dict = {'board': board,
                    'posts': posts,
                    'pinned': pinned}

    return render(request, 'messageboard/board.html', context_dict)
