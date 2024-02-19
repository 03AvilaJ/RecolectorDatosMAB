class MyoHandler(Myo):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()

    def on_connect(self, myo, timestamp, firmware_version):
        with self.lock:
            print("Myo Armband conectado!")

    def on_emg(self, myo, timestamp, emg_data):
        with self.lock:
            print("Datos EMG recibidos:", emg_data)
      