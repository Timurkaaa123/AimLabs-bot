def start():
    import cv2
    import time
    import torch

    import src.bot.modules as modules

    import config.config as config


    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)

    prev_time = 0

    while True:
        ret, frame = cap.read()

        # Detection
        targets = modules.aiming.detect(frame)
        if config.ALL_DETECTION_TARGETS_OVERLAY:
            frame = targets.plot()


        # Add FPS overlay
        if config.FPS_OVERLAY:
            frame, fps = modules.visualisation.add_FPS(frame, prev_time, time.time())
            prev_time = time.time()


        # Choose target
        target = modules.aiming.choose_target(targets, frame)
        if config.CURRENT_TARGET_OVERLAY and target:
            frame = modules.visualisation.add_target(frame, target)

        # Shot
        if target:
            modules.aiming.movement(target, frame)
            modules.aiming.shot(target, frame)


        # Window settings
        if config.VISUALISATION:
            cv2.imshow('AimLabs-Bot', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
