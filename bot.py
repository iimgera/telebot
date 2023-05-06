import os
import logging
import bot_config
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import executor
from django.core.files import File
from works.models import Project


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())

# pro = Project.objects.create(title='gera', description='hello world', image='media/projects/file_11.jpg', link='www.inst.com')
# print(pro.description)

project_instance = Project()


class Project(StatesGroup):
    add_project = State()
    title = State()
    description = State()
    image = State()
    link = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(
        'Привет! Хотите добавить проект?',
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ],
            ],
        )
    )
    await Project.add_project.set()


@dp.message_handler(state=Project.add_project)
@dp.message_handler(lambda message: message.text == 'Да')
async def add_project(message: types.Message, state: FSMContext):
    await message.answer('Введите название проекта:')
    project_instance.title = message.text
    await Project.title.set()


@dp.message_handler(state=Project.title)
async def process_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await message.answer('Введите описание проекта:')
    project_instance.description = message.text
    await Project.description.set()


@dp.message_handler(state=Project.description)
async def process_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await message.answer('Пришлите фотографию проекта:')
    project_instance.image = message.text
    await Project.image.set()

@dp.message_handler(content_types=['photo'], state=Project.image)
async def process_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        photo = message.photo[-1]
        photo_path = f"media/projects/{data['title']}.jpg"
        upload_dir = os.path.dirname(photo_path)
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        await photo.download(destination_file=photo_path)
        data['image'] = photo_path
        await state.update_data(data) 
    project_instance = Project()  
    project_instance.image = photo_path
    await message.answer('Введите ссылку на проект:')
    await state.update_data(project_instance=project_instance)  
    await Project.link.set()




@dp.message_handler(state=Project.link)
async def process_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        project_instance = data['project_instance']
        data['link'] = message.text
        project_instance.link = message.text
    await state.finish()
    await message.answer('Проект сохранен!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)