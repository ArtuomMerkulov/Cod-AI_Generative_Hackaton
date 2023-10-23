import streamlit as st
import openai

openai.api_key = st.secrets["key"]

st.title('Создание новой продуктовой карточки')

def createImageWithGPT(prompt):
  completion = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
  )
  return completion.data[0].url

def generateExplanationText(prompt):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1
    )
    return completion.choices[0].text


col1, col2 = st.columns(2)

col1.write("Проведённая аналитика показала, что параметрами влияющими на продажи являются наименование, бренд, цена, отзывы  и пол(мужская/женская обувь).")


title = col1.text_input('Наименование продукта ', 'Введите наименование продукта ')
brand = col1.text_input('Бренд', 'Введите название  бренда')
color = col1.text_input('Цвет' , 'Введите цвет')

gender = col1.radio(
        "Обувь",
        key="gender",
        options=["мужская","женская" ],)


image_prompt = title+" "+color+" "+brand+ " "+gender+" "+"на белом фоне"
image_url = createImageWithGPT(image_prompt)

text_prompt = title+" "+brand+" "+gender+" "+"Напиши наиболее продаваемое описание"
description = generateExplanationText(text_prompt)

if col1.button("Сгенерировать продуктовую карточку"):
    col2.image(image_url)
    col2.write(description)
else:
    col2.write('Здесь будет карточка')
