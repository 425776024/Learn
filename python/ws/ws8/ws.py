# -*- coding: utf-8 -*-
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import traceback

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        try:
            index = 0
            while 1:
                index += 1
                ws.send("Hello %d" % index)
                time.sleep(1)
        except Exception as e:
            print traceback.format_exc()
        finally:
            ws.close()
            print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()