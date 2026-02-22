import urllib.request
import urllib.parse
import json

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect


@require_POST
@csrf_protect
def feedback_submit(request):
    name = request.POST.get("name", "").strip()
    phone = request.POST.get("phone", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not phone:
        return JsonResponse({"ok": False, "error": "Заполните обязательные поля"}, status=400)

    text = (
        f"📩 <b>Новая заявка с сайта</b>\n\n"
        f"<b>Имя:</b> {name}\n"
        f"<b>Телефон:</b> {phone}"
    )
    if message:
        text += f"\n<b>Сообщение:</b> {message}"

    bot_token = getattr(settings, "TELEGRAM_BOT_TOKEN", "")
    chat_id = getattr(settings, "TELEGRAM_CHAT_ID", "")

    if not bot_token or not chat_id:
        return JsonResponse({"ok": False, "error": "Telegram не настроен"}, status=500)

    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }).encode()

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    req = urllib.request.Request(url, data=payload, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read())
            if result.get("ok"):
                return JsonResponse({"ok": True})
            return JsonResponse({"ok": False, "error": "Telegram error"}, status=500)
    except Exception:
        return JsonResponse({"ok": False, "error": "Ошибка соединения"}, status=500)
