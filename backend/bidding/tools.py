from io import BytesIO

from django.core.files import File
from django.core.files.base import ContentFile

from PIL import Image


class ResizeImageMixin:
    def resize(self, image_field, size):
        image = Image.open(image_field)
        source_image = image.convert('RGB')
        source_image.thumbnail(size)
        output = BytesIO()
        source_image.save(output, format='JPEG')
        output.seek(0)

        content_file = ContentFile(output.read())
        file = File(content_file)

        old_file_name = image_field.name.rsplit('.')
        new_file_name = ''.join(name_part for name_part in old_file_name[:-1])

        output_name = f'{new_file_name}_thumbnail.jpg'
        image_field.save(output_name, file, save=False)
