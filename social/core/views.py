from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile, Post, LikePost, FollowersCount

# Create your views here.
@login_required(login_url='core:login')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    
    posts = Post.objects.all()
    
    return render(request, "core/index.html", {
        "user_profile": user_profile,
        "posts": posts
    })

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('core:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                
                #log user in 
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                
                
                #create a profile object for new user & redirect to settings page
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                
                
                return redirect('core:settings')
                
                # return redirect('core:signup')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('core:signup')
    else:
        return render(request, "auth/signup.html", {})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('core:home')
        else:
            messages.info(request, "Credentials invalid")
            return redirect('core:login')
    
    return render(request, "auth/login.html", {})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('core:login')

@login_required
def settings(request):
    user = request.user.username
    user_profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
            
        return redirect('core:settings')
    
    return render(request, "core/setting.html", {
        "user": user,
        "user_profile": user_profile
    })
 
@login_required   
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES['image_upload']
        caption = request.POST['caption']
        
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        
        return redirect('core:home')
    else:
        return redirect('core:home')
    
@login_required   
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    
    post = Post.objects.get(id=post_id)
    
    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()
    
    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('core:home')
    
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('core:home')
   
@login_required
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_posts_length = len(user_posts)
    # user_follower = FollowersCount.objects.filter(user=pk).follower.count()
    
    follower = request.user.username
    user = pk
    
    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = "Follow"
     
    
    return render(request, "core/profile.html", {
        "user_profile": user_profile,
        "user_posts_length": user_posts_length,
        "user_posts": user_posts,
        # "user_follower": user_follower
        "button_text": button_text,
    })
           
@login_required(login_url='core:signup')
def follow(request):
    # follower = get_object_or_404(Profile, user=username)
    # user = User.objects.get(user=request.user.username)
    
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']
        
        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            # return redirect("core:profile", request.user.username )
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            # return redirect("core:profile", request.user.username )
            
    
    return redirect("core:home")

    
    
