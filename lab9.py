#Лабораторная_9. Вариант_3:Подсчитать количество мужчин и количество женщин, указав спасен/погиб и число или %.
import streamlit as st
import matplotlib.pyplot as plt
st.image('titanik.jpg')
info = {"мужчин:":0,"женщин:":0}
st.header('Информация по пассажирам Титаника, c разделением по половому признаку')
st.write('Для просмотра информации о пассажирах мужчинах и женщинах выберите соответствующий пункт из списка.')
selected_value = st.selectbox('Значение поля Survived:', ['Всего', 'Выживших (1)', 'Погибших (0)'])
with open("data.csv") as file:
    for line in file:
        data = line.split (',')
        sex = data[5]
        sur = data[1]
        if selected_value == "Всего":
            if sex == 'Age':
                continue
            if sex == 'male':
                info ["мужчин:"] += 1
            else:
                info["женщин:"] += 1
        if selected_value == "Выживших (1)" and sur == '1':
            if sex == 'male':
                info["мужчин:"] += 1
            else:
                info["женщин:"] += 1
        if selected_value == "Погибших (0)" and sur == '0':
            if sex == 'male':
                info["мужчин:"] += 1
            else:
                info["женщин:"] += 1
st.dataframe(info)
fig = plt.figure(figsize=(7,4))
plt.bar(['мужчин','женщин'],[info["мужчин:"],info["женщин:"]])
plt.ylabel('количество')
st.pyplot(fig)