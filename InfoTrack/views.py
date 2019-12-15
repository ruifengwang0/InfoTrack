from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from InfoTrack.forms import EditProfileForm,RegistrationForm,PostForm, CommentForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import User, Comment, Post,UserProfile

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('InfoTrack:homepage'))
    else:
        form = RegistrationForm()
    args = {"form":form}
    return render(request, 'accounts/reg_form.html',args)

@login_required
def viwe_profile(request):
    args = {"user": request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method =="POST":
        ###pass user object by instance= request.user
        #change from userchangeform to EditProfileForm
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('InfoTrack:view_profile'))
    else:
        form = EditProfileForm(instance = request.user)
        args = {"form":form}
        return render(request,"accounts/edit_profile.html",args)

def change_password(request):
    if request.method =="POST":
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            ###log_in and stay in the session even change the password
            update_session_auth_hash(request, form.user)
            return redirect(reverse('InfoTrack:view_profile'))
        else:
            return redirect(reverse('InfoTrack:change_password'))
    else:
        form = PasswordChangeForm(user = request.user)
        args = {"form":form}
        return render(request,"accounts/change_password.html",args)

@login_required
def clubinfo(request):
    try:
        posts = Post.objects.filter(PostType='clubinfo').order_by('-time')[:6]
        latests = Post.objects.all().order_by('-time')[:5]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    args ={ 
        'posts0' : posts[0],
        'posts1' : posts[1],
        'posts2' : posts[2],
        'posts3' : posts[3],
        'posts4' : posts[4],
        'posts5' : posts[5],

        'latests0' : latests[0],
        'latests1' : latests[1],
        'latests2' : latests[2],
        'latests3' : latests[3],
        'latests4' : latests[4]
        }
    return render(
        request,
        'sections/clubinfo.html',
        args
        )

@login_required
def courseinfo(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        posts = Post.objects.filter(PostType='courseinfo').order_by('-time')[:6]
        latests = Post.objects.all().order_by('-time')[:5]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    args ={ 
        'posts0' : posts[0],
        'posts1' : posts[1],
        'posts2' : posts[2],
        'posts3' : posts[3],
        'posts4' : posts[4],
        'posts5' : posts[5],

        'latests0' : latests[0],
        'latests1' : latests[1],
        'latests2' : latests[2],
        'latests3' : latests[3],
        'latests4' : latests[4]
        }
    return render(
        request,
        'sections/courseinfo.html',
        args
        )

@login_required
def freeride(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        posts = Post.objects.filter(PostType='lookforride').order_by('-time')[:6]
        latests = Post.objects.all().order_by('-time')[:5]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    args ={ 
        'posts0' : posts[0],
        'posts1' : posts[1],
        'posts2' : posts[2],
        'posts3' : posts[3],
        'posts4' : posts[4],
        'posts5' : posts[5],

        'latests0' : latests[0],
        'latests1' : latests[1],
        'latests2' : latests[2],
        'latests3' : latests[3],
        'latests4' : latests[4]
        }
    return render(
        request,
        'sections/freeride.html',
        args
        )
@login_required
def privatetutor(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        posts = Post.objects.filter(PostType='tutor').order_by('-time')[:6]
        latests = Post.objects.all().order_by('-time')[:5]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    args ={ 
        'posts0' : posts[0],
        'posts1' : posts[1],
        'posts2' : posts[2],
        'posts3' : posts[3],
        'posts4' : posts[4],
        'posts5' : posts[5],

        'latests0' : latests[0],
        'latests1' : latests[1],
        'latests2' : latests[2],
        'latests3' : latests[3],
        'latests4' : latests[4]
        }
    return render(
        request,
        'sections/privatetutor.html',
        args
        )

@login_required
def rentinfo(request):
    # Render the HTML template index.html with the data in the context variable
    try:
        posts = Post.objects.filter(PostType='rent').order_by('-time')[:6]
        latests = Post.objects.all().order_by('-time')[:5]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    args ={ 
        'posts0' : posts[0],
        'posts1' : posts[1],
        'posts2' : posts[2],
        'posts3' : posts[3],
        'posts4' : posts[4],
        'posts5' : posts[5],

        'latests0' : latests[0],
        'latests1' : latests[1],
        'latests2' : latests[2],
        'latests3' : latests[3],
        'latests4' : latests[4]
        }
    return render(
        request,
        'sections/rentinfo.html',
        args
        )

'''
New Functions Below:
'''

@login_required
def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        post_page = paginator.page(1)
    except EmptyPage:
        post_page = paginator.page(paginator.num_pages)
    return render(request, 'posts/post_list.html', {'posts': post_page})

@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    user = post.user
    comments = Comment.objects.filter(post=pk).order_by('-time')
    paginator = Paginator(comments, 3)
    page = request.GET.get('page')
    try:
        comment_page = paginator.page(page)
    except PageNotAnInteger:
        comment_page = paginator.page(1)
    except EmptyPage:
        comment_page = paginator.page(paginator.num_pages)
    args = {'post': post,
    'user': user,
    'comments': comment_page}
    return render(request, 'posts/post_detail.html', args)
 
@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.time = timezone.now()
            post.user = request.user
            post.save()
            return redirect('InfoTrack:post_detail', pk=post.pk)       
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})

@login_required
def post_search(request):
    if request.method == 'GET':
        keyword = request.GET.get('search_box', None)
        if not keyword:
            return redirect('InfoTrack:post_list')
        posts = Post.objects.filter(Q(context__contains = keyword) | Q(title__contains = keyword))
        #posts = Post.objects.filter(context__contains = keyword)
        paginator = Paginator(posts, 4)
        page = request.GET.get('page')
        try:
            post_page = paginator.page(page)
        except PageNotAnInteger:
            post_page = paginator.page(1)
        except EmptyPage:
            post_page = paginator.page(paginator.num_pages)
        return render(request, 'posts/post_list.html', {'posts': post_page})


@login_required
def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.time = timezone.now()
            comment.user = request.user
            comment.save()
            return redirect('InfoTrack:post_detail', pk=comment.post.pk)       
    else:
        form = CommentForm()
    return render(request, 'posts/add_comment.html', {'form': form})


def homepage(request):
    #return render(request,"accounts/test_form.html")
    #return render(request,"posts/postlist.html")
    return render(request,"homepage.html")

def test(request):
    return render(request,"base_test.html")

####################################################
#The following functionalities are left to test
####################################################
from friendship.models import Friend, Follow,FriendshipRequest
from django.conf import settings
try:
    from django.contrib.auth import get_user_model
    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
    user_model = User

from django.shortcuts import get_object_or_404
from friendship.exceptions import AlreadyExistsError

# def friend_list(request, username):
#     user = User.objects.get(username=username)
#     friends = Friend.objects.friends(user)
#     return render(request, 'friends/friends_list.html', {
#         'friends': friends
#     }
#     )
get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')
get_friendship_context_object_list_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME', 'users')


def view_friends(request, username, template_name='friendship/friend/user_list.html'):
    """ View the friends of a user """
    user = get_object_or_404(user_model, username=username)
    friends = Friend.objects.friends(user)
    return render(request, template_name, {
        get_friendship_context_object_name(): user,
        'friendship_context_object_name': get_friendship_context_object_name()
    })


def friendship_request_list(request):
    """ View unread and read friendship requests """
    # friendship_requests = Friend.objects.requests(request.user)
    friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True)
    #print(friendship_requests)
    return render(request, 'friends/requests_list.html', {'requests': friendship_requests})

@login_required
def friendship_add_friend(request, to_username):
    """ Create a FriendshipRequest """
    ctx = {'to_username': to_username}

    if request.method == 'POST':
        to_user = user_model.objects.get(username=to_username)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            ctx['errors'] = ["%s" % e]
        else:
            return redirect('friendship_request_list')

    return render(request, 'friends/add.html', ctx)
