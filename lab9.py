#Лабораторная_9. Вариант_3:Подсчитать количество мужчин и количество женщин, указав спасен/погиб и число или %.
import streamlit as st
import matplotlib.pyplot as plt

st.image('titanik.jpg')
info = {"мужчин": 0, "женщин": 0}
total_passengers = 0
st.header('Информация по пассажирам Титаника, c разделением по половому признаку')
st.write('Для просмотра информации о пассажирах мужчинах и женщинах выберите соответствующий пункт из списка.')
selected_value = st.selectbox('Значение поля выжившие:', ['Всего', 'Выживших (1)', 'Погибших (0)'])
selected_percent = st.checkbox('процент от общего количества пассажиров')

with open("data.csv") as file:
    for line in file:
        data = line.split(',')
        sex = data[5]
        sur = data[1]
        if selected_value == "Всего":
            if sex == 'Age':
                continue
            if sex == 'female':
                info['женщин'] += 1
            elif sex == 'male':
                info['мужчин'] += 1
        elif selected_value == "Выживших (1)" and sur == '1':
            if sex == 'female':
                info['женщин'] += 1
            elif sex == 'male':
                info['мужчин'] += 1
        elif selected_value == "Погибших (0)" and sur == '0':
            if sex == 'female':
                info['женщин'] += 1
            elif sex == 'male':
                info['мужчин'] += 1

fig = plt.figure(figsize=(7, 4))
if selected_percent:
    total_passengers = info["мужчин"] + info["женщин"]
    info = {"мужчин": round(info["мужчин"] / total_passengers * 100,2) , "женщин": round(info["женщин"] / total_passengers * 100,2)}
    plt.bar(['мужчин', 'женщин'], [info["мужчин"], info["женщин"]])
    plt.ylabel('процент')
    st.dataframe(info)
else:
    info = {"мужчин": info["мужчин"], "женщин": info["женщин"]}
    plt.bar(['мужчин', 'женщин'], [info["мужчин"], info["женщин"]])
    plt.ylabel('количество')
    st.dataframe(info)
plt.xlabel('Пассажиры')
plt.title('Количество мужчин и женщин')
st.pyplot(fig)