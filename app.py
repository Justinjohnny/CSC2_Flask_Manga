import json
import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_secret_key'

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / 'manga_shop.db'