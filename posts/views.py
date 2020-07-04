from django.db.models import Count
from django.core.paginator import Paginator

from django.shortcuts import (render,
                              get_object_or_404,
                              redirect,
                              reverse,)

from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment, Author
from .forms import CommentForm, PostForm


# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


class IndexView(View):
    # template_name = "index.html"
    # paginated_by = 2

    # def get_context_data(self, *args, **kwargs):
    #     featured = Post.objects.filter(featured=True)
    #     recent = Post.objects.order_by('-timestamp')[0:30]
    #     category_count = get_category_count()
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = featured,
    #     context['recent'] =recent,
    #     context['category_count'] =category_count,
    #     return context

    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        featured = Post.objects.filter(featured=True)
        recent = Post.objects.order_by('-timestamp')[0:30]
        category_count = get_category_count()
        paginator = Paginator(post, 2)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'object_list': featured,
            'recent': recent,
            'category_count': category_count,
            'page_obj': page_obj,

        }
        return render(request, "index.html", context)


class CanolaOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Canola Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class CoconutOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Coconut Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class CornOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Corn Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class CottonseedOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Cottonseed oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class OliveOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Olive Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class PalmOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Palm Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class PeanutOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Peanut Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class RapeseedOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Rapeseed Oil")

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class SunflowerOilList(ListView):
    context_object_name = 'object_list'
    template_name = 'posts/post-list.html'
    queryset = Post.objects.filter(categories__title="Sunflower Oil")
    paginate_by = 1

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]
        context = super().get_context_data(**kwargs)

        context['category_count'] = category_count
        context['recent'] = recent
        return context


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'posts/post-detail.html'
    context_object_name = 'post'
    form = CommentForm()

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        recent = Post.objects.order_by('-timestamp')[0:10]

        category = get_object_or_404(Category, id=self.kwargs['pk'])
        related_post = Post.objects.filter(categories=category)[0:24]

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        total_unlikes = stuff.total_unlikes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['category_count'] = category_count
        context['recent'] = recent
        context['related_post'] = related_post
        context['total_likes'] = total_likes
        context['total_unlikes'] = total_unlikes
        context['liked'] = liked
        return context

    def post(self, request, pk, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()

                return redirect(reverse("post-detail", kwargs={
                    'pk': post.pk
                }))
        else:
            form = CommentForm()

# class PostCategory(ListView):
#     model = Post
#     template_name = "posts/post-category.html"

#     def get_queryset(self, kwargs):
#         category = get_object_or_404(Category, pk=self.kwargs['pk'])
#         return Post.objects.filter(categories=category)

#     def get_context_data(self,  **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = category
#         return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    # unlike_post = get_object_or_404(Post, id=request.POST.get('post_unlike_id'))

    # liked = False
    # unliked = False
    # if unlike_post.unlikes.filter(id=request.user.id).exists()==False or post.likes.filter(id=request.user.id).exists():
    #     unlike_post.unlikes.add(request.user)
    #     unliked = True
    #     post.likes.remove(request.user)
    #     liked = False

    #     if post.likes.filter(id=request.user.id).exists()==False:
    #         post.likes.add(request.user)
    #         liked = True
    #         unlike_post.unlikes.remove(request.user)
    #         unliked = False

    #     else:
    #         post.likes.remove(request.user)
    #         liked = False

    # else:
    #     unlike_post.unlikes.remove(request.user)

    return HttpResponseRedirect(reverse("post-detail", args=[str(pk)]))
