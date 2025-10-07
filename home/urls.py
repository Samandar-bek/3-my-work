from django.urls import path
from . import views

urlpatterns = [
    # Asosiy sahifa
    path('', views.base_page, name='base_page'),

    # Present bo'ldi
    path('present_simple_easy.html', views.present_simple_easy, name='present_simple_easy'),
    path('present_simple_normal.html', views.present_simple_normal, name='present_simple_normal'),
    path('present_simple_hard.html', views.present_simple_hard, name='present_simple_hard'),

    path('present_continuous_easy.html', views.present_continuous_easy, name='present_continuous_easy'),
    path('present_continuous_normal.html', views.present_continuous_normal, name='present_continuous_normal'),
    path('present_continuous_hard.html', views.present_continuous_hard, name='present_continuous_hard'),

    path('present_perfect_easy.html', views.present_perfect_easy, name='present_perfect_easy'),
    path('present_perfect_normal.html', views.present_perfect_normal, name='present_perfect_normal'),
    path('present_perfect_hard.html', views.present_perfect_hard, name='present_perfect_hard'),

    path('present_perfect_cont_easy.html', views.present_perfect_cont_easy, name='present_perfect_cont_easy'),
    path('present_perfect_cont_normal.html', views.present_perfect_cont_normal, name='present_perfect_cont_normal'),
    path('present_perfect_cont_hard.html', views.present_perfect_cont_hard, name='present_perfect_cont_hard'),

    # Past
    path('past_simple_easy.html', views.past_simple_easy, name='past_simple_easy'),
    path('past_simple_normal.html', views.past_simple_normal, name='past_simple_normal'),
    path('past_simple_hard.html', views.past_simple_hard, name='past_simple_hard'),

    path('past_continuous_easy.html', views.past_continuous_easy, name='past_continuous_easy'),
    path('past_continuous_normal.html', views.past_continuous_normal, name='past_continuous_normal'),
    path('past_continuous_hard.html', views.past_continuous_hard, name='past_continuous_hard'),

    path('past_perfect_easy.html', views.past_perfect_easy, name='past_perfect_easy'),
    path('past_perfect_normal.html', views.past_perfect_normal, name='past_perfect_normal'),
    path('past_perfect_hard.html', views.past_perfect_hard, name='past_perfect_hard'),

    path('past_perfect_cont_easy.html', views.past_perfect_cont_easy, name='past_perfect_cont_easy'),
    path('past_perfect_cont_normal.html', views.past_perfect_cont_normal, name='past_perfect_cont_normal'),
    path('past_perfect_cont_hard.html', views.past_perfect_cont_hard, name='past_perfect_cont_hard'),

    # Future
    path('future_simple_easy.html', views.future_simple_easy, name='future_simple_easy'),
    path('future_simple_normal.html', views.future_simple_normal, name='future_simple_normal'),
    path('future_simple_hard.html', views.future_simple_hard, name='future_simple_hard'),

    path('future_continuous_easy.html', views.future_continuous_easy, name='future_continuous_easy'),
    path('future_continuous_normal.html', views.future_continuous_normal, name='future_continuous_normal'),
    path('future_continuous_hard.html', views.future_continuous_hard, name='future_continuous_hard'),

    path('future_perfect_easy.html', views.future_perfect_easy, name='future_perfect_easy'),
    path('future_perfect_normal.html', views.future_perfect_normal, name='future_perfect_normal'),
    path('future_perfect_hard.html', views.future_perfect_hard, name='future_perfect_hard'),

    path('clauses-reason.html', views.clauses_reason, name='clauses_reason'),
    path('clauses-purpose.html', views.clauses_purpose, name='clauses_purpose'),
    path('future_perfect_cont_easy.html', views.future_perfect_cont_easy, name='future_perfect_cont_easy'),
    path('future_perfect_cont_normal.html', views.future_perfect_cont_normal, name='future_perfect_cont_normal'),
    path('future_perfect_cont_hard.html', views.future_perfect_cont_hard, name='future_perfect_cont_hard'),
    path('clauses-result.html', views.clauses_result, name='clauses_result'),
    path('clauses-contrast.html', views.clauses_contrast, name='clauses_contrast'),
    path('conditionals.html', views.conditionals, name='conditionals'),
]
