from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostForm, AuthorForm

def post_list(request):
    """Fetch and display a list of all sticky notes."""
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """Display detailed view for a single sticky note by primary key."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    """Handle creation of a new sticky note using PostForm."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def post_update(request, pk):
    """Handle editing of an existing sticky note."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})

def post_delete(request, pk):
    """Handle deletion confirmation and removal of a sticky note."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

def author_create(request):
    """Handle creation of a new author using AuthorForm."""
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = AuthorForm()
    return render(request, 'posts/author_form.html', {'form': form})