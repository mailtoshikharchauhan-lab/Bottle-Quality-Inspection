#  Bottle Quality Inspection using YOLO11

A real-time Bottle Quality Inspection System built using **YOLO11**, **OpenCV**, and **Python**. The system detects bottles in a video and classifies them into quality categories such as **Perfect Bottle**, **Missing Cap**, **Missing Label**, **Empty Bottle**, and **Crooked Cap**.

---

## 📌 Features

- ✅ Real-time bottle detection using YOLO11
- ✅ Detects 5 bottle quality classes
- ✅ PASS / FAIL quality inspection
- ✅ Professional dashboard
- ✅ Confidence score display
- ✅ Bounding box visualization
- ✅ Video processing using OpenCV
- ✅ Saves annotated output video

---

## 📂 Project Structure

```
Bottle-Quality-Inspection/
│
├── models/
│   └── best.pt
│
├── videos/
│   └── input.mp4
│
├── output/
│   └── output.mp4
│
├── detector.py
├── utils.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Classes

| Class | Description | Result |
|--------|-------------|--------|
| Perfect_bottle | Bottle without any defect | ✅ PASS |
| empty_bottle | Bottle has no liquid | ❌ FAIL |
| no_cap | Bottle cap missing | ❌ FAIL |
| no_label | Bottle label missing | ❌ FAIL |
| crooked_cap | Bottle cap not aligned | ❌ FAIL |

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/mailtoshikharchauhan-lab/Bottle-Quality-Inspection.git

cd Bottle-Quality-Inspection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🖥️ Output

The system displays:

- Bounding Boxes
- Bottle Class
- Confidence Score
- PASS / FAIL Status
- Total Detected Bottles (Current Frame)
- Output Video Saved Automatically

---

## 📊 Example Dashboard

```
Bottle Quality Inspection

Frame : 125

FPS : 28

Detected : 2

PASS : 1

FAIL : 1
```

---

## 🛠️ Tech Stack

- Python
- YOLO11 (Ultralytics)
- OpenCV
- NumPy

---

## 📈 Model

The model was trained on the **Big Cola Bottles Dataset for YOLO Quality Control**.

### Classes

- Perfect Bottle
- Empty Bottle
- Missing Cap
- Missing Label
- Crooked Cap

---

## 📷 Screenshots

Add screenshots inside a folder named `screenshots`.

Example:

```
screenshots/
│
├── dashboard.png
├── pass_detection.png
├── fail_detection.png
└── output_video.png
```

Then display them like this:

```markdown
## Detection

![Detection](screenshots/dashboard.png)

## PASS Detection

![PASS](screenshots/pass_detection.png)

## FAIL Detection

![FAIL](screenshots/fail_detection.png)
```

---

## 🔮 Future Improvements

- Multi-object tracking using ByteTrack
- Conveyor belt counting
- CSV inspection reports
- Save failed bottle images
- Streamlit dashboard
- Industrial PLC integration

---

## 👨‍💻 Author

**Shikhar Chauhan**

GitHub: https://github.com/mailtoshikharchauhan-lab

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project useful, consider giving it a star.
