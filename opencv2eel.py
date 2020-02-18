#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import base64

import eel
import cv2 as cv


def main():
    cap = cv.VideoCapture(0)

    # Eelフォルダ設定、および起動 ###############################################
    eel.init('web')
    eel.start(
        'index.html',
        mode='chrome',
        cmdline_args=['--start-fullscreen'],
        block=False)

    while True:
        start_time = time.time()

        eel.sleep(0.01)

        # カメラキャプチャ #####################################################
        ret, frame = cap.read()
        if not ret:
            continue

        # UI側へ転送(画像) #####################################################
        _, imencode_image = cv.imencode('.jpg', frame)
        base64_image = base64.b64encode(imencode_image)
        eel.set_base64image("data:image/jpg;base64," +
                            base64_image.decode("ascii"))

        key = cv.waitKey(1)
        if key == 27:  # ESC
            break

        # UI側へ転送(処理時間) #################################################
        elapsed_time = round((time.time() - start_time), 3)
        eel.set_elapsedtime(elapsed_time)


if __name__ == '__main__':
    main()
