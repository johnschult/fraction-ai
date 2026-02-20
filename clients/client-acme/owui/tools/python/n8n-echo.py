import requests # type: ignore


class Tools:
    def __init__(self):
        self.webhook_url = (
            "http://192.168.68.130:5678/webhook/43ed87d9-67d0-4ef5-bbd2-2ef54ce60dd7"
        )

    def n8n_echo(
        self,
        body: dict,
        __user__: dict = None,
        __metadata__: dict = None,
        __model__: dict = None,
    ) -> str:
        message = (
            body.get("text") or body.get("input") or body.get("message") or str(body)
        )

        # Model info
        model_id = None
        model_name = None
        if isinstance(__model__, dict):
            model_id = __model__.get("id")
            model_name = __model__.get("name") or model_id
        model_id = model_id or "unknown-model"
        model_name = model_name or model_id

        # User info
        user_id = "anonymous"
        user_label = "anonymous"
        if isinstance(__user__, dict):
            user_id = __user__.get("id") or user_id
            # Try nice fields before falling back to id
            user_label = (
                __user__.get("username")
                or __user__.get("name")
                or __user__.get("email")
                or user_id
            )

        # Session/chat info
        session_id = "unknown-session"
        session_label = "unknown-session"
        if isinstance(__metadata__, dict):
            session_id = (
                __metadata__.get("chat_id")
                or __metadata__.get("session_id")
                or __metadata__.get("id")
                or session_id
            )
            session_label = __metadata__.get("title") or session_id

        payload = {
            "message": message,
            "metadata": {
                "model": {
                    "id": model_id,
                    "name": model_name,
                },
                "user": {
                    "id": user_id,
                    "label": user_label,
                },
                "session": {
                    "id": session_id,
                    "label": session_label,
                },
            },
        }

        resp = requests.post(self.webhook_url, json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        if isinstance(data, list) and data and isinstance(data[0], dict):
            if "output" in data[0]:
                return str(data[0]["output"])
        if isinstance(data, dict) and "output" in data:
            return str(data["output"])
        return str(data)
