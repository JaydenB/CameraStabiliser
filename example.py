from scripts.ui import CameraStabiliserWindow


def run():
    ui = CameraStabiliserWindow()
    ui.exec_()


if __name__ == '__main__':
    app = CameraStabiliserWindow()
    app.exec_()
