import os
import pickle
import time
from help_files.crypto import decrypt_file, encrypt_file
from help_files.filemanagment import get_account_files_path, get_project_directory_path
from help_files.logger import log
from my_steampy_modified.client import SteamClient
from my_api_files.item import Item
from my_steampy_modified.utils import GameOptions
from time import sleep

coef_drop_48h_168h = 1.05
coef_drop_24h_72h = 1.04
coef_drop_12h_36h = 1.03
coef_boost_48h_72h = 1.03
coef_boost_48h_168h = 1.04
coef_boost_24h_48h = 1.02
coef_boost_3h_24h = 1.01
sell_hist_count_coef_for_graphic_drop = None
sell_hist_count_coef_for_graphic_boost = None
sell_hist_count_bad_coef = None
sell_hist_count_good_coef = None
steam_client_file_name_for_relogin = None
steam_client = None


def login_steam(steam_client_file_name: str = 'steam_client.pkl', account_file_name: str = 'account.json',
                steam_guard_file_name: str = 'steam_guard.json') -> None:
    """
    осуществляет вход в аккаунт стим
    :param steam_client_file_name: название файла с текущей сессией
    :param account_file_name: название файла с данными от аккаунта
    :param steam_guard_file_name: название файла с данными для steam guard
    :return: ничего
    """
    log('steam_f: login_steam')
    project_directory_path = get_project_directory_path()
    account_files_path = project_directory_path + get_account_files_path()
    global steam_client_file_name_for_relogin
    steam_client_file_name_for_relogin = steam_client_file_name
    steam_client_file_name = account_files_path + steam_client_file_name
    account_file_name = account_files_path + account_file_name
    steam_guard_file_name = account_files_path + steam_guard_file_name
    global steam_client
    if os.path.isfile(steam_client_file_name):
        steam_client = decrypt_file(steam_client_file_name)
    if steam_client.is_session_alive():
        return
    account = decrypt_file(account_file_name)
    steam_guard = decrypt_file(steam_guard_file_name)
    steam_client = SteamClient(account['apikey'])
    steam_client.login(account['steam_login'], account['steam_password'], steam_guard)
    with open(steam_client_file_name, 'wb') as f:
        pickle.dump(steam_client, f)
        encrypt_file(steam_client_file_name)


def relogin_steam(account_file_name: str = 'account.json', steam_guard_file_name: str = 'steam_guard.json') -> None:
    """
    осуществляет перезаход в аккаунт стим
    :param account_file_name: название файла с данными от аккаунта
    :param steam_guard_file_name: название файла с данными для steam guard
    :return: ничего
    """
    log('steam_f: relogin_steam')
    while True:
        try:
            login_steam(steam_client_file_name_for_relogin, account_file_name, steam_guard_file_name)
            break
        except Exception as err:
            log('steam_f: проблема в функции relogin_steam')
            log(err)
        sleep(5)


def initialize_coefs_for_get_items_actual_price() -> None:
    """
    выставляет коэффициенты для цен
    :return: ничего
    """
    global sell_hist_count_coef_for_graphic_drop
    global sell_hist_count_coef_for_graphic_boost
    global sell_hist_count_bad_coef
    global sell_hist_count_good_coef
    cur_time = time.gmtime()
    if cur_time.tm_wday == 1:
        sell_hist_count_coef_for_graphic_drop = 0.02
        sell_hist_count_coef_for_graphic_boost = 0.02
        sell_hist_count_bad_coef = 0.04
        sell_hist_count_good_coef = 0.06
        return
    if cur_time.tm_wday == 2:
        sell_hist_count_coef_for_graphic_drop = 0.01
        sell_hist_count_coef_for_graphic_boost = 0.01
        sell_hist_count_bad_coef = 0.03
        sell_hist_count_good_coef = 0.05
        return
    if cur_time.tm_wday == 3:
        if cur_time.tm_hour < 8:
            sell_hist_count_coef_for_graphic_drop = 0.01
            sell_hist_count_coef_for_graphic_boost = 0.01
            sell_hist_count_bad_coef = 0.03
            sell_hist_count_good_coef = 0.05
            return
    sell_hist_count_coef_for_graphic_drop = 0.03
    sell_hist_count_coef_for_graphic_boost = 0.03
    sell_hist_count_bad_coef = 0.05
    sell_hist_count_good_coef = 0.07


def get_steam_price_for_every_item_in_list(items_list_for_steam: list, coef: float) -> None:
    """
    вычисляет цену по которой можно продать все предметы из заданного списка
    :param items_list_for_steam: список предметов на продажу
    :param coef: коэффициент цены
    :return: ничего
    """
    log('steam_f: get_steam_price_for_every_item_in_list')
    initialize_coefs_for_get_items_actual_price()
    for item in items_list_for_steam:
        while True:
            try:
                item_price = get_item_actual_price(item)
                break
            except Exception as err:
                log('проблема в функции get_steam_price_for_every_item_in_list')
                log(err)
        item.steam_price = item_price
        item.tm_price = round(item_price * 0.87 / coef * 10)
        log(f'{item.get_name()}: {item.steam_price} : {item.tm_price}\n')


def get_item_actual_price(item: Item) -> int:
    """
    возвращает цену, по которой этот предмет нужно продавать прямо сейчас
    :param item: предмет
    :return: цена, по которой этот предмет нужно продавать прямо сейчас
    """
    log('steam_f: get_item_actual_price')
    history = get_price_history(item.get_name())
    histogram = get_item_histogram(item)
    price_graphic = round(get_item_price_graphic(history), 2)
    price_histogram = round(get_item_price_histogram(history, histogram), 2)
    max_buy_order = float(histogram['highest_buy_order']) / 100
    min_sell_order = float(histogram['lowest_sell_order']) / 100
    if price_graphic == price_histogram:
        return int(round(price_graphic * 100))
    (count_24_12_histogram, count_12_6_histogram, count_6_3_histogram,
     count_3_0_histogram) = get_count_of_price_or_higher_in_history_24_12_6_3(history, price_histogram - 0.005)
    if (count_24_12_histogram == 0 and count_12_6_histogram == 0
            and count_6_3_histogram == 0 and count_3_0_histogram == 0):
        return int(round(max(price_graphic, min_sell_order) * 100))
    if check_graphic_drop(history) or check_graphic_boost(history):
        if price_graphic < price_histogram:
            return int(round(max(price_graphic, min_sell_order) * 100))
        return int(round(price_histogram * 100))
    else:
        if price_graphic > price_histogram and price_histogram <= max_buy_order:
            return int(round(max(price_graphic, min_sell_order) * 100))

        if price_histogram > price_graphic and price_graphic <= max_buy_order:
            return int(round(price_histogram * 100))
    if price_graphic/price_histogram >= 1.07 or price_histogram / price_graphic >= 1.07:
        return int(round(min(price_histogram, max(price_graphic, min_sell_order)) * 100))
    else:
        if price_graphic > price_histogram:
            return int(round(max(price_graphic, min_sell_order) * 100))
        return int(round(price_histogram * 100))


def get_price_history(item_name: str, game_option: int = GameOptions.CS) -> list:
    """
    возвращает список цен, из которых состоит график предмета
    :param item_name: название предмета
    :param game_option: код игры
    :return: список цен, из которых состоит график предмета
    """
    log('steam_f: get_price_history')
    while True:
        try:
            tmp = steam_client.market.fetch_price_history(item_name, game=game_option)
            if tmp["success"]:
                return tmp["prices"]
        except Exception as err:
            log('steam_f: проблема в функции get_price_history')
            log(err)
            if not steam_client.is_session_alive():
                relogin_steam()

            sleep(1)


def get_item_histogram(item: Item) -> dict:
    """
    возвращает гистограмму предмета
    :param item: предмет
    :return: гистограмму предмета
    """
    log('steam_f: get_item_histogram')
    while True:
        try:
            histogram = steam_client.market.get_item_histogram(item)
            if histogram['success']:
                return histogram
        except Exception as err:
            log('steam_f: проблема в функции get_item_histogram')
            log(err)
            if not steam_client.is_session_alive():
                relogin_steam()
            sleep(2)


def get_item_price_graphic(prices: list) -> float:
    """
    проверяет есть ли дроп графика(тогда возвращает  цену за последние 2 часа), есть ли буст графика(тогда возвращает
    цену для буста), если нет дропа или буста - возвращает цену за 2 дня
    :param prices: график цен на предмет
    :return: актуальную цену предмета по графику
    """
    log('steam_f: get_item_price_graphic')
    if check_graphic_drop(prices):
        price_2h = calculate_avg_price_and_more(prices, 2)
        return price_2h
    price_7_days = calculate_avg_price_and_more(prices, 168, 72)
    price_3_days = calculate_avg_price_and_more(prices,72, 48)
    price_2_days = calculate_avg_price_and_more(prices, 48)
    if price_2_days / price_3_days >= coef_boost_48h_72h and price_2_days / price_7_days >= coef_boost_48h_168h:
        price_1_day = calculate_avg_price_and_more(prices, 24)
        if price_1_day / price_2_days >= coef_boost_24h_48h:
            price_3_hrs = calculate_avg_price_and_more(prices, 3)
            if price_3_hrs/price_1_day >= coef_boost_3h_24h:
                return price_3_hrs
            else:
                price_2_hrs = calculate_avg_price_and_more(prices, 2)
                return price_2_hrs
        else:
            price_12h = calculate_avg_price_and_more(prices, 12)
            return price_12h
    return price_2_days


def calculate_avg_price_and_more(prices: list, time_2: int,  time_1: int = 0) -> float:
    """
    считает среднюю цену в промежутке от time_1 до time_2, после этого считает среднюю цену в промежутке от time_1 до
    time_2, но включает только те точки, которые принадлежат от price_average до price_average * highest_price_coef
    :param prices: график цен на предмет
    :param time_2: конец промежутка времени
    :param time_1: начало промежутка времени
    :return: цена предмета по графику
    """
    log('steam_f: calculate_avg_price_and_more')
    res = 0
    count = 0
    for i in range(time_1, time_2):
        res += prices[-1 - i][1] * int(prices[-1 - i][2])
        count += int(prices[-1 - i][2])
    price_average = res / count
    res = 0
    count = 0
    highest_price_coef = 1.2
    for i in range(time_1, time_2):
        if price_average <= prices[-1 - i][1] <= price_average * highest_price_coef:
            res += prices[-1 - i][1] * int(prices[-1 - i][2])
            count += int(prices[-1 - i][2])
    if count > 0:
        return res / count
    return price_average


def check_graphic_drop(prices: list) -> bool:
    """
    проверяет график на дроп цены
    :param prices: график цен на предмет
    :return: есть дроп графика или нет
    """
    log('steam_f: check_graphic_drop')
    price1 = calculate_avg_price_and_more(prices, 168, 48)
    price2 = calculate_avg_price_and_more(prices, 48)
    if price1 / price2 >= coef_drop_48h_168h:
        return True
    price1 = calculate_avg_price_and_more(prices, 72, 24)
    price2 = calculate_avg_price_and_more(prices, 24)
    if price1 / price2 >= coef_drop_24h_72h:
        return True
    price1 = calculate_avg_price_and_more(prices, 36, 12)
    price2 = calculate_avg_price_and_more(prices, 12)
    if price1 / price2 >= coef_drop_12h_36h:
        return True
    return False


def check_graphic_boost(prices: list) -> bool:
    """
    проверяет график на буст цены
    :param prices: график цен на предмет
    :return: есть буст графика или нет
    """
    log('steam_f: check_graphic_boost')
    price_7_days = calculate_avg_price_and_more(prices, 168, 72)
    price_3_days = calculate_avg_price_and_more(prices, 72, 48)
    price_2_days = calculate_avg_price_and_more(prices, 48)
    if price_2_days / price_3_days >= coef_boost_48h_72h and price_2_days / price_7_days >= coef_boost_48h_168h:
        return True
    return False


def get_item_price_histogram(prices: list, histogram: dict):
    """
    проверяет дроп графика(если он есть, то возвращает цену из гистограммы для дропа графика), иначе возвращает цену
    из гистограммы, по которой можно продать предмет
    :param prices: график цен на предмет
    :param histogram: гистограмма предмета
    :return: цену, по которой можно продать предмет, если судить по гистограмме
    """
    log('steam_f: get_item_price_histogram')
    sell_orders_list = get_item_sell_orders_list(histogram)
    item_sell_count_for_week = calculate_item_sell_count(prices, 168)
    item_sell_count_for_day = int(item_sell_count_for_week / 7)
    if check_graphic_drop(prices):
        sell_count_for_drop_coef = int(sell_hist_count_coef_for_graphic_drop * item_sell_count_for_day)
        counter = 0
        for i in range(len(sell_orders_list)):
            cur_counter = sell_orders_list[i]['count']
            counter += cur_counter
            if counter >= sell_count_for_drop_coef:
                if i == 0:
                    if counter > sell_count_for_drop_coef:
                        return sell_orders_list[i]['price'] - 0.01
                    else:
                        return sell_orders_list[i]['price']
                else:
                    return sell_orders_list[i - 1]['price']
    if check_graphic_boost(prices):
        sell_count_for_boost_coef = int(sell_hist_count_coef_for_graphic_boost * item_sell_count_for_day)
        counter = 0
        for i in range(len(sell_orders_list)):
            cur_counter = sell_orders_list[i]['count']
            counter += cur_counter
            if counter >= sell_count_for_boost_coef:
                if i == 0:
                    if counter > sell_count_for_boost_coef:
                        return sell_orders_list[i]['price'] - 0.01
                    else:
                        return sell_orders_list[i]['price']
                else:
                    return sell_orders_list[i - 1]['price']
    max_buy_order = int(histogram['highest_buy_order']) / 100
    sell_price_bad = 0
    sell_price_good = 0
    sell_count_bad = int(sell_hist_count_bad_coef * item_sell_count_for_day)
    sell_count_good = int(sell_hist_count_good_coef * item_sell_count_for_day)
    counter = 0
    for i in range(len(sell_orders_list)):
        cur_counter = sell_orders_list[i]['count']
        counter += cur_counter
        if counter >= sell_count_bad:
            if i == 0:
                if counter > sell_count_bad:
                    sell_price_bad = sell_orders_list[i]['price'] - 0.01
                    break
                else:
                    sell_price_bad = sell_orders_list[i]['price']
                    break
            else:
                sell_price_bad = sell_orders_list[i - 1]['price']
                break
    counter = 0
    for i in range(len(sell_orders_list)):
        cur_counter = sell_orders_list[i]['count']
        counter += cur_counter
        if counter >= sell_count_good:
            if i == 0:
                if counter > sell_count_good:
                    sell_price_good = sell_orders_list[i]['price'] - 0.01
                    break
                else:
                    sell_price_good = sell_orders_list[i]['price']
                    break
            else:
                sell_price_good = sell_orders_list[i - 1]['price']
                break
    if sell_price_bad / max_buy_order < 1.04 and sell_price_good / max_buy_order < 1.06:
        return sell_price_good
    else:
        return sell_price_bad


def get_item_sell_orders_list(histogram: dict) -> list:
    """
    возвращает лист запросов на продажу
    :param histogram: гистограмма предмета
    :return: список, каждый элемент которого содержит цену и кол-во предметов, проданых по этой цене
    """
    log('steam_f: get_item_sell_orders_list')
    sell_orders = histogram['sell_order_graph']
    res_list = list()
    pre_count = 0
    for item_sell_orders in sell_orders:
        count = item_sell_orders[1]
        res_count = count - pre_count
        pre_count = count
        res_object = {'price': item_sell_orders[0], 'count': res_count}
        res_list.append(res_object)
    return res_list


def calculate_item_sell_count(prices: list, time_2: int,  time_1: int = 0) -> int:
    """
    возвращает кол-во продаж по графику за время от time_1 до time_2
    :param prices: график цен на предмет
    :param time_2: конец промежутка времени
    :param time_1: начало промежутка времени
    :return: кол-во продаж за время от time_1 до time_2
    """
    log('steam_f: calculate_item_sell_count')
    count = 0
    for i in range(time_1, time_2):
        count += int(prices[-1 - i][2])
    return count


def get_count_of_price_or_higher_in_history_24_12_6_3(prices: list, price: float) -> tuple:
    """
    вызывает функцию parse_count_of_price_or_higher_in_history для промежутков времени с 12 до 24 часов,
    с 6 до 12, с 3 до 6 часов и с до 3 часов и возвращает значение этой функции для каждого промежутка времени
    :param prices: график цен на предмет
    :param price: заданная цена
    :return: кортеж из количества продаж предмета
    """
    log('steam_f: get_count_of_price_or_higher_in_history_24_12_6_3')
    count_12h_24h = parse_count_of_price_or_higher_in_history(prices, price, 24, 12)
    count_6h_12h = parse_count_of_price_or_higher_in_history(prices, price, 12, 6)
    count_3h_6h = parse_count_of_price_or_higher_in_history(prices, price, 6, 3)
    count_3h = parse_count_of_price_or_higher_in_history(prices, price, 3)
    return count_12h_24h, count_6h_12h, count_3h_6h, count_3h


def parse_count_of_price_or_higher_in_history(prices: list, price: float, time_2: int,  time_1: int = 0) -> int:
    """
    возвращает кол-во продаж на графике по цене >= заданной
    :param prices: график цен на предмет
    :param price: заданная цена
    :param time_2: конец промежутка времени
    :param time_1: начало промежутка времени
    :return: кол-во продаж на графике по цене >= заданной
    """
    log('steam_f: parse_count_of_price_or_higher_in_history')
    count = 0
    for i in range(time_1, time_2):
        if prices[-1 - i][1] >= price:
            count += int(prices[-1 - i][2])
    return count