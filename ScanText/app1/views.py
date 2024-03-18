from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .form import ImageUploadForm
from django.core.files.storage import default_storage
from django.http import JsonResponse
import pytesseract
from PIL import Image
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Create your views here.
def HomePage(request):
    return render(request,'Home.html')
def Member (request):
    if not request.user.is_authenticated:
        return redirect('Login')  # Chuyển hướng đến trang đăng nhập

    # Truy xuất thông tin người dùng từ request
    username = request.user.username

    # Render template cho trang thành viên
    context = {
        'username': username
    }#Tạo đối tượng mới context chứa username
    return render(request, 'Member.html', context)

def SignUp(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same, please check it again!")
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('Login')
    return render(request,'SignUp.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('Member')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request,'Login.html')

def Logout(request):
    logout(request)
    return redirect('Home')
def Member(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid(): #Check xem có đúng định dạng không
            image = form.cleaned_data['image']
            file_name = default_storage.save('uploads/' + image.name, image) #Lưu hình ảnh vào mục uploads(uploads nằm trong media)
            file_path = default_storage.path(file_name) #lấy link của hình ảnh đã lưu
            text = scan_image(file_path)  # Gọi hàm scan_image
            context = {'form': form, 'scanned_text': text}
    else:
        form = ImageUploadForm()
        context = {'form': form}

    return render(request, 'Member.html', context)
def scan_image(file_path):
    # Đọc ảnh bằng OpenCV
    img = cv2.imread(file_path)

    # Làm sắc nét ảnh bằng kernel Gaussian
    kernel = cv2.getGaussianKernel(3, 0)
    img = cv2.filter2D(img, -1, kernel)

    # Tăng cường độ tương phản
    alpha = 1.5  # Tăng giá trị alpha để tăng độ tương phản
    img = cv2.convertScaleAbs(img, alpha=alpha)

    # Loại bỏ nhiễu bằng bộ lọc Median
    img = cv2.medianBlur(img, 3)

    # Chuyển đổi ảnh sang định dạng PIL
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Sử dụng pytesseract để nhận diện text
    text = pytesseract.image_to_string(img_pil)

    return text
