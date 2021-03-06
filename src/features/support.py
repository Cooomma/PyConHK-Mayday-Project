'''
Created on May 5, 2017

@author: Comma
'''
import traceback

from config.config import LogConfig, ContentConfig
from constants import conversations
from constants.stages import Stages
from constants.replykeyboards import ReplyKeyboards
from helpers.requests import RequestHelper


logger = LogConfig.logger

conversations = conversations.SupportEvents()
keyboards = ReplyKeyboards()
stage = Stages()
requests_helper = RequestHelper()


def list_events(bot, update, user_data):
    update.message.reply_text(conversations.LIST_EVENTS,
                              reply_markup=keyboards.support_event_keyboard_markup)
    return stage.SUPPORT_EVENT_START


def event_523(bot, update, user_data):
    userid = update.message.from_user.id
    requests_helper.send_promo_metrics(userid, '523上班餘興節目')
    update.message.reply_text(conversations.EVENTS_523,
                              reply_markup=keyboards.support_event_keyboard_markup)
    update.message.reply_text(conversations.EVENT_BACK,
                              reply_markup=keyboards.support_event_keyboard_markup)
    return stage.SUPPORT_EVENT_START


def event_home_kong(bot, update, user_data):
    userid = update.message.from_user.id
    requests_helper.send_promo_metrics(userid, '《五月之約》尋回專屬HOME KONG場的感動')
    update.message.reply_text(conversations.EVENT_HOME_KONG)
    for pic in ['AgADBQAD7KcxGzak-VS3Tc8RdlkBJKcmzDIABMP5dnxxPEBQeekBAAEC',
                'AgADBQAD7acxGzak-VTLffELMMm8IjURzDIABNLPMEaNIBw8zeUBAAEC',
                'AgADBQAD66cxGzak-VTDj1_dsgEYa88WzDIABFHRx6fhGHY3POQBAAEC']:
        update.message.reply_photo(pic)
    update.message.reply_text(conversations.EVENT_HOME_KONG_CREDIT)
    update.message.reply_text(conversations.EVENT_BACK, reply_markup=keyboards.support_event_keyboard_markup)
    return stage.SUPPORT_EVENT_START
