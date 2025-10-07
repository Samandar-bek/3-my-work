from django.shortcuts import render

# Asosiy sahifa
def base_page(request):
    return render(request, 'index.html')

# Present
def present_simple_easy(request): return render(request, 'present_simple_easy.html')
def present_simple_normal(request): return render(request, 'present_simple_normal.html')
def present_simple_hard(request): return render(request, 'present_simple_hard.html')

def present_continuous_easy(request): return render(request, 'present_continuous_easy.html')
def present_continuous_normal(request): return render(request, 'present_continuous_normal.html')
def present_continuous_hard(request): return render(request, 'present_continuous_hard.html')

def present_perfect_easy(request): return render(request, 'present_perfect_easy.html')
def present_perfect_normal(request): return render(request, 'present_perfect_normal.html')
def present_perfect_hard(request): return render(request, 'present_perfect_hard.html')

def present_perfect_cont_easy(request): return render(request, 'present_perfect_cont_easy.html')
def present_perfect_cont_normal(request): return render(request, 'present_perfect_cont_normal.html')
def present_perfect_cont_hard(request): return render(request, 'present_perfect_cont_hard.html')

# Past
def past_simple_easy(request): return render(request, 'past_simple_easy.html')
def past_simple_normal(request): return render(request, 'past_simple_normal.html')
def past_simple_hard(request): return render(request, 'past_simple_hard.html')

def past_continuous_easy(request): return render(request, 'past_continuous_easy.html')
def past_continuous_normal(request): return render(request, 'past_continuous_normal.html')
def past_continuous_hard(request): return render(request, 'past_continuous_hard.html')

def past_perfect_easy(request): return render(request, 'past_perfect_easy.html')
def past_perfect_normal(request): return render(request, 'past_perfect_normal.html')
def past_perfect_hard(request): return render(request, 'past_perfect_hard.html')

def past_perfect_cont_easy(request): return render(request, 'past_perfect_cont_easy.html')
def past_perfect_cont_normal(request): return render(request, 'past_perfect_cont_normal.html')
def past_perfect_cont_hard(request): return render(request, 'past_perfect_cont_hard.html')

# Future
def future_simple_easy(request): return render(request, 'future_simple_easy.html')
def future_simple_normal(request): return render(request, 'future_simple_normal.html')
def future_simple_hard(request): return render(request, 'future_simple_hard.html')

def future_continuous_easy(request): return render(request, 'future_continuous_easy.html')
def future_continuous_normal(request): return render(request, 'future_continuous_normal.html')
def future_continuous_hard(request): return render(request, 'future_continuous_hard.html')

def future_perfect_easy(request): return render(request, 'future_perfect_easy.html')
def future_perfect_normal(request): return render(request, 'future_perfect_normal.html')
def future_perfect_hard(request): return render(request, 'future_perfect_hard.html')

def future_perfect_cont_easy(request): return render(request, 'future_perfect_cont_easy.html')
def future_perfect_cont_normal(request): return render(request, 'future_perfect_cont_normal.html')
def future_perfect_cont_hard(request): return render(request, 'future_perfect_cont_hard.html')

def clauses_reason(request):return render(request, 'clauses-reason.html')

def clauses_reason(request):
    return render(request, 'clauses-reason.html')
def clauses_contrast(request):
    return render(request, 'clauses-contrast.html')


def clauses_purpose(request):
    return render(request, 'clauses-purpose.html')

def clauses_result(request):
    return render(request, 'clauses-result.html')

def conditionals(request):
    return render(request, 'conditionals.html')

from django.conf import settings
from django.conf.urls.static import static