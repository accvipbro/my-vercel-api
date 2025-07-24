import json
import requests

def handler(request, response):
    video_url = request.query.get("video")
    if not video_url:
        response.status_code = 400
        return response.json({ "error": "Thiếu link video" })

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(video_url, headers=headers, timeout=10)
        if r.status_code == 200:
            return response.json({ "success": True, "message": "Đã gửi view" })
        else:
            return response.json({ "success": False, "message": f"Lỗi: {r.status_code}" })
    except Exception as e:
        return response.json({ "success": False, "error": str(e) })
