from flask import Flask, render_template, request
from faker import Faker
import csv
import pandas as pd
import requests

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return 'Домашнее задание Глонти Нико'


@app.route('/requirements')
def requirements():
    with open("requirements.txt", "r") as f:
        text = f.read()
        return text


@app.route('/user')
def generate_users():
    my_list = []
    for i in range(100):
        my_list.append(f'{fake.name()}: {fake.email()}<br>')
    user = ''.join(my_list)
    return user


@app.route('/mean')
def mean():
    data = pd.read_csv('hw.csv')
    mean_height = str(data[' Height'].mean())
    mean_weight = str(data[' Weight'].mean())
    out = f"Средний рост: {mean_height}, Cредний вес: {mean_weight}"
    return out


@app.route('/space')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    out = str(r.json()["number"])
    return f'Сейчас в космосе:{out}'


if __name__ == '__main__':
    app.run(debug=True)
