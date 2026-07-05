import cv2


class UI:

    def __init__(self):

        self.class_names = {
            "Perfect_bottle": "Perfect Bottle",
            "empty_bottle": "Empty Bottle",
            "no_cap": "Missing Cap",
            "no_label": "Missing Label",
            "crooked_cap": "Crooked Cap"
        }

        self.colors = {
            "Perfect_bottle": (0, 220, 0),
            "empty_bottle": (0, 0, 255),
            "no_cap": (0, 140, 255),
            "no_label": (255, 0, 255),
            "crooked_cap": (0, 255, 255)
        }

    # --------------------------------------------
    # Draw Detection
    # --------------------------------------------

    def draw_detection(self, frame, detection):

        class_name = detection["class"]
        confidence = detection["confidence"]
        x1, y1, x2, y2 = detection["bbox"]

        display_name = self.class_names.get(class_name, class_name)

        if class_name == "Perfect_bottle":
            status = "PASS"
        else:
            status = "FAIL"

        color = self.colors.get(class_name, (255,255,255))

        # =============================
        # Thick Bounding Box
        # =============================

        cv2.rectangle(
            frame,
            (x1,y1),
            (x2,y2),
            color,
            6
        )

        # =============================
        # Top Background
        # =============================

        label = f"{display_name}  {confidence*100:.1f}%"

        (tw, th), _ = cv2.getTextSize(
            label,
            cv2.FONT_HERSHEY_SIMPLEX,
            1.3,
            4
        )

        top = max(0, y1 - 65)

        cv2.rectangle(
            frame,
            (x1, top),
            (x1 + tw + 20, y1),
            color,
            -1
        )

        # =============================
        # Label
        # =============================

        cv2.putText(
            frame,
            label,
            (x1 + 10, y1 - 18),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.3,
            (255,255,255),
            4
        )

        # =============================
        # PASS / FAIL
        # =============================

        cv2.putText(
            frame,
            status,
            (x1, y2 + 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            color,
            4
        )

        return status

    # --------------------------------------------
    # Dashboard
    # --------------------------------------------

    def draw_dashboard(self,
                       frame,
                       frame_no,
                       fps,
                       detected,
                       passed,
                       failed):

        cv2.rectangle(
            frame,
            (10,10),
            (520,250),
            (35,35,35),
            -1
        )

        cv2.putText(
            frame,
            "Bottle Quality Inspection",
            (25,45),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0,255,255),
            3
        )

        cv2.putText(
            frame,
            f"Frame     : {frame_no}",
            (25,95),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,255),
            2
        )

        cv2.putText(
            frame,
            f"FPS       : {fps:.1f}",
            (25,135),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,255),
            2
        )

        cv2.putText(
            frame,
            f"Detected  : {detected}",
            (25,175),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,255),
            2
        )

        cv2.putText(
            frame,
            f"PASS      : {passed}",
            (25,215),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"FAIL      : {failed}",
            (260,215),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )