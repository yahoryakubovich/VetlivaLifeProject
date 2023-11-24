from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from sqlalchemy.orm import Session
from main import dp
from models import User, SessionLocal


class SurveyStates:
    waiting_for_age = "waiting_for_age"
    waiting_for_problem = "waiting_for_problem"
    waiting_for_condition = "waiting_for_condition"
    waiting_for_experience = "waiting_for_experience"
    waiting_for_preferences = "waiting_for_preferences"
    waiting_for_approach = "waiting_for_approach"
    waiting_for_format = "waiting_for_format"
    waiting_for_price = "waiting_for_price"
    waiting_for_young_specialist = "waiting_for_young_specialist"
    waiting_for_additional_wishes = "waiting_for_additional_wishes"
    waiting_for_source = "waiting_for_source"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@dp.message_handler(Command("survey"))
async def cmd_survey_start(message: types.Message, state: FSMContext):
    if await state.get_state() is not None:
        await state.finish()
    await state.update_data(survey_state=SurveyStates.waiting_for_age)
    await message.answer("Давайте начнем анкету. Вопрос 1: Сколько вам лет?")


# Обработчик текстовых сообщений в состоянии "waiting_for_age"
@dp.message_handler(state=SurveyStates.waiting_for_age)
async def process_age(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о возрасте
    user_age = message.text
    await state.update_data(age=user_age)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_problem)
    await message.answer("Вопрос 2: Какая проблема вас тревожит?", reply_markup=types.ReplyKeyboardRemove())


# Обработчик текстовых сообщений в состоянии "waiting_for_problem"
@dp.message_handler(state=SurveyStates.waiting_for_problem)
async def process_problem(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о проблеме
    user_problem = message.text
    await state.update_data(problem=user_problem)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_condition)
    await message.answer("Вопрос 3: Пожалуйста, укажите, что вас беспокоит в вашем состоянии?")


# Обработчик текстовых сообщений в состоянии "waiting_for_condition"
@dp.message_handler(state=SurveyStates.waiting_for_condition)
async def process_condition(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о состоянии пользователя
    user_condition = message.text

    # Добавляем состояние в данные состояния
    await state.update_data(condition=user_condition)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_experience)
    await message.answer("Вопрос 4: Был ли опыт работы с психологом/психотерапевтом ранее? "
                         "Если да: Что не понравилось? Если нет: введите 'Нет'.")


# Обработчик текстовых сообщений в состоянии "waiting_for_experience"
@dp.message_handler(state=SurveyStates.waiting_for_experience)
async def process_experience(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос об опыте работы с психологом/психотерапевтом
    user_experience = message.text

    # Добавляем опыт в данные состояния
    await state.update_data(experience=user_experience)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_preferences)
    await message.answer("Вопрос 5: Есть ли пожелания по полу специалиста?")


# Обработчик текстовых сообщений в состоянии "waiting_for_preferences"
@dp.message_handler(state=SurveyStates.waiting_for_preferences)
async def process_preferences(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о предпочтениях по полу специалиста
    user_preferences = message.text

    # Добавляем предпочтения в данные состояния
    await state.update_data(preferences=user_preferences)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_approach)
    await message.answer("Вопрос 6: Какой подход тебе ближе?")


# Обработчик текстовых сообщений в состоянии "waiting_for_approach"
@dp.message_handler(state=SurveyStates.waiting_for_approach)
async def process_approach(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о предпочтениях по подходу
    user_approach = message.text

    # Добавляем подход в данные состояния
    await state.update_data(approach=user_approach)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_format)
    await message.answer("Вопрос 7: Какой формат работы более комфортен для тебя?")


# Обработчик текстовых сообщений в состоянии "waiting_for_format"
@dp.message_handler(state=SurveyStates.waiting_for_format)
async def process_format(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о формате работы
    user_format = message.text

    # Добавляем формат в данные состояния
    await state.update_data(format=user_format)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_price)
    await message.answer("Вопрос 8: Какая цена за сессию для тебя будет комфортной?")


# Обработчик текстовых сообщений в состоянии "waiting_for_price"
@dp.message_handler(state=SurveyStates.waiting_for_price)
async def process_price(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о комфортной цене за сессию
    user_price = message.text

    # Добавляем цену в данные состояния
    await state.update_data(price=user_price)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_young_specialist)
    await message.answer("Вопрос 9: Комфортно ли тебе будет работать с молодым специалистом?")


# Обработчик текстовых сообщений в состоянии "waiting_for_young_specialist"
@dp.message_handler(state=SurveyStates.waiting_for_young_specialist)
async def process_young_specialist(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о комфорте работы с молодым специалистом
    user_young_specialist = message.text

    # Добавляем ответ в данные состояния
    await state.update_data(young_specialist=user_young_specialist)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_additional_wishes)
    await message.answer(
        "Вопрос 10: Может, есть еще какие-то пожелания к специалисту, о которых ты хотел бы нам сказать? "
        "Если да, введи их. Если нет, введи 'Нет'.")


# Обработчик текстовых сообщений в состоянии "waiting_for_additional_wishes"
@dp.message_handler(state=SurveyStates.waiting_for_additional_wishes)
async def process_additional_wishes(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос о дополнительных пожеланиях
    user_additional_wishes = message.text

    # Добавляем пожелания в данные состояния
    await state.update_data(additional_wishes=user_additional_wishes)

    # Переход к следующему вопросу
    await state.update_data(survey_state=SurveyStates.waiting_for_source)
    await message.answer("Вопрос 11: Откуда ты узнал о нашем проекте?")


# Обработчик текстовых сообщений в состоянии "waiting_for_source"
@dp.message_handler(state=SurveyStates.waiting_for_source)
async def process_source(message: types.Message, state: FSMContext):
    # Логика обработки ответа на вопрос об источнике узнавания о проекте
    user_source = message.text

    # Добавляем источник в данные состояния
    await state.update_data(source=user_source)

    # Анкета завершена, записываем данные в базу данных
    async with get_db() as db:
        data = state.get_data()
        db_user = User(
            name=data.get("name"),
            age=data.get("age"),
            problem=data.get("problem"),
            condition=data.get("condition"),
            experience=data.get("experience"),
            preferences=data.get("preferences"),
            approach=data.get("approach"),
            format=data.get("format"),
            price=data.get("price"),
            young_specialist=data.get("young_specialist"),
            additional_wishes=data.get("additional_wishes"),
            source=user_source
        )
        db.add(db_user)
        db.commit()

    await message.answer("Спасибо за заполнение анкеты! Ваши ответы сохранены.")
    await state.finish()
