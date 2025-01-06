# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PDjC1a7l-AvQYzLhZ3nF1XWExQyXGERk
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

# 加载模型
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 应用标题
st.title("贫血检测模型部署")
st.write("通过输入性别和 RGB 值来判断是否发生贫血")

# 侧边栏输入
st.sidebar.header("输入数据")

# 添加性别选择
sex = st.sidebar.selectbox(
    "性别",
    options=['Male', 'Female']
)

# RGB 数值输入
red_pixel = st.sidebar.slider("红色像素比例（%Red Pixel）", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
green_pixel = st.sidebar.slider("绿色像素比例（%Green pixel）", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
blue_pixel = st.sidebar.slider("蓝色像素比例（%Blue pixel）", min_value=0.0, max_value=100.0, value=50.0, step=0.1)

# 显示用户输入
st.write("您输入的数据如下：")
st.write(f"性别: {sex}")
st.write(f"红色像素比例: {red_pixel}%")
st.write(f"绿色像素比例: {green_pixel}%")
st.write(f"蓝色像素比例: {blue_pixel}%")

# 预测按钮
if st.button("预测是否贫血"):
    try:
        # 创建输入数据框，确保特征顺序与训练时一致
        input_data = pd.DataFrame({
            'Sex': [sex],
            '%Red Pixel': [red_pixel],
            '%Green pixel': [green_pixel],
            '%Blue pixel': [blue_pixel]
        })

        # 使用模型预测
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)

        # 显示预测结果
        st.subheader("预测结果")
        if prediction[0] == "Yes":
            st.write("结果：贫血")
        else:
            st.write("结果：未贫血")

        # 显示置信概率
        st.write("模型置信概率：")
        st.write(f"未贫血（No）：{prediction_proba[0][0]:.2f}")
        st.write(f"贫血（Yes）：{prediction_proba[0][1]:.2f}")

    except Exception as e:
        st.error(f"预测过程中出现错误：{str(e)}")