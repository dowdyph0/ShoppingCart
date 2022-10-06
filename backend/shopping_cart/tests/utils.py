from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

def generate_dummy_png() -> ContentFile:
    file = BytesIO()
    image = Image.new("RGBA", size=(50,50), color=(256,0,0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return ContentFile(file.getvalue())