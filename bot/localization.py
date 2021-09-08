strings = {
    "en": {
        "error_no_reply": "This command must be sent as a reply to one's message!",
        "error_report_admin": "Whoa! Don't report admins 😈",
        "error_restrict_admin": "You cannot restrict an admin.",

        "report_date_format": "%d.%m.%Y at %H:%M",
        "report_message": '👆 Sent {time} (server time)\n'
                          '<a href="{msg_url}">Go to message</a>',
        "report_note": "\n\nNote: {note}",
        "report_sent": "<i>Report sent</i>",

        "action_del_msg": "Delete message",
        "action_del_and_ban": "Delete and ban",

        "action_deleted": "\n\n🗑 <b>Deleted</b>",
        "action_deleted_banned": "\n\n🗑❌ <b>Deleted, user banned</b>",
        "action_deleted_partially": "Some messages couldn't be found or deleted",

        "readonly_forever": "🙊 <i>User set to read-only mode forever</i>",
        "readonly_temporary": "🙊 <i>User set to read-only mode until {time} (server time)</i>",
        "nomedia_forever": "🖼 <i>User set to text-only mode forever</i>",
        "nomedia_temporary": "🖼 <i>User set to text-only mode until {time} (server time)</i>",

        "need_admins_attention": 'Dear admins, your presence in chat is needed!\n\n'
                                 '<a href="{msg_url}">Go to chat</a>',
    },
    "ru": {
        "error_no_reply": "Эта команда должна быть ответом на какое-либо сообщение!",
        "error_report_admin": "Админов репортишь? Ай-ай-ай 😈",
        "error_restrict_admin": "Невозможно ограничить администратора.",

        "report_date_format": "%d.%m.%Y в %H:%M",
        "report_message": '👆 Отправлено {time} (время серверное)\n'
                          '<a href="{msg_url}">Перейти к сообщению</a>',
        "report_note": "\n\nПримечание: {note}",
        "report_sent": "<i>Жалоба отправлена администраторам</i>",

        "action_del_msg": "Удалить сообщение",
        "action_del_and_ban": "Удалить и забанить",

        "action_deleted": "\n\n🗑 <b>Удалено</b>",
        "action_deleted_banned": "\n\n🗑❌ <b>Удалено, юзер забанен</b>",
        "action_deleted_partially": "Не удалось найти или удалить некоторые сообщения",

        "readonly_forever": "🙊 <i>Пользователь переведён в режим «только чтение» навсегда</i>",
        "readonly_temporary": "🙊 <i>Пользователь переведён в режим «только чтение» до {time} (время серверное)</i>",
        "nomedia_forever": "🖼 <i>Пользователю запрещено отправлять медиафайлы навсегда</i>",
        "nomedia_temporary": "🖼 <i>Пользователю запрещено отправлять медиафайлы до {time} (время серверное)</i>",

        "need_admins_attention": 'Товарищи админы, в чате нужно ваше присутствие!\n\n'
                                 '<a href="{msg_url}">Перейти к чату</a>',
    },
    "de": {
        "error_no_reply": "Dieser Befehl kann nur als Antwort gesendet werden!",
        "error_report_admin": "Whoa! Du kannst Admins nicht melden 😈",
        "error_restrict_admin": "Du kannst keine Admins einschränken.",

        "report_date_format": "%d.%m.%Y um %H:%M Uhr",
        "report_message": '👆 Gesendet {time} (server time)\n'
                          '<a href="{msg_url}">Zur Nachricht</a>',
        "report_note": "\n\nNotiz: {note}",
        "report_sent": "<i>Gemeldet</i>",

        "action_del_msg": "Nachricht löschen",
        "action_del_and_ban": "Löschen und Sperren",

        "action_deleted": "\n\n🗑 <b>Löschen</b>",
        "action_deleted_banned": "\n\n🗑❌ <b>Gelöscht, Nutzer gesperrt!</b>",
        "action_deleted_partially": "Einige Nachrichten wurden nicht gefunden zum löschen",

        "readonly_forever": "🙊 <i>Nutzer ist für immer stumm</i>",
        "readonly_temporary": "🙊 <i>Nutzer bis {time} stumm. (server time)</i>",
        "nomedia_forever": "🖼 <i>Nutzer für immer im Nur-Text-Modus.</i>",
        "nomedia_temporary": "🖼 <i>Nutzer bis {time} im nur Text-Modus. (server time)</i>",

        "need_admins_attention": 'Liebe Admins, ich sehne euch herbei!\n\n'
                                 '<a href="{msg_url}">Zum Chat</a>',
}


 @@ -64,7 +89,7 @@ def get_string(lang: str, key: str):
    lang = strings.get(lang)
    if not lang:
        if not strings.get("en"):
            raise KeyError(f'Neither "{lang}" nor "en" locales found')
            raise KeyError(f'Weder "{lang}" noch "en" gefunden.')
        else:
            lang = strings.get("en")
try:
        return lang[key]
    except KeyError:
        return strings.get("en").get(key, "ERR_NO_STRING")
