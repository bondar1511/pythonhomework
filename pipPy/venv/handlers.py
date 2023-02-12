import random
from aiogram import types
from loader import dp
max_count = 150
total = 0
new_game = False
duel = []
first = 0
current = 0
@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'{name} Добро пожаловать в нашу игру!! Для того чтобы начать игру необходимо написать /new_game. ' 
                        f'{name} для настройки количества конфет /set. {name} удачи в игре!! ')
    print(message.from_user.id)
@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global new_game
    global total
    global max_count
    new_game = True
    total = max_count
    first = random.randint(0,1)
    if first:
     await message.answer(f' Игра началась. По жребию первым ходит {message.from_user.first_name}')
    else:
        await message.answer(f' Игра началась. По жребию первым ходит Бот')
        await bot_turn(message)

@dp.message_handler(commands=['duel'])
async def mes_duel(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global current
    duel.append(int(message.from_user.id))
    duel.append(int(message.text.split()[1]))
    total = max_count
    first = random.randint(0,1)
    if first:
     await dp.bot.send_message(duel[0], 'Первый ход за тобой бери конфеты')
     await dp.bot.send_message(duel[1], 'Первый ход за твоим противником! Жди своего хода')
     
    else:
      await dp.bot.send_message(duel[1], 'Первый ход за тобой бери конфеты')
      await dp.bot.send_message(duel[0], 'Первый ход за твоим противником! Жди своего хода')
  
    current = duel[0] if first else duel[1] 
    new_game = True

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global max_count
    global new_game
    name = message.from_user.first_name
    count = message.text.split()[1]
    if not new_game:
       if count.isdigit():
           max_count= int(count)
           await message.answer(f'Конфет теперь будет {max_count} ')  
       else:
           await message.answer(f'{name}, в данной игре используются только цифры')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры')

@dp.message_handler()
async def mes_take_candy(message: types.Message):
    global total
    global new_game
    global max_count
    global duel
    global first
    name = message.from_user.first_name
    count = message.text
    if len(duel) == 0:
     if new_game:
       if message.text.isdigit() and 0 < int(message.text) < 29:
          total -= int(message.text)
          if total<=0:
            await message.answer(f'{name}, в данной игре ты одержал победу!')
            new_game = False
        
          else:
            await message.answer(f'{name} взял {message.text} конфет. '
                             f'На столе осталось, {total}')
            await bot_turn(message)
       
       else:
           await message.answer(f'{name}, надо указать число о 1 до 28')
    else:
        
     if current == int(message. from_user.id):
       name = message.from_user.first_name
       count = message.text
       if new_game:
        print('Взял конфеты')
        if message.text.isdigit() and 0 < int(message.text) < 29:
          total -= int(message.text)
          if total<=0:
            await message.answer(f'{name}, в данной игре ты одержал победу!')
            await dp.bot.send_message(enemy_id(), 'К сожалению  ты проиграл! Твой оппонент выиграл!!')
            new_game = False
        
          else:
            await message.answer(f'{name} взял {message.text} конфет. '
                             f'На столе осталось, {total}')
            await dp.bot.send_message(enemy_id(), 'Теперь твой ход, бер конфеты')
            switch_players()
        else:
            await message.answer(f'{name}, надо указать число от 1 до 28')

async def bot_turn(message: types.Message):
    global total
    global new_game
    bot_take = 0
    if 0 < total <29:
     bot_take = total
     total -= bot_take
     await message.answer(f'Бот взял {bot_take} конфет. '
                        f'На столе осталось, {total} и бот одержал победу')
     new_game = False
     total = 150
    else:
     remainder = total%29
     bot_take = remainder if remainder !=0 else 28
     total -= bot_take
     await message.answer(f'Бот взял {bot_take} конфет. '
                            f'На столе осталось, {total}')


def switch_players():
    global duel
    global current
    
    if current == duel[0]:
       current = duel[1]
    else:
       current = duel[0]

def enemy_id():
    global duel
    global current
    if current == duel[0]:
        return duel[1]
    else:
       return duel[0]
      
