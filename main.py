from typing import Union
from api.bot.bot import Bot
from config.settings import CONFIG_KWARGS
from api.bot.utils import form_response_to_user
from flask import Flask, Response, jsonify, request


app = Flask(__name__)
bot = Bot(**CONFIG_KWARGS)
bot.update_webhook()


@app.route("/", methods=["POST", "GET"])
def main() -> Union[Response, str]:
    if request.method == "POST":
        r: dict = request.get_json()
        chat_id, data = form_response_to_user(bot, r)
        bot.send_message(chat_id, text=data)
        return jsonify(r)
    return bot.HTML


if __name__ == "__main__":
    app.run(debug=bot.IS_LOCALHOST)
