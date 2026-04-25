# quality_menu.py

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


# ==================================
# قائمة الجودة
# ==================================
def quality_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔥 جودة عالية",
                    callback_data="q_24"
                ),
                InlineKeyboardButton(
                    text="⚖ جودة متوسطة",
                    callback_data="q_28"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📉 أقصى ضغط",
                    callback_data="q_32"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏠 الرئيسية",
                    callback_data="home"
                )
            ]
        ]
    )

    return keyboard
