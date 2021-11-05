from flask import Flask, render_template, request, redirect, session

def dropsessions():
    session.pop('user', None)
    print("signing out")
    return render_template('login.html')