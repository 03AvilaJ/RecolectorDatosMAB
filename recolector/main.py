from myo_handler import MyoHandler
import time

def main():
    try:
        myo_handler = MyoHandler()
        myo_handler.connect()
        myo_handler.set_stream_emg(emg_mode.EMG_MODE_RAW)

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Desconectando el Myo Armband...")
        myo_handler.disconnect()

if __name__ == "__main__":
    main()
