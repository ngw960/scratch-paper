from django.shortcuts import render, redirect
from asdf.models import Users, Posts, Messages, Inventory_Equipment, Inventory_Consumable
from asdf.models import Mushrooms, Dealer, Card_Pool, Drawn_Card
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Max
from django.urls import reverse
from urllib.parse import urlencode



def Index_Page(request):
    dictionary = {
        'trigger_index' : 'x'
    }

    return render(request, "integration.html", dictionary)



def Signup_Page(request):
    dictionary = {
        'trigger_signup' : 'x'
    }

    return render(request, "integration.html", dictionary)



def Login_Page(request):
    dictionary = {
        'trigger_login' : 'x'
    }

    return render(request, "integration.html", dictionary)



def Signup_Action(request):
    # 입력받은 값 정의
    var_user_id = request.POST.get('input_user_id')
    var_password = request.POST.get('input_password')
    var_name = request.POST.get('input_name')
    var_email = request.POST.get('input_email')

    # 빈 필드가 없는지 검증
    if var_user_id and var_password and var_name and var_email:

        # 입력받은 아이디, 이메일이 db에 존재하는지 검증
        if Users.objects.filter(user_id = var_user_id).exists():
            return redirect('Signup_Page')

        if Users.objects.filter(email = var_email).exists():
            return redirect('Signup_Page')

        # db에 입력받은 유저 정보 저장
        Users.objects.create(
            user_id = var_user_id,
            password = var_password,
            name = var_name,
            email = var_email
        )

        return redirect('Login_Page')

    else:
        return redirect('Signup_Page')


def Login_Action(request):
    # 입력받은 값 정의
    var_user_id = request.POST.get('input_user_id')
    var_password = request.POST.get('input_password')

    # 빈 필드가 없는지 검증
    if var_user_id and var_password:

        select_user = Users.objects.filter(user_id = var_user_id).first()

        if select_user:

            if select_user.password == var_password:
                # 사용자를 로그인한다
                login(request, select_user)

                return redirect('Index_Page')

            else:
                return redirect('Login_Page')

        else:
            return redirect('Login_Page')



def Logout(request):
    request.session.flush()

    return redirect('Index_Page')



@login_required
def Board_Page(request):
    posts_object = Posts.objects.all()

    dictionary = {
        'trigger_board' : 'x',
        'posts' : posts_object
    }

    return render(request, 'integration.html', dictionary)




def Post_Writing_Page(request):
    var_name = request.user.name

    dictionary = {
        'trigger_post_writing' : 'x',
        'name' : var_name
    }

    return render(request, 'integration.html', dictionary)



def Post_Writing_Action(request):
    var_title = request.POST.get('input_title')
    var_content = request.POST.get('input_content')
    var_author = request.POST.get('input_author')
    user_object = Users.objects.get(id = request.user.id)

    if var_title and var_content:

        Posts.objects.create(
            title = var_title,
            content = var_content,
            author = var_author,
            user = user_object
        )

    else:
        return redirect('Post_Writing_Page')

    return redirect('Board_Page')



def Post_Detail_Page(request, post_id):
    post_object = Posts.objects.get(id = post_id)

    dictionary = {
        'trigger_post_detail' : 'x',
        'post' : post_object
    }

    return render(request, 'integration.html', dictionary)



@login_required
def Myaccount_Page(request):
    var_posts = request.user.posts.all()

    dictionary = {
        'trigger_myaccount' : 'x',
        'posts' : var_posts
    }

    return render(request, 'integration.html', dictionary)



def Edit_Info(request):
    var_name = request.POST.get('input_name')

    if var_name:

        if Users.objects.filter(name = var_name).exists():

            return redirect('Myaccount_Page')

        else:
            user = Users.objects.filter(id = request.user.id).first()
            user.name = var_name
            user.save()

            return redirect('Myaccount_Page')

    else:
        return redirect('Myaccount_Page')



def User_Detail_Page(request, user_id):
    user_object = Users.objects.get(id = user_id)

    dictionary = {
        'trigger_user_detail' : 'x',
        'user' : user_object
    }

    return render(request, 'integration.html', dictionary)



def Delete_Post(request, post_id):
    post_object = Posts.objects.get(id = post_id)
    post_object.delete()

    return redirect('Board_Page')



@login_required
def Message_Box_Page(request):
    user_object = request.user
    messages_object = Messages.objects.all()
    sent_messages = Messages.objects.filter(user = user_object)

    dictionary = {
        'trigger_message_box' : 'x',
        'messages' : messages_object,
        'sent_messages' : sent_messages
    }

    return render(request, 'integration.html', dictionary)



def Message_Writing_Page(request):
    dictionary = {
        'trigger_message_writing' : 'x'
    }

    return render(request, 'integration.html', dictionary)



def Message_Writing_Action(request):
    var_recipient = request.POST.get('input_recipient')
    var_title = request.POST.get('input_title')
    var_content = request.POST.get('input_content')
    user_object = Users.objects.get(id = request.user.id)

    if var_recipient and var_title and var_content:

        if Users.objects.filter(user_id = var_recipient).exists():

            Messages.objects.create(
                recipient = var_recipient,
                title = var_title,
                content = var_content,
                user = user_object
            )

            return redirect('Message_Box_Page')

        else:
            return redirect('Message_Writing_Page')

    else:
        return redirect('Message_Writing_Page')



def Message_Detail_Page(request, message_id):
    message_object = Messages.objects.get(id = message_id)

    dictionary = {
        'trigger_message_detail' : 'x',
        'message' : message_object
    }

    return render(request, 'integration.html', dictionary)



def Message_Reply_Page(request, user_id):
    user_object = Users.objects.get(id = user_id)

    dictionary = {
        'trigger_message_reply' : 'x',
        'user' : user_object
    }

    return render(request, 'integration.html', dictionary)



def Message_Delete(request, message_id):
    message_object = Messages.objects.get(id = message_id)
    message_object.delete()

    return redirect('Message_Box_Page')



@login_required
def Ranking_Page(request):
    user_rankings = Users.objects.annotate(
        highest_item_level = Max('inventory_equipment__item_level')
    ).order_by('-highest_item_level')

    #강화레벨이 가장 높은 'sword'를 소유하고 있는 유저 순서대로 정렬
    result = {}
    Users_ = Users.objects.all()
    for user in Users_:
        item = Inventory_Equipment.objects.filter(user = user, category = 'sword').order_by('-item_level').first()

        if item:
            result[user.name] = item.item_level
        else:
            result[user.name] = 0

    rankings = sorted(result.items(), key=lambda x : x[1], reverse=True)

    dictionary = {
        'trigger_ranking': 'x',
        'user_rankings': user_rankings,
        'rankings' : rankings
    }

    return render(request, 'integration.html', dictionary)


@login_required
def Shop_Page(request):
    user_object = request.user
    items_object = Inventory_Equipment.objects.filter(user = user_object).order_by('-item_level')

    dictionary = {
        'trigger_shop' : 'x',
        'user' : user_object,
        'items' : items_object
    }

    return render(request, 'integration.html', dictionary)



def Shop_Buy_Sword(request):
    user_object = request.user

    if user_object.money >= 1000:
        user_object.money -= 1000
        user_object.save()
    else:
        return redirect('Shop_Page')

    Inventory_Equipment.objects.create(
        user = user_object,
        category = 'sword',
        item_name = '검',
        item_attack = 10
    )

    return redirect('Shop_Page')



def Shop_Buy_Shield(request):
    user_object = request.user

    if user_object.money >= 1000:
        user_object.money -= 1000
        user_object.save()
    else:
        return redirect('Shop_Page')

    Inventory_Equipment.objects.create(
        user = user_object,
        category = 'shield',
        item_name = '방패',
        item_defense = 10
    )

    return redirect('Shop_Page')



def Shop_Buy_Armor(request):
    user_object = request.user

    if user_object.money >= 1000:
        user_object.money -= 1000
        user_object.save()
    else:
        return redirect('Shop_Page')

    Inventory_Equipment.objects.create(
        user = user_object,
        category = 'armor',
        item_name = '갑옷',
        item_health = 100
    )

    return redirect('Shop_Page')



def Shop_Buy_Protect_Potion(request):
    user_object = request.user

    if user_object.money >= 1000000:
        user_object.money -= 1000000
        user_object.save()
    else:
        return redirect('Shop_Page')

    Inventory_Consumable.objects.create(
        user = user_object,
        item_name = 'Protect_Potion'
    )

    return redirect('Shop_Page')



def Shop_Buy_Sword_15(request):
    user_object = request.user

    if user_object.money >= 5000000:
        user_object.money -= 5000000
        user_object.save()
    else:
        return redirect('Shop_Page')

    Inventory_Equipment.objects.create(
        user = user_object,
        category = 'sword',
        item_name = '검',
        item_level = 15,
        item_attack = 163840,
        value = 1638400,
        upgrade_cost = 43000,
        probability = 40
    )

    return redirect('Shop_Page')



def Shop_Buy_Shield_15(request):
    user_object = request.user

    if user_object.money >= 5000000:
        user_object.money -= 5000000
        user_object.save()
    else:
        return redirect('Shop_Page')

    Inventory_Equipment.objects.create(
        user = user_object,
        category = 'shield',
        item_name = '방패',
        item_level = 15,
        item_defense = 150,
        value = 163840,
        upgrade_cost = 43000,
        probability = 40
    )

    return redirect('Shop_Page')



def Shop_Sell(request, item_id):
    user_object = request.user

    sell_item = Inventory_Equipment.objects.get(id = item_id)
    sell_item.delete()

    user_object.money += sell_item.value
    user_object.save()

    return redirect('Shop_Page')



@login_required
def Equipment_Page(request):
    user_object = request.user
    items_object = Inventory_Equipment.objects.filter(user = user_object).order_by('-item_level')
    equipped_sword = Inventory_Equipment.objects.filter(user = user_object, category = 'sword', equip = True).first()
    equipped_shield = Inventory_Equipment.objects.filter(user = user_object, category = 'shield', equip = True).first()
    equipped_armor = Inventory_Equipment.objects.filter(user = user_object, category = 'armor', equip = True).first()

    if equipped_sword:
        user_attack = user_object.attack + equipped_sword.item_attack
    else:
        user_attack = user_object.attack

    if equipped_shield:
        user_defense = user_object.defense + equipped_shield.item_defense
    else:
        user_defense = user_object.defense

    if equipped_armor:
        user_health = user_object.health + equipped_armor.item_health
    else:
        user_health = user_object.health

    dictionary = {
        'trigger_equipment' : 'x',
        'user' : user_object,
        'items' : items_object,
        'equipped_sword' : equipped_sword,
        'equipped_shield' : equipped_shield,
        'equipped_armor' : equipped_armor,
        'user_attack' : user_attack,
        'user_defense' : user_defense,
        'user_health' : user_health
    }

    return render(request, 'integration.html', dictionary)



def Equip_Item(request, item_id):
    user_object = request.user
    select_item_object = Inventory_Equipment.objects.get(id = item_id)

    if select_item_object.category == 'sword':
        select_item_object.equip = True
        select_item_object.save()

        sword_objects = Inventory_Equipment.objects.filter(user = user_object, category = 'sword')
        sword_objects.exclude(id = item_id).update(equip = False)

    elif select_item_object.category == 'shield':
        select_item_object.equip = True
        select_item_object.save()

        shield_objects = Inventory_Equipment.objects.filter(user = user_object, category = 'shield')
        shield_objects.exclude(id = item_id).update(equip = False)

    elif select_item_object.category == 'armor':
        select_item_object.equip = True
        select_item_object.save()

        armor_objects = Inventory_Equipment.objects.filter(user = user_object, category = 'armor')
        armor_objects.exclude(id = item_id).update(equip = False)


    return redirect('Equipment_Page')



@login_required
def Blacksmith_Page(request):
    user_object = request.user
    equipment_items = Inventory_Equipment.objects.filter(user = user_object).order_by('-item_level')
    Number_of_protection_potions = Inventory_Consumable.objects.filter(user = user_object).count()
    selected_item = equipment_items.filter(upgrade_select = True).first()

    dictionary = {
        'trigger_blacksmith' : 'x',
        'user' : user_object,
        'equipment_items' : equipment_items,
        'Number_of_protection_potions' : Number_of_protection_potions,
        'selected_item' : selected_item
    }

    return render(request, 'integration.html', dictionary)



def Blacksmith_Select(request, item_id):
    user_object = request.user
    selected_item = Inventory_Equipment.objects.filter(id = item_id).first()
    selected_item.upgrade_select = True
    selected_item.save()

    equipment_items = Inventory_Equipment.objects.filter(user = user_object)
    equipment_items.exclude(id = item_id).update(upgrade_select = False)

    return redirect('Blacksmith_Page')



def Blacksmith_Upgrade(request, item_id):
    user_object = request.user
    upgrade_item = Inventory_Equipment.objects.filter(id=item_id).first()

    if not upgrade_item:
        return JsonResponse({'error': '아이템을 찾을 수 없습니다.'})

    upgrade_cost = upgrade_item.upgrade_cost
    random_int = random.randint(1, 100)

    if user_object.money < upgrade_cost:
        return JsonResponse({'error': '소지금이 부족합니다.'})

    user_object.money -= upgrade_cost
    user_object.save()

    destroyed = False

    # probability = upgrade_item.probability + add_probability

    # 강화 성공
    if random_int <= upgrade_item.probability:
        upgrade_item.item_level += 1

        if upgrade_item.category == 'sword':
            upgrade_item.item_attack *= 2
        elif upgrade_item.category == 'shield':
            upgrade_item.item_defense += 10
        elif upgrade_item.category == 'armor':
            upgrade_item.item_health += 100

        upgrade_item.value *= 2
        upgrade_item.upgrade_cost += 3000
        if upgrade_item.probability > 40:
            upgrade_item.probability -= 5

        upgrade_item.save()

    else:  # 강화 실패
        if upgrade_item.item_level > 1:
            upgrade_item.item_level -= 1

        if upgrade_item.item_level >= 19:
            if upgrade_item.protected:
                upgrade_item.protected = False
            else:
                upgrade_item.delete()
                destroyed = True  # 아이템이 파괴됨

        if not destroyed:
            if upgrade_item.category == 'sword':
                upgrade_item.item_attack /= 2
            elif upgrade_item.category == 'shield':
                upgrade_item.item_defense -= 10
            elif upgrade_item.category == 'armor':
                upgrade_item.item_health -= 10

            upgrade_item.value /= 2
            upgrade_item.upgrade_cost -= 3000
            if upgrade_item.item_level <= 11:
                upgrade_item.probability += 5

            upgrade_item.save()

    if destroyed:
        return JsonResponse({'destroyed': True})
    # if upgrade_item.category == 'sword' else None,

    return JsonResponse({
        'new_money': user_object.money,
        'item_category' : upgrade_item.category,
        'item_level': upgrade_item.item_level,
        'item_attack': upgrade_item.item_attack,
        'item_defense' : upgrade_item.item_defense,
        'item_health' : upgrade_item.item_health,
        'value': upgrade_item.value,
        'probability': upgrade_item.probability,
        'upgrade_cost': upgrade_item.upgrade_cost,
        'destroyed': destroyed,
        'protected': upgrade_item.protected
    })




def Blacksmith_Upgrade_Loop(request, item_id):
    while True:
        upgrade_item = Inventory_Equipment.objects.filter(id=item_id).first()

        if upgrade_item:
            print(f"현재 아이템 레벨: {upgrade_item.item_level}, 유저 돈: {request.user.money}")  # 현재 아이템 레벨과 유저 돈 로그 출력

            # 강화 비용이 충분한지 체크
            if request.user.money <= upgrade_item.upgrade_cost:
                print("돈이 부족하여 강화할 수 없습니다.")  # 돈 부족 로그 출력
                break

            if upgrade_item.item_level < 20:
                Blacksmith_Upgrade(request, item_id)  # 강화 시도
            else:
                print("아이템 레벨이 20에 도달했습니다.")  # 레벨이 20에 도달했을 때 로그 출력
                break
        else:
            print("아이템이 존재하지 않습니다.")  # 아이템이 없을 때 로그 출력
            break

    return redirect('Blacksmith_Page')



def Protect_Potion_Use(request, item_id):
    user_object = request.user
    protect_potion = Inventory_Consumable.objects.filter(user = user_object).first()
    protect_potion.delete()

    target_item = Inventory_Equipment.objects.filter(id = item_id).first()
    target_item.protected = True
    target_item.save()

    return redirect('Blacksmith_Page')



@login_required
def Mushroom_Page(request):
    mushrooms = Mushrooms.objects.all()
    user_object = request.user
    user_attack = Users.objects.filter(id = user_object.id).first().attack
    equip_item = Inventory_Equipment.objects.filter(user = user_object, category = 'sword', equip = True).first()
    if equip_item is not None:
        item_attack = equip_item.item_attack
    else:
        item_attack = 0
    total_attack = user_attack + item_attack


    dictionary = {
        'trigger_mushroom' : 'x',
        'user' : user_object,
        'mushrooms' : mushrooms,
        'total_attack' : total_attack,
        'equip_item' : equip_item
    }

    return render(request, 'integration.html', dictionary)



@csrf_exempt
def Mushroom_Attack(request, mushroom_id, total_attack):
    user_object = request.user
    mushroom = Mushrooms.objects.filter(id=mushroom_id).first()

    if request.method == 'POST':
        if mushroom_id == 1:
            if mushroom.health <= total_attack:
                user_object.money += 1000
                user_object.save()
                mushroom.health = 100  # 초기화
                mushroom.save()
            else:
                mushroom.health -= total_attack
                mushroom.save()

        elif mushroom_id == 2:
            if mushroom.health <= total_attack:
                user_object.money += 3000
                user_object.save()
                mushroom.health = 1000
                mushroom.save()
            else:
                mushroom.health -= total_attack
                mushroom.save()

        elif mushroom_id == 3:
            if mushroom.health <= total_attack:
                user_object.money += 10000
                user_object.save()
                mushroom.health = 10000
                mushroom.save()
            else:
                mushroom.health -= total_attack
                mushroom.save()

        elif mushroom_id == 4:
            if mushroom.health <= total_attack:
                user_object.money += 25000
                user_object.save()
                mushroom.health = 1000000
                mushroom.save()
            else:
                mushroom.health -= total_attack
                mushroom.save()

        elif mushroom_id == 5:
            if mushroom.health <= total_attack:
                user_object.money += 50000
                user_object.save()
                mushroom.health = 50000000
                mushroom.save()
            else:
                mushroom.health -= total_attack
                mushroom.save()

    # 상태 업데이트만 반환
    return JsonResponse({'new_money': user_object.money, 'new_health': mushroom.health})



@login_required
def Blackjack_Page(request):
    dealer_object = Dealer.objects.filter(name = 'dealer').first()
    player_object = request.user

    dealer_turns = dealer_object.turns

    dealer_cards = Drawn_Card.objects.filter(dealer = dealer_object)
    dealer_hand_total = sum(Drawn_Card.objects.filter(dealer = dealer_object).values_list('number', flat = True))

    player_cards = Drawn_Card.objects.filter(user = player_object)
    player_hand_total = sum(Drawn_Card.objects.filter(user = player_object).values_list('number', flat = True))

    result_message = request.GET.get('result_message')

    dictionary = {
        'trigger_blackjack' : 'x',
        'dealer_turns' : dealer_turns,
        'dealer_cards' : dealer_cards,
        'player_cards' : player_cards,
        'player_hand_total' : player_hand_total,
        'dealer_hand_total' : dealer_hand_total,
        'result_message' : result_message
    }
    return render(request, 'integration.html', dictionary)



def Card_Dealing(request):
    dealer_object = Dealer.objects.filter(name = 'dealer').first()
    player_object = request.user

    dealer_object.turns += 1
    dealer_object.save()

    shuffled_cards = Card_Pool.objects.order_by('?')
    dealer_card = shuffled_cards.filter(cards_dealt = False).first()
    dealer_card.cards_dealt = True
    dealer_card.save()

    Drawn_Card.objects.create(
        dealer = dealer_object,
        number = dealer_card.number
    )

    player_card = shuffled_cards.filter(cards_dealt = False).first()
    player_card.cards_dealt = True
    player_card.save()

    Drawn_Card.objects.create(
        user = player_object,
        number = player_card.number
    )

    return redirect('Blackjack_Page')



def Hit(request):
    player_object = request.user

    shuffled_cards = Card_Pool.objects.filter(cards_dealt = False).order_by('?')
    hit_card = shuffled_cards.first()
    hit_card.cards_dealt = True
    hit_card.save()

    # player_hand_total = sum(Drawn_Card.objects.filter(user = player_object).values_list('number', flat = True))
    # if player_hand_total > 21:
    #     result_message = '패배했습니다.'

    Drawn_Card.objects.create(
        user = player_object,
        number = hit_card.number
    )

    return redirect('Blackjack_Page')



def Stand(request):
    dealer_object = Dealer.objects.filter(name = 'dealer').first()
    dealer_object.turns += 1
    dealer_object.save()

    return redirect('Blackjack_Page')



def Last_Turn(request):
    dealer_object = Dealer.objects.filter(name = 'dealer').first()
    dealer_hand_total = sum(Drawn_Card.objects.filter(dealer = dealer_object).values_list('number', flat = True))
    player_object = request.user
    player_hand_total = sum(Drawn_Card.objects.filter(user = player_object).values_list('number', flat = True))
    shuffled_cards = Card_Pool.objects.filter(cards_dealt = False).order_by('?')
    drawn_card_number = shuffled_cards.first().number

    if dealer_hand_total < 17:
        Drawn_Card.objects.create(
            dealer = dealer_object,
            number = drawn_card_number
        )

        dealer_object.turns += 1
        dealer_object.save()
    else:
        dealer_object.turns += 1
        dealer_object.save()

    if dealer_hand_total and player_hand_total < 22:
        if dealer_hand_total > player_hand_total:
            result_message = '딜러 승'
        elif dealer_hand_total == player_hand_total:
            result_message = '무승부'
        else:
            result_message = '플레이어 승'
    elif dealer_hand_total > 21:
        result_message = '플레이어 승'
    else:
        result_message = '딜러 승'

    dictionary = {
        'result_message' : result_message,
    }

    query_string = urlencode(dictionary)
    url = reverse('Blackjack_Page') + '?' + query_string

    return redirect(url)



def Restart(request):
    dealer_object = Dealer.objects.filter(name = 'dealer').first()
    dealer_object.turns = 0
    dealer_object.save()
    Drawn_Card.objects.all().delete()
    Card_Pool.objects.filter(cards_dealt = True).update(cards_dealt = False)

    return redirect('Blackjack_Page')



@login_required
def Rock_Paper_Scissors_Page(request):

    user_object = request.user
    user_choice = request.GET.get('user_choice')
    dealer_choice = request.GET.get('dealer_choice')
    result_message = request.GET.get('result_message')

    dictionary = {
        'trigger_rps' : 'x',
        'user' : user_object,
        'user_choice' : user_choice,
        'dealer_choice' : dealer_choice,
        'result_message' : result_message
    }

    return render(request, 'integration.html', dictionary)



def Rock_Paper_Scissors_Play(request,user_id):
    user_choice = request.GET.get('user_choice')
    user_object = Users.objects.filter(id = user_id).first()

    dealer_dice = random.randint(1, 3)
    if dealer_dice == 1:
        dealer_choice = '가위'
    elif dealer_dice == 2:
        dealer_choice = '바위'
    elif dealer_dice == 3:
        dealer_choice = '보'

    if user_choice == '가위':
        if dealer_choice == '가위':
            result_message = '비겼습니다.'
        elif dealer_choice == '바위':
            result_message = '졌습니다.'
        elif dealer_choice == '보':
            result_message = '이겼습니다. 5000원 획득!'
            user_object.money += 5000
            user_object.save()
    elif user_choice == '바위':
        if dealer_choice == '가위':
            result_message = '이겼습니다. 5000원 획득!'
            user_object.money += 5000
            user_object.save()
        elif dealer_choice == '바위':
            result_message = '비겼습니다.'
        elif dealer_choice == '보':
            result_message = '졌습니다.'
    elif user_choice == '보':
        if dealer_choice == '가위':
            result_message = '졌습니다.'
        elif dealer_choice == '바위':
            result_message = '이겼습니다. 5000원 획득!'
            user_object.money += 5000
            user_object.save()
        elif dealer_choice == '보':
            result_message = '비겼습니다.'

    dictionary = {
        'user_choice' : user_choice,
        'dealer_choice' : dealer_choice,
        'result_message' : result_message
    }

    query_string = urlencode(dictionary)
    url = reverse('Rock_Paper_Scissors_Page') + '?' + query_string

    return redirect(url)





