import os
import shutil
from datetime import datetime
from io import BytesIO
from zipfile import ZipFile

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from divichildbuilder.settings import BASE_DIR
from .forms import ChildForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)

        if form.is_valid():
            request.session['child_name'] = form.cleaned_data['child_name']
            request.session['customer_name'] = form.cleaned_data['customer_name']
            request.session['customer_site'] = form.cleaned_data['customer_site']
            redirect('render_child')

    else:
        form = ChildForm()

    context = {
        'form': form,
    }
    return render(request, 'home.html', context)


def download_child(request):
    context = {
        'child_name': request.POST.get('child_name', 'DiviChild'),
        'customer_name': request.POST.get('customer_name', 'Mulher Gorila'),
        'customer_site': request.POST.get('customer_site', 'https://www.mulhergorila.com'),
    }
    byte = BytesIO()
    template_dir = os.path.abspath(BASE_DIR + '/templates/divi-child/')
    file_paths = []
    divi_child_name = context['child_name']
    divi_child_name_file = divi_child_name + '.zip'

    fs = FileSystemStorage('/tmp')
    dirname = f'{divi_child_name}-{datetime.now().strftime("%Y.%m.%d.%H.%M.%S")}'
    os.mkdir(os.path.join('/tmp', dirname))

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(template_dir):
        for filename in files:
            # Checks if file is image
            if filename.endswith(".jpg") or filename.endswith(".png"):
                shutil.copy2(f'{template_dir}/{filename}', f'/tmp/{dirname}')
            else:
                # rendering files and save in /tmp
                file_string = render_to_string(root + '/' + filename, context)
                with fs.open(f'/tmp/{dirname}/{filename}', 'w') as rendered_file:
                    rendered_file.write(file_string)

            # join the two strings in order to form the full filepath.
            filepath = os.path.join(f'/tmp/{dirname}', filename)
            file_paths.append(filepath)

    # writing files to a zipfile
    with ZipFile(byte, 'w') as zipped:
        # writing each file one by one
        for file in file_paths:
            zipped.write(file, divi_child_name + '/' + os.path.basename(file))

    zipped.close()
    shutil.rmtree(f'/tmp/{dirname}')

    response = HttpResponse(byte.getvalue(), content_type="application/x-zip-compressed")
    response['Content-Disposition'] = f'attachment; filename={divi_child_name_file}'
    return response
