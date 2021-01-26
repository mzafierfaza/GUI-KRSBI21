import PySimpleGUI as sg


class HSV:

    def __init__(self, h, s, v):
        self.H = h
        self.S = s
        self.V = v


BolaDepan = HSV(200, 200, 200)
BolaAtas = HSV(200, 200, 200)
LapanganDepan = HSV(200, 200, 200)
LapanganAtas = HSV(200, 200, 200)

# Define the window layout
col_trackbar_cam = [
    [sg.Text("HSV FRONT BALL    ||    HSV UPPER BALL",
             justification="center", font=(12))],
    [sg.HorizontalSeparator()],     # pemisahh
    [
        sg.Text("H"),
        sg.Slider(
            (0, 255),
            BolaDepan.H,
            1,
            orientation="h",
            size=(15, 15),
            key="-H_MIN_FR_BALL-",
        ),
        sg.VSeperator(),
        sg.Slider(
            (0, 255),
            BolaAtas.H,
            1,
            orientation="h",
            size=(15, 15),
            key="-H_MIN_UP_BALL-",
        ),
    ],
    [
        sg.Text("S"),
        sg.Slider(
            (0, 255),
            BolaDepan.S,
            1,
            orientation="h",
            size=(15, 15),
            key="-S_MIN_FR_BALL-",
        ),
        sg.VSeperator(),
        sg.Slider(
            (0, 255),
            BolaAtas.S,
            1,
            orientation="h",
            size=(15, 15),
            key="-S_MIN_UP_BALL-",
        ),
    ],
    [
        sg.Text("V"),
        sg.Slider(
            (0, 255),
            BolaDepan.V,
            1,
            orientation="h",
            size=(15, 15),
            key="-V_MIN_FR_BALL-",
        ),
        sg.VSeperator(),
        sg.Slider(
            (0, 255),
            BolaAtas.V,
            1,
            orientation="h",
            size=(15, 15),
            key="-V_MIN_UP_BALL-",
        ),
    ],
    [sg.HSeparator()],     # pemisahh
    [sg.Text("HSV FRONT FIELD     ||   HSV UPPER FIELD",
             justification="center", font=(12))],
    [sg.HorizontalSeparator()],     # pemisahh
    [
        sg.Text("H"),
        sg.Slider(
            (0, 255),
            LapanganDepan.H,
            1,
            orientation="h",
            size=(15, 15),
            key="-H_MIN_FR_FIELD-",
        ),
        sg.VSeperator(),
        sg.Slider(
            (0, 255),
            LapanganAtas.H,
            1,
            orientation="h",
            size=(15, 15),
            key="-H_MIN_UP_FIELD-",
        ),
    ],
    [
        sg.Text("S"),
        sg.Slider(
            (0, 255),
            LapanganDepan.S,
            1,
            orientation="h",
            size=(15, 15),
            key="-S_MIN_FR_FIELD-",
        ),
        sg.VSeperator(),
        sg.Slider(
            (0, 255),
            LapanganAtas.S,
            1,
            orientation="h",
            size=(15, 15),
            key="-S_MIN_UP_FIELD-",
        ),
    ],
    [
        sg.Text("V"),
        sg.Slider(
            (0, 255),
            LapanganDepan.V,
            1,
            orientation="h",
            size=(15, 15),
            key="-V_MIN_FR_FIELD-",
        ),
        sg.VSeperator(),
        sg.Slider(
            (0, 255),
            LapanganAtas.V,
            1,
            orientation="h",
            size=(15, 15),
            key="-V_MIN_UP_FIELD-",
        ),
    ],
]


# First the window layout in 2 columns
col_setting = [
    [sg.Text("           KIRANA SRIWIJAYA 2021", size=(35, 0), font=(12))],
]

col_monitor_kalibrasi = [
    [sg.Text("Kalibrasi from user : X Y T", size=(23, 0), font=(12))],
]

col_monitor_refbox = [
    [sg.Text("Data refbox masuk : ", size=(23, 0), font=(12))],
]

col_monitor_ball = [
    [sg.Text("Monitor data bola (x,y) : ", font=(12), size=(23, 0))],
]

col_monitor_serial = [
    [sg.Text("Monitor Serial out : ", font=(12), size=(26, 0))],
]

# =============== COLUMN FRAME ================


col_front_frame = [
    [sg.Image(filename="", key="-FRAME_FR-")],
]


col_upper_frame = [
    [sg.Image(filename="", key="-FRAME_UP-")],
]

# =============== COLUMN HSV ================


col_front_ball = [
    [sg.Image(filename="", key="-BALL_FR-")],
]


col_front_field = [
    [sg.Image(filename="", key="-FIELD_FR-")],
]

col_upper_ball = [
    [sg.Image(filename="", key="-BALL_UP-")],
]

col_upper_field = [
    [sg.Image(filename="", key="-FIELD_UP-")],
]


# ----- Full layout -----
layout2 = [
    [
        sg.Column(col_trackbar_cam),
        sg.VSeperator(),
        sg.Column(col_front_frame),
        sg.VSeperator(),
        sg.Column(col_upper_frame),
        sg.VSeperator(),

    ],
    [
        sg.Image("logo.png", key='key1', size=(240, 150)),
        sg.VSeperator(),
        sg.Column(col_front_ball),
        sg.Column(col_front_field),
        sg.VSeperator(),
        sg.Column(col_upper_ball),
        sg.Column(col_upper_field),
        sg.VSeperator(),
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Column(col_setting),
        sg.VSeperator(),
        sg.Column(col_monitor_ball),
        sg.VSeperator(),
        sg.Column(col_monitor_refbox),
        sg.VSeperator(),
        sg.Column(col_monitor_kalibrasi),
        sg.VSeperator(),
        sg.Column(col_monitor_serial),
        sg.VSeperator(),

    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Output(size=(50, 8)),
        sg.VSeperator(),
        sg.Output(key="-MON_SERIAL-", size=(33, 8)),
        sg.VSeperator(),
        sg.Output(key="-MON_DATAA-", size=(33, 8)),
        sg.VSeperator(),
        sg.Output(key="-MON_ads-", size=(33, 8)),
        sg.VSeperator(),
        sg.Output(key="-MON_Sasdf-", size=(35, 8)),
        sg.VSeperator(),

    ]
]
