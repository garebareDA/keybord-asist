import pyautogui as pgui
from pyhooked import Hook, KeyboardEvent, MouseEvent
from time import sleep


def handle_events(args):
    if isinstance(args, KeyboardEvent):
        if args.key_code == 56 and args.event_type == 'key down' and 'Lshift'in args.pressed_key:
            sleep(0.3)
            pgui.typewrite([')', 'left'])

        elif args.key_code == 219 and args.event_type == 'key down' and 'Lshift'in args.pressed_key:
            sleep(0.3)
            pgui.typewrite(['}', 'left'])

        elif args.key_code == 219 and args.event_type == 'key down' and 'Lshift' not in args.pressed_key:
            sleep(0.3)
            pgui.typewrite([']', 'left'])

        elif args.key_code == 188 and args.event_type == 'key down' and 'Lshift'in args.pressed_key:
            sleep(0.3)
            pgui.typewrite(['>', 'left'])

        elif args.key_code == 190 and args.event_type == 'key down' and 'Lshift'not in args.pressed_key:
            sleep(0.3)
            pgui.typewrite(['return'])


        elif args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            hk.stop()
            print('Quitting.')

hk = Hook()
hk.handler = handle_events
hk.hook()



