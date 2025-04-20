import os
import subprocess
from PIL import Image, ImageChops, ImageDraw
import numpy as np

def extract_frames(video_file="video.h264", frame_dir="frames", fps=5):
    """Extract frames from video using ffmpeg."""
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    # Clear previous frames
    for f in os.listdir(frame_dir):
        os.remove(os.path.join(frame_dir, f))

    cmd = [
        "ffmpeg",
        "-i", video_file,
        "-vf", f"fps={fps}",
        os.path.join(frame_dir, "frame_%03d.jpg")
    ]
    subprocess.run(cmd)
    print(f"[INFO] Extracted frames to '{frame_dir}'.")

def detect_hand_to_mouth_motion(frame_dir="frames", roi=(150, 100, 450, 350), threshold=15):
    """Detect motion in ROI between frames, show and keep only the detected one."""
    frames = sorted([f for f in os.listdir(frame_dir) if f.endswith(".jpg")])
    motion_frame_path = None

    for i in range(len(frames) - 1):
        path1 = os.path.join(frame_dir, frames[i])
        path2 = os.path.join(frame_dir, frames[i + 1])

        f1 = Image.open(path1).convert("L")
        f2 = Image.open(path2).convert("L")

        r1 = f1.crop(roi)
        r2 = f2.crop(roi)

        diff = ImageChops.difference(r1, r2)
        mean_change = np.mean(np.array(diff))

        if mean_change > threshold:
            # ✅ Save frame with green rectangle
            original = Image.open(path2).convert("RGB")
            draw = ImageDraw.Draw(original)
            draw.rectangle(roi, outline="green", width=4)

            motion_frame_path = os.path.join(frame_dir, "motion_detected.jpg")
            original.save(motion_frame_path)
            print(f"✅ Motion detected! Frame saved as {motion_frame_path}")

            # 🧹 Delete all other frames
            for f in frames:
                full_path = os.path.join(frame_dir, f)
                if os.path.exists(full_path) and f != "motion_detected.jpg":
                    os.remove(full_path)

            # 👀 Show image on screen (Raspberry Pi GUI)
            os.system(f"xdg-open {motion_frame_path}")
            return True

    # ❌ No motion: clean up all frames
    for f in frames:
        os.remove(os.path.join(frame_dir, f))

    print("❌ No significant motion near mouth.")
    return False

# === MAIN EXECUTION ===

video_file = "video.h264"  # Make sure this exists
extract_frames(video_file)

if detect_hand_to_mouth_motion():
    print("✅ Pill taken.")
else:
    print("⚠ Pill not taken. Kindly Confirm!")
