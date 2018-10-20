# -*- coding:UTF-8 -*-
from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView
from .models import Picture
from django.http import HttpResponse
from django.shortcuts import render
#import numpy as np
#import sys,os
#caffe_root = '/home/xuan/caffe/caffe/' #指定根目录
#django_root = '/home/xuan/anaconda2/envs/python27/' #指定根目录
#sys.path.insert(0, caffe_root + 'python')
#import caffe
#os.chdir(caffe_root) #改变当前工作路径到指定路径
# Create your views here.

class PicList(ListView):
    queryset = Picture.objects.all().order_by('-date')

    #listview默认context
    context_object_name='latest_picture_list'
class PicDetail(DetailView):
    model = Picture


    #def get_context_data(self, **kwargs):
    #context = super().get_context_data(**kwargs)
    #context['now'] = 'hello'
    #return context


#def my (request):
 #   if request.method == 'POST':  # 是否为post请求
  #          ans={}
   #         ans['head'] = 'hello world'
    #        return render(request,'templates/picture_detail.html', ans)
    #else:
     #   return render(request, 'templates/picture_detail.html')

    #def whichstyle(request):
        #if request.method == "POST":
            #if uf.is_valid():
                # { % csrf_token %}
                #dir = django_root + 'test03/media/mypictures'  # 保存测试图片的集合
                #filelist = []
                #filenames = os.listdir(dir)
                #for fn in filenames:
                #   fullfilename = os.path.join(dir, fn)
                #   filelist.append(fullfilename)
                #for i in range(0, len(filelist)):
                #   img = filelist[i]
                #    datalist = [Test(img)]
                #return render(request, 'result.html', {'datalist': datalist})
                #return  httpResponse(u"你好")
    #def Test(img):
        #caffe_root = '/home/xuan/caffe/caffe/'
        #deploy = caffe_root + 'test1/deploy.prototxt'  # 结构文件
        #caffe_model = caffe_root + 'test1/N_worship_iter_40000.caffemodel'  # 训练模型
        #mean_file = caffe_root + 'test1/worship_resize_mean.npy'  # 均值文件
        # 加载模型
        #net = caffe.Net(deploy, caffe_model, caffe.TEST)
        # 加载输入和配置预处理
        #transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})  # 设定图片的shape格式(1,3,28,28)
        #transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))  # 减去均值，前面训练模型时没有减均值，就不用减
        #transformer.set_transpose('data', (2, 0, 1))  # 改变维度的顺序，由原始图片(28,28,3)变为(3,28,28)
        #transformer.set_channel_swap('data', (2, 1, 0))  # 交换通道，将图片由RGB变为BGR
        #transformer.set_raw_scale('data', 255.0)  # 缩放到【0，255】之间

        # 注意可以调节预处理批次的大小
        # 由于是处理一张图片，所以把原来的10张的批次改为1
        #net.blobs['data'].reshape(1, 3, 227, 227)
        # 加载图片到数据层
        #im = caffe.io.load_image(img)
        #net.blobs['data'].data[...] = transformer.preprocess('data', im)

        # 前向计算
        #out = net.forward()

        # 预测分类
        #print
        #out['prob'].argmax()

        # 打印预测标签
        #labels = np.loadtxt(caffe_root + 'test1/label.txt', str, delimiter='\t')  # 类别名称文件，将数字标签转换回类别名称
        #top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]  # 取出最后一层（Softmax）属于某个类别的概率值，并打印

        #return labels[top_k]

class PicUpload(CreateView):
    model = Picture
    fields = ['title','image']
