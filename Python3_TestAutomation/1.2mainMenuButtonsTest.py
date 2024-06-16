import time
import pyautogui
import ctypes
import testClassBuilder
import shutil
import os

log_counter = 0
screenshot_count = 1000000
dir_path = r'screenShots/mainMenuButtonsTest\test'


def clear_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.unlink(os.path.join(root, file))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)


def screen_shot_test():
    global screenshot_count
    screen_shot = pyautogui.screenshot(region=(0, 71, 1920, 938))
    screen_shot.save(dir_path+str(screenshot_count)+'.png')
    screenshot_count = screenshot_count+1


def log_event(log_counter_int, mouse_x, mouse_y, screenshot_counter):
    log_created = testClassBuilder.Event(log_counter_int, mouse_x, mouse_y, screenshot_counter)
    log_event_list.append(log_created)
    global log_counter
    log_counter = log_counter+1


def log():
    f = open('1.logsTest.txt', 'w')
    with f:
        for k in range(0, len(log_event_list)):
            f.write("Testlog"+str(log_event_list[k].counter)+" |"+"mouse_position"+str(log_event_list[k].mouse_x)+"," +
                    str(log_event_list[k].mouse_y)+" |screenshot_no."+str(log_event_list[k].screen_shot) + "\n")
    f.close()


while True:

    clear_file(dir_path)

    log_event_list = []

    top_menu_click_list_x = [115, 350, 585, 820, 1055, 1290, 1525, 1760] # , 1995]
    top_menu_click_list_y = [236, 236, 236, 236, 236,  236,  236,  236] # , 236]
#                              0    1    2    3    4    5    6    7    8    9    10   11
    left_menu_click_list_x = [147, 147, 147, 147, 147, 147, 147, 147, 147, 147, 147, 147]
    left_menu_click_list_y = [350, 399, 427, 475, 509, 547, 579, 621, 657, 690, 730, 765]

    programming = 12
    management = 10
    service = 2
    reports = 11
    system = 7
    scheduling = 3
    wvw_admin = 5
    logout = 0

    list_of_submenus = [programming, management, service, reports, system, scheduling, wvw_admin] # , logout]

    for i in range(0, 3):
        print("starting in " + str(3-i))
        time.sleep(1)

    print("Running...")

    # starting screen
    screen_shot_test()
    log_event(log_counter, 0, 0, screenshot_count-1)

    time.sleep(3)

    click(left_menu_click_list_x[0], left_menu_click_list_y[0])
    time.sleep(3)
    screen_shot_test()
    log_event(log_counter, left_menu_click_list_x[0], left_menu_click_list_y[0], screenshot_count - 1)

    # programming
    for i in range(0, len(list_of_submenus)):
        click(top_menu_click_list_x[i], top_menu_click_list_y[i])
        time.sleep(3)
        screen_shot_test()
        log_event(log_counter, top_menu_click_list_x[i], top_menu_click_list_y[i], screenshot_count-1)

        for j in range(0, list_of_submenus[i]):

            if i == 6 and j == 4:
                time.sleep(20)

            click(left_menu_click_list_x[j], left_menu_click_list_y[j])
            time.sleep(3)
            screen_shot_test()
            log_event(log_counter, left_menu_click_list_x[j], left_menu_click_list_y[j], screenshot_count-1)

    log()
    print("Finished")
    break



