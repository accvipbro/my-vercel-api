from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def tiktokview():
    video_url = request.args.get("video")
    if not video_url:
        return jsonify({ "error": "Thiếu link video" }), 400

    try:
        r = requests.get(video_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if r.status_code == 200:
            return jsonify({ "success": True, "message": "Đã gửi view" })
        else:
            return jsonify({ "success": False, "message": f"Lỗi: {r.status_code}" })
    except Exception as e:
        return jsonify({ "success": False, "error": str(e) })

# cần dòng này để Vercel biết app là Flask app
app = app
