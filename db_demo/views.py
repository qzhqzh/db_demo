from django.shortcuts import render
from rest_framework.validators import ValidationError
import os
from django.contrib.auth.models import User
from core.models import Primer
from db_demo.funs import generate_random_strings
from db_demo.settings import project_dir


def db_demo(request):
    return render(request, 'index.html')


def search_primer(request):
    context = {}
    username = request.GET.get('user', '')
    if username:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # raise ValidationError('%s 用户不存在' %username)
            context['error_msg'] = '%s 用户不存在' %username
            return render(request, 'search-primer.html', context)
        context['primer_data'] = Primer.objects.filter(submitter=user).values('fp', 'rp')
        return render(request, 'search-primer-result.html', context)
    return render(request, 'search-primer.html')


def cal_primer(request):
    context = {}
    nc_rna = request.GET.get('nc_rna', '')
    if nc_rna:

        # Valiadation
        for c in nc_rna:
            if c not in 'ATCGUatcgu':
                context['error_msg'] = '%s 只能含有ATCGUatcgu' % nc_rna
                return render(request, 'cal-primer.html', context)

        # cmd
        outfile = os.path.join(project_dir, 'software', 'temp',
                               generate_random_strings())
        software = os.path.join(project_dir, 'software', 'cal.py')
        cmd = 'python %s %s %s' % (software, nc_rna, outfile)

        if os.system(cmd) :
            # raise Exception('%s 命令执行失败' %cmd)
            context['error_msg'] = '%s 命令执行失败' % cmd
            return render(request, 'cal-primer.html', context)

        with open(outfile, encoding='utf-8')as fh:
            result = fh.read()
        context['result'] = result
        return render(request, 'cal-primer-result.html', context)
    return render(request, 'cal-primer.html')
