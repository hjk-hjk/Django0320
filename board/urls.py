from django.urls  import path
from board.views import board_form,board_list,board_edit,board_delete

urlpatterns = [

path('board_list/', board_list , name='board_list' ),
path('board_edit/<int:pk>/', board_edit , name='board_edit' ),
path('board_delete/<int:pk>/', board_delete , name='board_delete' ),
path('board_form/', board_form , name='board_form' ),
]