from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shop
from .forms import ShopForm


from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

# CRUD -> 굉장히 많이 쓰임
# 블로그 , 쇼핑몰, --> CRUD
# 이렇게 많이 쓰여서 친절한 django = 쉽게!!!!!
# -> CRUD : class형으로 view


# def index(request):
#     all_items = Shop.objects.all()
#     # Shop 속 데이터를 몽땅 가져옴
#     return render(request, 'index.html', {'all_items': all_items})

# ListView 사용
class indexView(ListView):
    template_name = 'index.html'
    model = Shop
    context_object_name = 'all_items'


# def detail(request, item_id):
#     detail_item = Shop.objects.get(pk=item_id)
#     # 상세히 보고싶은 데이터 하나
#     return render(request, 'detail.html', {'detail_item': detail_item})

class detailView(DetailView):
    template_name = 'detail.html'
    model = Shop
    context_object_name = 'detail_item'


# def create(request):
#     if request.method == 'POST':
#         # 이용자가 form을 제출했을때~~
#         shop_form = ShopForm(request.POST)
#         if shop_form.is_valid():
#             shop_form.save()
#             return redirect('index')
#     else:
#         # 이용자가 form제출 X -> 그냥 들어왔을때~~
#         shop_form = ShopForm()

#     return render(request, 'create.html', {'shop_form': shop_form})

class createView(CreateView):
    template_name = 'create.html'
    model = Shop
    fields = '__all__'

    success_url = reverse_lazy('index')
    # redirect


# def update(request, item_id):
#     update_item = Shop.objects.get(pk=item_id)
#     # 업데이트 시키고 싶은 데이터

#     if request.method == 'POST':
#         # 이용자가 업데이트 폼을 제출하면
#         shop_form = ShopForm(request.POST, instance=update_item)
#         # shop_form에다가 업데이트 시켜주고 싶은 데이터 + 이용자가 요청한 데이터
#         if shop_form.is_valid():
#             shop_form.save()
#             return redirect('index')
#     else:
#         shop_form = ShopForm(instance=update_item)
#         # shop_form에다가 업데이트 시켜주고 싶은 데이터를 담은 것

#     return render(request, 'update.html', {'shop_form': shop_form})

class updateView(UpdateView):
    template_name = 'update.html'
    model = Shop
    fields = '__all__'

    success_url = reverse_lazy('index')


# def delete(request, item_id):
#     delete_item = Shop.objects.get(pk=item_id)
#     # 우리가 지우고 싶은 데이터 하나
#     delete_item.delete()
#     return redirect('index')

class deleteView(DeleteView):
    # template_name = 'delete.html'
    model = Shop

    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
