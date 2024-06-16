import time
import pyautogui
import ctypes
import testClassBuilder
import os
import shutil

timer_interval = 3
log_counter = 0
screenshot_count = 1000000
dir_path = r'screenShots/add&DeleteTest\test'

top_menu_click_list_x = [115, 350, 585, 820, 1055, 1290, 1525, 1760] #, 1995]
top_menu_click_list_y = [236, 236, 236, 236, 236,  236,  236,  236] #, 236]
#                          0    1    2    3    4    5    6    7    8    9    10   11
left_menu_click_list_x = [147, 147, 147, 147, 147, 147, 147, 147, 147, 147, 147, 147]
left_menu_click_list_y = [350, 399, 427, 475, 509, 547, 579, 621, 657, 690, 730, 765]

add_x = 1464
add_y = 1000
delete_x = 1652
delete_y = 1000
ok_x = 1057
ok_y = 163

programming = 12
management = 10
service = 2
reports = 11
system = 7
scheduling = 3
wvw_admin = 4
logout = 0


def clear_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.unlink(os.path.join(root, file))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(1)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    time.sleep(0.1)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)


def screen_shot_base():
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
    f = open('2.logsAdd&DeleteTest.txt', 'w')
    with f:
        for k in range(0, len(log_event_list)):
            f.write("Testlog"+str(log_event_list[k].counter)+" |"+"mouse_position"+str(log_event_list[k].mouse_x)+"," +
                    str(log_event_list[k].mouse_y)+" |screenshot_no."+str(log_event_list[k].screen_shot) + "\n")
    f.close()


while True:

    clear_file(dir_path)

    log_event_list = []

    list_of_submenus = [programming, management, service, reports, system, scheduling, wvw_admin, logout]

    for i in range(0, 3):
        print("starting in " + str(3 - i))
        time.sleep(1)

    print("Running...")

    # starting screen
    screen_shot_base()
    log_event(log_counter, 0, 0, screenshot_count - 1)

    time.sleep(timer_interval)
    click(left_menu_click_list_x[0], left_menu_click_list_y[0])
    screen_shot_base()
    log_event(log_counter, left_menu_click_list_x[0], left_menu_click_list_y[0], screenshot_count - 1)

    # programming
    for i in range(0, len(list_of_submenus)):
        time.sleep(timer_interval)
        click(top_menu_click_list_x[i], top_menu_click_list_y[i])

        for j in range(0, list_of_submenus[i]):
            if i == 1 and j == 2:
                pass
            elif i == 1 and j == 5:
                pass
            elif i == 1 and j == 9:
                pass
            elif i == 3:
                pass
            elif i == 5:
                pass
            elif i == 4 and j == 1:
                pass
            elif i == 4 and j == 3:
                pass
            elif i == 4 and j == 4:
                pass
            elif i == 4 and j == 6:
                pass
            elif i == 6 and j == 0:
                pass
            elif i == 6 and j == 2:
                pass
            elif i == 6 and j == 3:
                pass
            else:
                time.sleep(timer_interval)
                click(left_menu_click_list_x[j], left_menu_click_list_y[j])
                screen_shot_base()

                time.sleep(timer_interval)
                click(add_x, add_y)
                screen_shot_base()
                log_event(log_counter, left_menu_click_list_x[j], left_menu_click_list_y[j], screenshot_count - 1)

                time.sleep(timer_interval)
                click(delete_x, delete_y)
                screen_shot_base()
                log_event(log_counter, left_menu_click_list_x[j], left_menu_click_list_y[j], screenshot_count - 1)

                time.sleep(timer_interval)
                click(ok_x, ok_y)
                screen_shot_base()
                log_event(log_counter, left_menu_click_list_x[j], left_menu_click_list_y[j], screenshot_count - 1)

    log()
    print("finished")
    break
