import os
import numpy as np
import cv2
import shutil

dir1 = "screenShots/add&DeleteBase/"
dir2 = "screenShots/add&DeleteTest/"
dir3 = "Results/add&DeleteDiff/"
number_of_white_allowed = 2150


def clear_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.unlink(os.path.join(root, file))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


def image_checker(base_img, test_img, number):
    image_original = cv2.imread(base_img)
    image1 = cv2.imread(base_img)
    image2 = cv2.imread(test_img)

    # compute difference
    difference = cv2.subtract(image1, image2)

    # color the mask red
    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    difference[mask != 255] = [0, 0, 255]

    num_white = np.sum(difference == 255)

    if num_white > number_of_white_allowed:
        test_outcome1 = 'Fail'
        image1[mask != 255] = [0, 0, 255]
        image2[mask != 255] = [0, 0, 255]

        cv2.imwrite(dir3+'b.Fail_'+str(number)+'a'+'.png', image_original)
        cv2.imwrite(dir3+'b.Fail_'+str(number)+'b'+'.png', image2)
        cv2.imwrite(dir3+'b.Fail_'+str(number)+'c'+'.png', difference)

    else:
        test_outcome1 = 'Pass'

    value1 = num_white

    return test_outcome1, value1

# def image_checker(base_img, test_img, conf_value_threshold):
#     base_img = cv2.imread(base_img, cv2.IMREAD_REDUCED_COLOR_2)
#     test_img = cv2.imread(test_img, cv2.IMREAD_REDUCED_COLOR_2)
#
#     result = cv2.matchTemplate(base_img, test_img, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
#     print('best match = '+str(max_loc))
#     print('best match confidence = ' + str(max_val))
#
#     if max_val > conf_value_threshold:
#         test_outcome = 'Pass'
#     else:
#         test_outcome = 'Fail'
#
#     print('test_0 | screenShot_0 vs testImg_0 | ' + test_outcome)


while True:

    clear_file(dir3)

    test_list = []
    failed_test_list = []
    list1 = os.listdir(dir1)
    list2 = os.listdir(dir2)  # dir is your directory path

    print("Running comparison...")

    for i in range(0, len(list1)):
        index = 1000000+i
        img1 = dir1 + list1[i]
        img2 = dir2 + list2[i]
        test_outcome, value = image_checker(img1, img2, i)
        log = "Log"+str(index)+"| "+list1[i]+" vs "+list2[i]+" | "+test_outcome +\
              " | difference: "+str(value)
        print(log)
        test_list.append(log)

        if test_outcome == 'Fail':
            failed_test_list.append(log)

    print("")
    print("failed tests:")
    for i in range(0, len(failed_test_list)):
        print(failed_test_list[i])

    f = open('2.logsComparison.txt', 'w')
    with f:
        f.write('failed tests:\n')
        for i in range(0, len(failed_test_list)):
            f.write(failed_test_list[i] + '\n')
        f.write('\n')
        f.write('Logs: \n')
        for j in range(0, len(test_list)):
            f.write(test_list[j]+"\n")
    f.close()

    print("Comparison finished")

    break
