from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_Page, name = 'Index_Page'),
    
    path('signup/', views.Signup_Page, name = 'Signup_Page'),

    path('login/', views.Login_Page, name = 'Login_Page'),

    path('signup_action/', views.Signup_Action, name = 'Signup_Action'),

    path('login_action/', views.Login_Action, name = 'Login_Action'),

    path('logout/', views.Logout, name = 'Logout'),

    path('board/', views.Board_Page, name = 'Board_Page'),

    path('post_writing/', views.Post_Writing_Page, name = 'Post_Writing_Page'),

    path('post_writing_action/', views.Post_Writing_Action, name = 'Post_Writing_Action'),

    path('post_detail/<int:post_id>/', views.Post_Detail_Page, name = 'Post_Detail_Page'),

    path('myaccount/', views.Myaccount_Page, name = 'Myaccount_Page'),

    path('edit_info', views.Edit_Info, name = 'Edit_Info'),

    path('user_detail/<int:user_id>/', views.User_Detail_Page, name = 'User_Detail_Page'),

    path('delete_post/<int:post_id>', views.Delete_Post, name = 'Delete_Post'),

    path('message_box/', views.Message_Box_Page, name = 'Message_Box_Page'),

    path('message_writing/', views.Message_Writing_Page, name = 'Message_Writing_Page'),

    path('message_writing_action/', views.Message_Writing_Action, name = 'Message_Writing_Action'),

    path('message_detail/<int:message_id>/', views.Message_Detail_Page, name = 'Message_Detail_Page'),

    path('message_reply/<int:user_id>/', views.Message_Reply_Page, name = 'Message_Reply_Page'),

    path('message_delete/<int:message_id>/', views.Message_Delete, name = 'Message_Delete'),

    path('ranking/', views.Ranking_Page, name = "Ranking_Page"),

    path('shop/', views.Shop_Page, name = 'Shop_Page'),

    path('shop_buy_sword/', views.Shop_Buy_Sword, name = 'Shop_Buy_Sword'),

    path('shop_buy_shield/', views.Shop_Buy_Shield, name = 'Shop_Buy_Shield'),

    path('shop_buy_armor/', views.Shop_Buy_Armor, name = 'Shop_Buy_Armor'),

    path('shop_buy_protect_potion/', views.Shop_Buy_Protect_Potion, name = 'Shop_Buy_Protect_Potion'),

    path('shop_buy_sword_15/', views.Shop_Buy_Sword_15, name = 'Shop_Buy_Sword_15'),

    path('shop_buy_shield_15/', views.Shop_Buy_Shield_15, name = 'Shop_Buy_Shield_15'),

    path('shop_sell/<int:item_id>', views.Shop_Sell, name = 'Shop_Sell'),

    path('equipment/', views.Equipment_Page, name = 'Equipment_Page'),

    path('equip_item/<int:item_id>/', views.Equip_Item, name = 'Equip_Item'),

    path('blacksmith/', views.Blacksmith_Page, name = 'Blacksmith_Page'),

    path('blacksmith_select/<int:item_id>/', views.Blacksmith_Select, name = 'Blacksmith_Select'),

    path('blacksmith_upgrade/<int:item_id>/', views.Blacksmith_Upgrade, name = 'Blacksmith_Upgrade'),

    path('blacksmith_upgrade_loop/<int:item_id>/', views.Blacksmith_Upgrade_Loop, name = 'Blacksmith_Upgrade_Loop'),

    path('protect_potion/<int:item_id>/', views.Protect_Potion_Use, name = 'Protect_Potion_Use'),

    path('mushroom_page/', views.Mushroom_Page, name = 'Mushroom_Page'),

    path('mushroom_attack/<int:mushroom_id>/<int:total_attack>/', views.Mushroom_Attack, name = "Mushroom_Attack"),

    # 블랙잭

    path('blackjack/', views.Blackjack_Page, name = 'Blackjack_Page'),

    path('card_dealing/', views.Card_Dealing, name = 'Card_Dealing'),

    path('hit/', views.Hit, name = 'Hit'),

    path('stand/', views.Stand, name = 'Stand'),

    path('last_turn/', views.Last_Turn, name = 'Last_Turn'),

    path('restart/', views.Restart, name = 'Restart'),

    # 가위바위보

    path('rock_paper_scissors/', views.Rock_Paper_Scissors_Page, name = 'Rock_Paper_Scissors_Page'),

    path('rock_paper_scissors_play/<int:user_id>/', views.Rock_Paper_Scissors_Play, name = 'Rock_Paper_Scissors_Play'),



]
