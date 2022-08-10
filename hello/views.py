from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm, EstimatorForm

import math
from scipy.optimize import minimize
#import calcs
from .calcs import calc

# Create your views here.

def index(request):
    """params = {
            'title': 'Claculation!!',
            'message': 'すべて埋めてください',
            'form': HelloForm()
        }
    if (request.method == 'POST'):
        params['message'] = '積立月額：' + '{:,}'.format(int(request.POST['amount'])) + ' 円' + \
            '<br>年利：' + request.POST['interest'] + ' ％' + \
            '<br>投資期間：' + request.POST['period'] + ' 年' + \
            '<br>投資総額：' '{:,}'.format(int(request.POST['amount']) * int(request.POST['period']) * 12) + ' 円' + \
            '<br>最終価値：' + \
                '{:,}'.format(math.floor(
                    int(request.POST['amount']) + 
                    int(request.POST['amount']) * (1+float(request.POST['interest'])/100/12) * 
                    ((1+float(request.POST['interest'])/100/12)**(int(request.POST['period'])*12-1)-1) / 
                    ((1+float(request.POST['interest'])/100/12)-1)
                    )) + ' 円'
        params['form'] = HelloForm(request.POST)"""
        
    params = {
            'title': 'Claculation!!',
            'message': 'すべて埋めてください',
            'form': EstimatorForm()
        }
    if (request.method == 'POST'):
        def func(x):
            x0=x[0]
            chk_val=(calc(monthly,x0,fulltime)-finalvalue)**2
            return chk_val

        finalvalue=int(request.POST['Finish'])
        fulltime=int(request.POST['Period'])
        monthly=int(request.POST['Monthly'])
        SimpleProfitRate=(finalvalue/(12*fulltime*monthly)-1)*100
        x0=[1.0]
        """if finalvalue<monthly*12*fulltime:
            result="損失"
            #print("減っています")
        else:"""
        results = minimize(func,x0=x0,bounds=[(-100,100)])
        result=str(math.floor(results.x[0]*100)/100)+"%"
            #print("年利",math.floor(result.x[0]*10000)/10000,"%で運用")

        params['message'] = '月' + '{:,}'.format(monthly) + '円を' + \
            '{:,}'.format(fulltime) + '年積立、' + \
            '{:,}'.format(finalvalue) + '円となった。' + \
            '<br>' + '表面上は' + str(math.floor(SimpleProfitRate*100)/100) + '%増、' + \
            '年利換算だと' + result + '運用ということ。'
        params['form'] = EstimatorForm(request.POST)

    return render(request, 'hello/index.html', params)
