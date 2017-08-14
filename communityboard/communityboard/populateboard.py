import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'communityboard.settings')
import django

django.setup()
from messageboard.models import Board, Post
from tasklist.models import Task
from datetime import date


def populate():
    pages = {
        'Board 1': [
            {'author': 'Nick', 'text': 'Post1'},
            {'author': 'Some person', 'text': 'Post3'},
            {'author': 'Who knows', 'text': 'Post4'},
            {'author': 'Not me', 'text': 'Post5'},
        ],
        'Board 2': [
            {'author': 'Someone different', 'text': 'Post2'},
            {'author': 'Unknown', 'text': 'Post6'},
            {'author': 'A mystery', 'text': 'Post8'},
            {'author': 'Nick', 'text': 'Post7'},
        ]}

    tasks = ['wash dishes', 'sweep', 'take out trash']

    for title, posts in pages.items():
        b = add_board(title)
        for p in posts:
            add_post(b, p['text'], p['author'])
    # Print out the categories we have added.
    for b in Board.objects.all():
        for p in b.posts.all():
            print("- {0} - {1}".format(str(b), str(p)))

    for t in tasks:
        add_task(t)


def add_task(name):
    t = Task.objects.create(name=name, completed=False, due_date=date.today())
    t.save()
    return t


def add_post(board, text, author):
    p = Post.objects.create(board=board, text=text, author=author)
    p.save()
    return p


def add_board(name):
    b = Board.objects.get_or_create(title=name)[0]
    for p in b.posts.all():
        p.delete()
    b.save()
    return b


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
