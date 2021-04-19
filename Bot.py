from telegram import Update
from telegram import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup
from telegram.ext import CommandHandler, Updater, CallbackContext, Filters, MessageHandler

import GameAI
import config
import json

class TeleBot:

    __button_help = f"🆘 Помощь"
    __button_restart = f"🔃 Рестарт"
    __button_explanation_question = f"🔎 Объяснение вопроса"
    __button_explanation_decisions = f"🌐 Объяснение решения"
    __button_start = "Cтарт"
    __welcome_text = "Добро пожаловать в экспертную систему 'Разработка игры'"
    __help_text = "Это бот по экспертной системе 'Разработка игры'"

    def __init__(self):
        self.__predictor = GameAI.GamePredictor()
        self.__updater = Updater(
            token=config.BOT_TOKEN,
            use_context=True,
        )

        dp = self.__updater.dispatcher

        dp.add_handler(CommandHandler("start", self.__start_command))
        dp.add_handler(CommandHandler("help", self.__help_command))

        dp.add_handler(MessageHandler(filters=Filters.all, callback= self.__message_handler))

    def __log_error(self, f):

        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                print(f'Error: {e}')
                raise e

        return inner

    def __start_command(self, update, context):
        self.__predictor = GameAI.GamePredictor()
        buttons = [KeyboardButton(f'{self.__button_start}')]

        reply_markup = ReplyKeyboardMarkup(
            keyboard=self.build_menu(buttons, 2),
            resize_keyboard=True,
            one_time_keyboard=True
        )

        update.message.reply_text(text=f'{self.__welcome_text}', reply_markup=reply_markup)

    def __restart_command(self, update, context):
        self.__predictor.reset()
        buttons = [KeyboardButton(f'{self.__button_start}')]

        reply_markup = ReplyKeyboardMarkup(
            keyboard=self.build_menu(buttons, 2),
            resize_keyboard=True,
            one_time_keyboard=True)

        update.message.reply_text(text=f'{self.__welcome_text}', reply_markup=reply_markup)

    def __help_command(self, update, context):
        update.message.reply_text(text=f'{self.__help_text}')

    def __button_help_handler(self, update: Update, context: CallbackContext):
        update.message.reply_text(text="Помощь",
                                  reply_markup=ReplyKeyboardRemove(), )

    def __print_message(self, update: Update, message):
        update.message.reply_text(text=str(message))

    def build_menu(self, buttons, n_cols,
                   header_buttons=None,
                   footer_buttons=None):
        menu = []

        for i in range(0, len(buttons), n_cols):
            menu.append(buttons[i:i + n_cols])

        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu

    def __print_question(self, update: Update, context: CallbackContext, question: GameAI.Question):

        buttons = []

        for answer in question.answers:
            buttons.append(KeyboardButton(f'{answer.answer}'))

        buttons.append(KeyboardButton(self.__button_restart))
        buttons.append(KeyboardButton(self.__button_explanation_question))

        reply_markup = ReplyKeyboardMarkup(
            keyboard = self.build_menu(buttons, 2),
            resize_keyboard= True,
            one_time_keyboard= True
        )

        update.message.reply_text(text=f'❓ {question.question}', reply_markup=reply_markup)

    def __print_help(self, update: Update, context: CallbackContext, question: GameAI.Question):

        buttons = []

        for answer in question.answers:
            buttons.append(KeyboardButton(f'{answer.answer}'))

        buttons.append(KeyboardButton(self.__button_restart))
        buttons.append(KeyboardButton(self.__button_help))

        reply_markup = ReplyKeyboardMarkup(
            keyboard = self.build_menu(buttons, 2),
            resize_keyboard= True,
            one_time_keyboard= True
        )

        update.message.reply_text(text=f'🔎 {question.description}', reply_markup=reply_markup)

    def __print_prediction(self, update: Update, context: CallbackContext, question: GameAI.Question):
        buttons = []
        buttons.append(KeyboardButton(self.__button_restart))

        reply_markup = ReplyKeyboardMarkup(
            keyboard=self.build_menu(buttons, 2, KeyboardButton(self.__button_explanation_decisions)),
            resize_keyboard=True,
            one_time_keyboard=True
        )

        update.message.reply_text(text=f'✅ {question.prediction.text}', reply_markup=reply_markup)

        if(question.prediction.src != None and question.prediction.img != None):
            update.message.reply_photo(photo = question.prediction.img, caption=f"Ссылка на <a href='{question.prediction.src}'>игру</a>", parse_mode='HTML')

    def __print_explanation_question(self, update: Update, context: CallbackContext, question: GameAI.Question):
        buttons = []

        for answer in question.answers:
            buttons.append(KeyboardButton(f'{answer.answer}'))

        buttons.append(KeyboardButton(self.__button_restart))
        buttons.append(KeyboardButton(self.__button_explanation_question))

        reply_markup = ReplyKeyboardMarkup(
            keyboard=self.build_menu(buttons, 2),
            resize_keyboard=True,
            one_time_keyboard=True
        )

        update.message.reply_text(text=f'🔎 {question.description}', reply_markup=reply_markup)
        pass

    def __print_explanation_decisions(self, update: Update, context: CallbackContext):
        history = self.__predictor.getHistoryQuestions()
        text = f"Вы выбрали варианты ответа:\n"

        print(history)
        for question in history:
            text += f"🔹 {question[0].question} : - {question[1].answer} \n"

        text += f"По данным ответам можно сделать вывод о том, что:\n"
        text += f"✅ {self.__predictor.getQuestion().prediction.text}"

        buttons = []
        buttons.append(KeyboardButton(self.__button_restart))

        reply_markup = ReplyKeyboardMarkup(
            keyboard=self.build_menu(buttons, 2, KeyboardButton(self.__button_explanation_decisions)),
            resize_keyboard=True,
            one_time_keyboard=True
        )

        update.message.reply_text(text=text, reply_markup=reply_markup)


    def __message_handler(self, update: Update, context: CallbackContext):
        text = update.message.text
        print(f"[{update.message.date.ctime()}] {update.effective_user.username}({update.effective_user.id}) : {text}")

        if (text == self.__button_restart):
            self.__restart_command(update, context)
            return

        if (text == self.__button_start):
            self.__print_question(update, context, self.__predictor.getQuestion())
            return

        if(text == self.__button_help):
            self.__print_help(update, context, self.__predictor.getQuestion())
            return

        if(text == self.__button_explanation_decisions):
            self.__print_explanation_decisions(update, context)
            return

        if (text == self.__button_explanation_question):
            self.__print_explanation_question(update, context, self.__predictor.getQuestion())
            return


        self.__predictor.tryNext(text)

        if not self.__predictor.IsEnd():
            self.__print_question(update, context, self.__predictor.getQuestion())
            return

        self.__print_prediction(update, context, self.__predictor.getQuestion())

    def Start(self):
        self.__updater.start_polling()
        self.__updater.idle()
