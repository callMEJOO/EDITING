# keyboards/main_menu.py

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ==================================
# القائمة الرئيسية
# ==================================
def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📦 ضغط فيديو",
                    callback_data="compress"
                ),
                InlineKeyboardButton(
                    text="🎞 تحويل صيغة",
                    callback_data="convert"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚡ ضغط سريع",
                    callback_data="fast"
                ),
                InlineKeyboardButton(
                    text="🎚 الإعدادات",
                    callback_data="settings"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📊 حالة السيرفر",
                    callback_data="status"
                ),
                InlineKeyboardButton(
                    text="👑 VIP",
                    callback_data="vip"
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