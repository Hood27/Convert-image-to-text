# app1/forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.FileField(
        label='Select a file',
        widget=forms.FileInput(attrs={
            'onchange': 'document.getElementById("image-filename").value = this.value.replace("C:\\fakepath\\", "")',
        })#Loại bỏ đường dẫn giả
    )#CHo phép user chọn 1 tệp để tải lên

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
    #Hàm khởi tạo cho class
