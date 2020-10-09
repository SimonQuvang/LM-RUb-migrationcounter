import pyautogui
import time
import cv2
import numpy as np
import pytesseract
import csv
numberOne = [1240, 445];
numberTwo = [1360, 445];
numberThree = [1490, 445];
numberFour = [1240, 530];
numberFive = [1360, 530];
numberSix = [1490, 530];
numberSeven = [1240, 630];
numberEight = [1360, 630];
numberNine = [1490, 630];
numberZero = [1260, 700];

searchKingdomPos = [870, 160];
kingdomPos = [750, 395];
acceptKingdomNumber = [1500, 720];
goButton = [930, 545];
migrateButton = [825, 500]
closeButton = [1430, 130]
migrate_button_pos = [700, 470, 900, 520]
migrate = [1100, 910, 1370, 955]
monster_hunt = [966, 640, 1260, 700]
monster_hunt_close = [1765, 94]


def resize(resized_image, scale):
    resized_image_width = int(resized_image.shape[1] * scale / 100)
    resized_image_height = int(resized_image.shape[0] * scale / 100)
    resized_image = cv2.resize(resized_image, (resized_image_width, resized_image_height))
    return resized_image


def screen_image_processing(image):
    # making image grey because thats better for reasons
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)

    # Adding blur to remove noise and make the text more clear
    # blur = cv2.GaussianBlur(gray, (3, 3), 0)
    blur = cv2.medianBlur(opening, 3)

    # Basic OTSU threshold example
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    invert = 255 - thresh

    return invert


def screen_to_text(coords):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = image[coords[1]:coords[3], coords[0]:coords[2]]

    image = resize(image, 400)
    image = screen_image_processing(image)
    cv2.imwrite('open_image.png', image)
    txt_open = pytesseract.image_to_string(image)

    print(txt_open)
    return txt_open


def loop_kingdoms(numbers):
    for item in numbers:
        time.sleep(0.5)
        if item == 0:
            pyautogui.click(numberZero[0], numberZero[1])
        elif item == 1:
            pyautogui.click(numberOne[0], numberOne[1])
        elif item == 2:
            pyautogui.click(numberTwo[0], numberTwo[1])
        elif item == 3:
            pyautogui.click(numberThree[0], numberThree[1])
        elif item == 4:
            pyautogui.click(numberFour[0], numberFour[1])
        elif item == 5:
            pyautogui.click(numberFive[0], numberFive[1])
        elif item == 6:
            pyautogui.click(numberSix[0], numberSix[1])
        elif item == 7:
            pyautogui.click(numberSeven[0], numberSeven[1])
        elif item == 8:
            pyautogui.click(numberEight[0], numberEight[1])
        elif item == 9:
            pyautogui.click(numberNine[0], numberNine[1])
    time.sleep(0.5)
    pyautogui.click(acceptKingdomNumber[0], acceptKingdomNumber[1])
    time.sleep(0.5)
    pyautogui.click(goButton[0], goButton[1])
    time.sleep(10)

    # Clicking a tile in the kingdom
    pyautogui.click(950, 530)
    time.sleep(1)
    # Checking if
    text = screen_to_text(migrate_button_pos)
    monster_text = screen_to_text(monster_hunt)
    if text == 'Migrate':
        # Clicking migrate button
        pyautogui.click(migrateButton[0], migrateButton[1])
    else:
        if monster_text == 'Monstergta Umit':
            time.sleep(0.5)
            pyautogui.click(monster_hunt_close[0], monster_hunt_close[1])
        time.sleep(0.5)
        pyautogui.click(600, 630)
        time.sleep(0.5)
        text = screen_to_text(migrate_button_pos)
        if text == 'Migrate':
            time.sleep(0.5)
            pyautogui.click(migrateButton[0], migrateButton[1])
        else:
            pyautogui.click(1600, 744)
            time.sleep(0.5)
            text = screen_to_text(migrate_button_pos)
            if text == 'Migrate':
                pyautogui.click(migrateButton[0], migrateButton[1])
            else:
                row = [x, 'Unknown']
                return row

    time.sleep(1)
    # Taking screenshot of the scroll count
    migrate_scroll = screen_to_text(migrate)

    # Saving the kingdom nubmer and the amount of scrolls to a csv file

    # Close the migration menu
    pyautogui.click(closeButton[0], closeButton[1])
    time.sleep(0.5)
    row = [x, migrate_scroll]
    return row


try:
    time.sleep(5)
    for x in range(368, 720):
        time.sleep(5)
        pyautogui.click(searchKingdomPos[0], searchKingdomPos[1])
        time.sleep(0.5)
        pyautogui.click(kingdomPos[0], kingdomPos[1])
        # Making a list of the numbers in the x number. So 200 turn to 2, 0, 0
        numbers = list(map(int, str(x)))
        with open('scroll_count.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(loop_kingdoms(numbers))
            csvFile.close()

except KeyboardInterrupt:
    print("Done")


